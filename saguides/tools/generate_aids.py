#!/usr/bin/env python3
"""
Deterministic SVG generator for the STAAR Supplemental Aid Candidate Library.

Per project spec section 13 (Programmatic Production): every student-facing
test-use aid is produced as a hand-inspectable SVG. No generative imagery is used
for any test-use aid. Output is reproducible: no randomness, no timestamps.

Each aid is described by an entry in REGISTRY. main() writes:
  - the SVG for each aid into its candidate/classroom folder
  - aids.json (the manifest that drives the compliance matrix + teacher catalog)

Rendering to PDF/PNG is handled separately by tools/render.sh (headless Chrome).
Linting is handled by tools/lint_aids.py.

US Letter canvas: viewBox 0 0 816 1056 (8.5x11in @96dpi). White background,
black/grayscale line art, generous margins. Student aids carry NO title, label,
branding, URL, or teacher note (spec section 4).
"""
import json
import math
import os

W, H = 816, 1056          # US Letter @ 96dpi
CX = W / 2
BLACK = "#000000"
GRAY = "#666666"

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


# ---------------------------------------------------------------------------
# SVG primitives (all deterministic)
# ---------------------------------------------------------------------------
def svg_open():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="8.5in" '
            f'height="11in" viewBox="0 0 {W} {H}">\n'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>\n')


def svg_close():
    return '</svg>\n'


def rect(x, y, w, h, sw=3, fill="none", rx=0):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'rx="{rx}" fill="{fill}" stroke="{BLACK}" stroke-width="{sw}"/>\n')


def line(x1, y1, x2, y2, sw=3, color=BLACK, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{sw}"{d}/>\n')


def circle(cx, cy, r, sw=3, fill="none", color=BLACK):
    return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" '
            f'stroke="{color}" stroke-width="{sw}"/>\n')


def dot(cx, cy, r, fill=BLACK):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}"/>\n'


def polygon(pts, sw=3, fill="none", dash=None):
    p = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<polygon points="{p}" fill="{fill}" stroke="{BLACK}" '
            f'stroke-width="{sw}"{d}/>\n')


def polyline(pts, sw=3, dash=None, color=BLACK):
    p = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<polyline points="{p}" fill="none" stroke="{color}" '
            f'stroke-width="{sw}"{d}/>\n')


def path(d, sw=3, fill="none", color=BLACK, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{sw}"{da}/>\n'


def ellipse(cx, cy, rx, ry, sw=3, fill="none"):
    return (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" '
            f'fill="{fill}" stroke="{BLACK}" stroke-width="{sw}"/>\n')


def text(x, y, s, size=40, weight="700", anchor="middle"):
    # Used ONLY where the aid_type permits characters (numbers, place-value
    # punctuation, a verified mnemonic, or single formula-triangle variables).
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{BLACK}">{s}</text>\n')


def wedge(cx, cy, r, a0, a1, sw=3):
    """Pie wedge outline from angle a0 to a1 (degrees), for fraction circles."""
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    large = 1 if (a1 - a0) % 360 > 180 else 0
    d = (f'M {cx:.1f} {cy:.1f} L {x0:.1f} {y0:.1f} '
         f'A {r:.1f} {r:.1f} 0 {large} 1 {x1:.1f} {y1:.1f} Z')
    return path(d, sw=sw)


# ---------------------------------------------------------------------------
# MATH aids
# ---------------------------------------------------------------------------
def math_number_chart_100():
    """math_number_chart: plain 1-100 hundreds chart. Numbers + grid only."""
    s = svg_open()
    n = 10
    cell = 66
    gx = CX - n * cell / 2
    gy = 150
    for r in range(n):
        for c in range(n):
            x, y = gx + c * cell, gy + r * cell
            s += rect(x, y, cell, cell, sw=2)
            val = r * n + c + 1
            s += text(x + cell / 2, y + cell / 2 + 12, str(val), size=30, weight="600")
    return s + svg_close()


def math_place_value_whole():
    """math_place_value_chart: blank whole-number cells with period commas."""
    s = svg_open()
    cells = 9  # 3 periods of 3
    cw = 74
    ch = 150
    total = cells * cw + 2 * 26  # two comma gaps
    x = CX - total / 2
    y = 440
    idx = 0
    for group in range(3):
        for c in range(3):
            s += rect(x, y, cw, ch, sw=3)
            x += cw
            idx += 1
        if group < 2:
            s += text(x + 13, y + ch - 6, ',', size=90)
            x += 26
    return s + svg_close()


def math_place_value_decimal():
    """math_place_value_chart: blank whole cells + decimal point + decimal cells."""
    s = svg_open()
    cw = 78
    ch = 150
    whole = 4
    dec = 3
    total = (whole + dec) * cw + 30
    x = CX - total / 2
    y = 440
    for c in range(whole):
        s += rect(x, y, cw, ch, sw=3)
        x += cw
    s += dot(x + 15, y + ch - 14, 9)  # decimal point
    x += 30
    for c in range(dec):
        s += rect(x, y, cw, ch, sw=3)
        x += cw
    return s + svg_close()


def math_fraction_bars():
    """math_fraction_model: unlabeled fraction wall (bars partitioned only)."""
    s = svg_open()
    parts = [1, 2, 3, 4, 5, 6, 8, 10, 12]
    bw = 560
    bh = 62
    x = CX - bw / 2
    y = 150
    gap = 14
    for p in parts:
        s += rect(x, y, bw, bh, sw=3)
        for i in range(1, p):
            xx = x + bw * i / p
            s += line(xx, y, xx, y + bh, sw=2)
        y += bh + gap
    return s + svg_close()


def math_fraction_circles():
    """math_fraction_model: unlabeled circles partitioned into equal parts."""
    s = svg_open()
    parts = [1, 2, 3, 4, 5, 6, 8, 9]
    r = 92
    cols = 2
    xs = [CX - 200, CX + 200]
    y = 210
    row_gap = 210
    for i, p in enumerate(parts):
        cx = xs[i % cols]
        cy = y + (i // cols) * row_gap
        s += circle(cx, cy, r, sw=3)
        if p == 1:
            pass
        else:
            for k in range(p):
                a = -90 + 360 * k / p
                s += line(cx, cy,
                          cx + r * math.cos(math.radians(a)),
                          cy + r * math.sin(math.radians(a)), sw=2)
    return s + svg_close()


def math_geometry_2d_basic():
    """math_geometry_2d: basic unlabeled plane figures (grades 3-5)."""
    s = svg_open()
    # row 1: equilateral triangle, square, rectangle
    s += polygon([(150, 300), (250, 130), (350, 300)])
    s += rect(430, 150, 150, 150)
    s += rect(620, 175, 150, 100)
    # row 2: circle, pentagon, hexagon
    s += circle(230, 560, 90)
    s += polygon(_regular_polygon(500, 560, 95, 5, -90))
    s += polygon(_regular_polygon(690, 560, 95, 6, -90))
    # row 3: right triangle, parallelogram, trapezoid
    s += polygon([(150, 920), (150, 760), (320, 920)])
    s += polygon([(430, 920), (490, 770), (660, 770), (600, 920)])
    s += polygon([(700, 920), (740, 770), (800, 770), (816 - 6, 920)])
    return s + svg_close()


def math_geometry_2d_full():
    """math_geometry_2d: expanded plane figures (grades 5-7)."""
    s = svg_open()
    figs = []
    # triangles: equilateral, right, obtuse, isosceles
    figs.append([(0, 90), (100, -70), (200, 90)])          # equilateral-ish
    figs.append([(0, 90), (0, -70), (170, 90)])            # right
    figs.append([(0, 90), (60, -70), (210, 90)])           # scalene/obtuse
    figs.append([(0, 90), (100, -80), (200, 90)])          # isosceles
    # quads: square, rectangle, parallelogram, rhombus, trapezoid, kite
    figs.append([(0, 0), (150, 0), (150, 150), (0, 150)])  # square
    figs.append([(0, 0), (180, 0), (180, 110), (0, 110)])  # rectangle
    figs.append([(30, 0), (200, 0), (170, 130), (0, 130)]) # parallelogram
    figs.append([(90, 0), (180, 90), (90, 180), (0, 90)])  # rhombus
    figs.append([(40, 0), (150, 0), (190, 120), (0, 120)]) # trapezoid
    figs.append([(90, 0), (180, 80), (90, 200), (0, 80)])  # kite
    # polygons: pentagon, hexagon, octagon, circle placeholder handled separately
    positions = [(120, 170), (330, 170), (540, 170), (720, 170),
                 (120, 400), (340, 400), (560, 400), (760, 400),
                 (150, 640), (380, 640)]
    for fig, (ox, oy) in zip(figs, positions):
        pts = [(ox + x * 0.9, oy + y * 0.9) for x, y in fig]
        s += polygon(pts, sw=3)
    # pentagon, hexagon, octagon, circle on bottom row
    s += polygon(_regular_polygon(150, 900, 78, 5, -90))
    s += polygon(_regular_polygon(340, 900, 78, 6, -90))
    s += polygon(_regular_polygon(540, 900, 78, 8, -90 + 22.5))
    s += circle(730, 900, 80)
    return s + svg_close()


def math_geometry_3d():
    """math_geometry_3d: unlabeled solid figures. Hidden edges dashed."""
    s = svg_open()
    # Cube
    ox, oy, a, d = 130, 200, 130, 45
    s += _cube(ox, oy, a, d)
    # Rectangular prism
    s += _box(360, 200, 170, 110, 45)
    # Triangular prism
    s += _tri_prism(620, 200, 150, 120, 45)
    # Cylinder
    s += _cylinder(180, 560, 90, 170)
    # Cone
    s += _cone(440, 560, 90, 190)
    # Sphere
    s += _sphere(680, 620, 95)
    # Square pyramid
    s += _sq_pyramid(300, 940, 190, 170, 40)
    # Rectangular pyramid
    s += _sq_pyramid(600, 940, 210, 150, 55)
    return s + svg_close()


def math_mnemonic_pemdas():
    """mnemonic: verified acronym only, no decoded words/symbols."""
    s = svg_open()
    s += text(CX, 520, 'PEMDAS', size=150, weight="800")
    s += rect(CX - 300, 400, 600, 170, sw=4)
    return s + svg_close()


def blank_venn():
    s = svg_open()
    s += circle(CX - 120, H / 2, 230, sw=4)
    s += circle(CX + 120, H / 2, 230, sw=4)
    return s + svg_close()


def blank_tchart():
    s = svg_open()
    m = 90
    s += line(m, 170, W - m, 170, sw=4)          # top bar
    s += line(CX, 170, CX, H - 150, sw=4)        # divider
    s += rect(m, 170, W - 2 * m, H - 320, sw=4)  # outer box
    return s + svg_close()


def blank_frayer():
    s = svg_open()
    m = 100
    x, y, w, h = m, 170, W - 2 * m, H - 320
    s += rect(x, y, w, h, sw=4)
    s += line(x + w / 2, y, x + w / 2, y + h, sw=3)
    s += line(x, y + h / 2, x + w, y + h / 2, sw=3)
    s += ellipse(x + w / 2, y + h / 2, 90, 60, sw=4)  # center oval
    return s + svg_close()


def blank_grid():
    s = svg_open()
    m = 90
    x, y, w, h = m, 160, W - 2 * m, H - 300
    cols, rows = 4, 6
    s += rect(x, y, w, h, sw=4)
    for c in range(1, cols):
        s += line(x + w * c / cols, y, x + w * c / cols, y + h, sw=2)
    for r in range(1, rows):
        s += line(x, y + h * r / rows, x + w, y + h * r / rows, sw=2)
    return s + svg_close()


# ---------- 3D helpers ----------
def _cube(x, y, a, d):
    s = ''
    fr = [(x, y), (x + a, y), (x + a, y + a), (x, y + a)]
    bk = [(px + d, py - d) for px, py in fr]
    s += polygon(fr)
    s += line(*fr[0], *bk[0], dash="8 6", sw=2)  # hidden corner via dashed
    # visible back edges
    s += line(*fr[1], *bk[1])
    s += line(*fr[2], *bk[2])
    s += line(*fr[3], *bk[3], dash="8 6", sw=2)
    s += polyline([bk[3], bk[0], bk[1]], dash="8 6", sw=2)
    s += polyline([bk[1], bk[2], bk[3]])
    return s


def _box(x, y, w, h, d):
    s = ''
    fr = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    bk = [(px + d, py - d) for px, py in fr]
    s += polygon(fr)
    s += line(*fr[1], *bk[1]); s += line(*fr[2], *bk[2])
    s += polyline([bk[1], bk[2]])
    s += line(*fr[0], *bk[0], dash="8 6", sw=2)
    s += line(*fr[3], *bk[3], dash="8 6", sw=2)
    s += polyline([bk[3], bk[0], bk[1]], dash="8 6", sw=2)
    return s


def _tri_prism(x, y, w, h, d):
    s = ''
    fr = [(x, y + h), (x + w / 2, y), (x + w, y + h)]
    bk = [(px + d, py - d) for px, py in fr]
    s += polygon(fr)
    for a, b in zip(fr, bk):
        s += line(*a, *b)
    s += polyline([bk[0], bk[1], bk[2]])
    s += line(*bk[0], *bk[2], dash="8 6", sw=2)
    return s


def _cylinder(cx, cy, rx, h):
    s = ''
    ry = rx * 0.32
    s += ellipse(cx, cy - h / 2, rx, ry)
    s += line(cx - rx, cy - h / 2, cx - rx, cy + h / 2)
    s += line(cx + rx, cy - h / 2, cx + rx, cy + h / 2)
    s += path(f'M {cx-rx:.1f} {cy+h/2:.1f} A {rx:.1f} {ry:.1f} 0 0 0 {cx+rx:.1f} {cy+h/2:.1f}')
    s += path(f'M {cx-rx:.1f} {cy+h/2:.1f} A {rx:.1f} {ry:.1f} 0 0 1 {cx+rx:.1f} {cy+h/2:.1f}',
              dash="8 6", sw=2)
    return s


def _cone(cx, cy, rx, h):
    s = ''
    ry = rx * 0.32
    apex = (cx, cy - h / 2)
    s += line(*apex, cx - rx, cy + h / 2)
    s += line(*apex, cx + rx, cy + h / 2)
    s += path(f'M {cx-rx:.1f} {cy+h/2:.1f} A {rx:.1f} {ry:.1f} 0 0 0 {cx+rx:.1f} {cy+h/2:.1f}')
    s += path(f'M {cx-rx:.1f} {cy+h/2:.1f} A {rx:.1f} {ry:.1f} 0 0 1 {cx+rx:.1f} {cy+h/2:.1f}',
              dash="8 6", sw=2)
    return s


def _sphere(cx, cy, r):
    s = circle(cx, cy, r)
    s += path(f'M {cx-r:.1f} {cy:.1f} A {r:.1f} {r*0.30:.1f} 0 0 0 {cx+r:.1f} {cy:.1f}')
    s += path(f'M {cx-r:.1f} {cy:.1f} A {r:.1f} {r*0.30:.1f} 0 0 1 {cx+r:.1f} {cy:.1f}',
              dash="8 6", sw=2)
    return s


def _sq_pyramid(cx, base_y, w, h, d):
    s = ''
    bl = (cx - w / 2, base_y)
    br = (cx + w / 2, base_y)
    bbl = (bl[0] + d, bl[1] - d)
    bbr = (br[0] + d, br[1] - d)
    apex = (cx + d / 2, base_y - h)
    s += line(*bl, *br)
    s += line(*bl, *apex)
    s += line(*br, *apex)
    s += line(*br, *bbr); s += line(*bbr, *apex)
    s += line(*bl, *bbl, dash="8 6", sw=2)
    s += line(*bbl, *bbr, dash="8 6", sw=2)
    s += line(*bbl, *apex, dash="8 6", sw=2)
    return s


def _regular_polygon(cx, cy, r, n, start_deg):
    return [(cx + r * math.cos(math.radians(start_deg + 360 * i / n)),
             cy + r * math.sin(math.radians(start_deg + 360 * i / n))) for i in range(n)]


# ---------------------------------------------------------------------------
# SCIENCE aids (science_graphic: unlabeled grayscale line art, no arrows/text)
# ---------------------------------------------------------------------------
def _particle_box(x, y, size, positions, r=13):
    s = rect(x, y, size, size, sw=3)
    for px, py in positions:
        s += dot(x + px, y + py, r)
    return s


def sci_states_of_matter():
    s = svg_open()
    size = 200
    y = 430
    xs = [70, 308, 546]
    # solid: ordered packed grid
    solid = [(35 + c * 43, 35 + rr * 43) for rr in range(4) for c in range(4)]
    # liquid: looser, offset
    liquid = [(30 + c * 52 + (rr % 2) * 20, 40 + rr * 50) for rr in range(4) for c in range(3)]
    # gas: sparse
    gas = [(45, 55), (150, 40), (95, 120), (170, 150), (55, 165), (120, 180)]
    s += _particle_box(xs[0], y, size, solid, r=12)
    s += _particle_box(xs[1], y, size, liquid, r=12)
    s += _particle_box(xs[2], y, size, gas, r=12)
    return s + svg_close()


def sci_element_compound_mixture():
    s = svg_open()
    size = 200
    y = 430
    xs = [70, 308, 546]
    # element: identical single atoms
    el = [(35 + c * 43, 35 + rr * 43) for rr in range(4) for c in range(4)]
    s += _particle_box(xs[0], y, size, [], r=0)
    s += rect(xs[0], y, size, size, sw=3)
    for px, py in el:
        s += dot(xs[0] + px, y + py, 12)
    # compound: identical two-atom molecules (big+small bonded)
    s += rect(xs[1], y, size, size, sw=3)
    mol = [(45, 45), (110, 55), (60, 120), (130, 130), (40, 175)]
    for px, py in mol:
        s += dot(xs[1] + px, y + py, 14)
        s += dot(xs[1] + px + 24, y + py + 8, 9)
        s += line(xs[1] + px, y + py, xs[1] + px + 24, y + py + 8, sw=3)
    # mixture: two kinds intermixed, unbonded
    s += rect(xs[2], y, size, size, sw=3)
    big = [(40, 50), (150, 45), (95, 110), (55, 165), (160, 160)]
    small = [(95, 45), (45, 110), (150, 110), (110, 165), (30, 45)]
    for px, py in big:
        s += dot(xs[2] + px, y + py, 15)
    for px, py in small:
        s += circle(xs[2] + px, y + py, 9, sw=3)
    return s + svg_close()


def sci_mixtures_simple():
    """grade 5: two kinds of particles mixed but keeping their identity."""
    s = svg_open()
    size = 360
    x = CX - size / 2
    y = 350
    s += rect(x, y, size, size, sw=3)
    squares = [(50, 60), (150, 90), (250, 55), (300, 160), (70, 200),
               (180, 210), (90, 300), (250, 290), (300, 250)]
    circs = [(110, 55), (210, 130), (60, 130), (150, 160), (250, 200),
             (40, 270), (170, 300), (300, 90), (210, 290)]
    for px, py in squares:
        s += rect(x + px - 13, y + py - 13, 26, 26, sw=3)
    for px, py in circs:
        s += dot(x + px, y + py, 14)
    return s + svg_close()


def sci_atomic_structure():
    """Generic Bohr model: nucleus cluster + electron shells. No numbers."""
    s = svg_open()
    cx, cy = CX, H / 2
    s += circle(cx, cy, 120, sw=2)   # inner shell
    s += circle(cx, cy, 210, sw=2)   # outer shell
    # nucleus cluster
    for dx, dy in [(-14, -8), (12, -10), (0, 12), (-10, 14), (16, 8), (2, -18)]:
        s += dot(cx + dx, cy + dy, 15)
    # electrons on shells
    for a in (0, 180):
        s += dot(cx + 120 * math.cos(math.radians(a)), cy + 120 * math.sin(math.radians(a)), 12)
    for a in (45, 135, 225, 315):
        s += dot(cx + 210 * math.cos(math.radians(a)), cy + 210 * math.sin(math.radians(a)), 12)
    return s + svg_close()


def sci_moon_phases():
    """8 phase disks with illumination shading (depiction, not a color label)."""
    s = svg_open()
    r = 78
    cx, cy = CX, H / 2
    ring = 300
    for i in range(8):
        a = -90 + 360 * i / 8
        px = cx + ring * math.cos(math.radians(a))
        py = cy + ring * math.sin(math.radians(a))
        s += _moon(px, py, r, i / 8.0)
    return s + svg_close()


def _moon(cx, cy, r, phase):
    """phase 0=new(dark) .. 0.5=full(light) .. ->new. Shade the dark part."""
    s = circle(cx, cy, r, sw=3)
    # illuminated fraction f (0..1) of a simple waxing/waning model
    # draw dark region as filled path
    if abs(phase - 0.0) < 1e-6 or abs(phase - 1.0) < 1e-6:
        s += circle(cx, cy, r, sw=0, fill=BLACK)                     # new: fully dark
        s += circle(cx, cy, r, sw=3)
        return s
    if abs(phase - 0.5) < 1e-6:
        return s                                                     # full: fully light
    # terminator ellipse width
    k = math.cos(2 * math.pi * phase)          # -1..1
    waxing = phase < 0.5
    # dark side path: left half if waxing, right half if waning, minus lit crescent
    rx = abs(k) * r
    if waxing:
        # dark on left; lit grows from right
        d = (f'M {cx:.1f} {cy-r:.1f} '
             f'A {r:.1f} {r:.1f} 0 0 0 {cx:.1f} {cy+r:.1f} '
             f'A {rx:.1f} {r:.1f} 0 0 {0 if k>0 else 1} {cx:.1f} {cy-r:.1f} Z')
    else:
        d = (f'M {cx:.1f} {cy-r:.1f} '
             f'A {r:.1f} {r:.1f} 0 0 1 {cx:.1f} {cy+r:.1f} '
             f'A {rx:.1f} {r:.1f} 0 0 {1 if k>0 else 0} {cx:.1f} {cy-r:.1f} Z')
    s += path(d, sw=0, fill=BLACK)
    return s


def sci_plate_boundaries():
    """Three block cross-sections; no arrows, no labels."""
    s = svg_open()
    x = 120
    w = 576
    h = 130
    # divergent: gap/ridge in the middle
    y = 200
    s += polygon([(x, y + h), (x, y + 40), (x + w / 2 - 40, y + 40),
                  (x + w / 2, y), (x + w / 2 + 40, y + 40), (x + w, y + 40),
                  (x + w, y + h)])
    s += line(x + w / 2, y, x + w / 2, y + h, dash="8 6", sw=2)
    # convergent: one block wedging under the other
    y = 470
    s += polygon([(x, y + 40), (x + w / 2 + 30, y + 40), (x + w, y + 110),
                  (x + w, y + h), (x, y + h)])
    s += line(x + w / 2 + 30, y + 40, x, y + h, dash="8 6", sw=2)
    s += polygon([(x, y + 40), (x + w * 0.62, y + 40), (x + w * 0.42, y + h),
                  (x, y + h)], sw=3)
    # transform: vertical offset break
    y = 740
    s += rect(x, y, w / 2 - 10, h, sw=3)
    s += rect(x + w / 2 + 10, y - 26, w / 2 - 10, h, sw=3)
    return s + svg_close()


def sci_cell_animal():
    s = svg_open()
    cx, cy = CX, H / 2
    # membrane (irregular rounded blob)
    s += path(f'M {cx-260} {cy} '
              f'C {cx-260} {cy-170}, {cx-120} {cy-220}, {cx} {cy-215} '
              f'C {cx+150} {cy-210}, {cx+270} {cy-140}, {cx+265} {cy} '
              f'C {cx+260} {cy+160}, {cx+130} {cy+220}, {cx} {cy+215} '
              f'C {cx-140} {cy+210}, {cx-260} {cy+150}, {cx-260} {cy} Z', sw=4)
    # nucleus + nucleolus
    s += circle(cx - 30, cy - 20, 70, sw=3)
    s += dot(cx - 30, cy - 20, 20)
    # mitochondria (ovals with inner crease)
    for ex, ey, rot in [(cx + 120, cy - 90, 0), (cx - 150, cy + 90, 0), (cx + 100, cy + 110, 0)]:
        s += ellipse(ex, ey, 52, 26, sw=3)
        s += polyline([(ex - 40, ey), (ex - 20, ey - 10), (ex, ey + 10),
                       (ex + 20, ey - 10), (ex + 40, ey)], sw=2)
    # ER (wavy) and ribosome dots
    s += polyline([(cx + 60, cy - 150), (cx + 90, cy - 120), (cx + 60, cy - 90),
                   (cx + 90, cy - 60), (cx + 60, cy - 30)], sw=2)
    for dx, dy in [(-120, -120), (-160, 20), (60, 160), (150, 40)]:
        s += dot(cx + dx, cy + dy, 6)
    # a few vesicles
    s += circle(cx - 190, cy - 40, 24, sw=3)
    s += circle(cx + 180, cy - 10, 20, sw=3)
    return s + svg_close()


def sci_cell_plant():
    s = svg_open()
    cx, cy = CX, H / 2
    x, y, w, h = cx - 280, cy - 220, 560, 440
    s += rect(x, y, w, h, sw=5, rx=18)                 # cell wall
    s += rect(x + 16, y + 16, w - 32, h - 32, sw=2, rx=14)  # membrane
    # large central vacuole
    s += rect(cx - 150, cy - 130, 300, 260, sw=3, rx=30)
    # nucleus
    s += circle(x + 90, y + 100, 55, sw=3)
    s += dot(x + 90, y + 100, 16)
    # chloroplasts (ovals) around the vacuole
    for ex, ey in [(x + 70, cy + 120), (cx + 210, y + 110), (cx + 210, cy + 120),
                   (cx - 10, y + 60), (cx, cy + 180)]:
        s += ellipse(ex, ey, 34, 18, sw=3)
    return s + svg_close()


def sci_plant_parts():
    s = svg_open()
    cx = CX
    ground = 720
    s += line(180, ground, 636, ground, sw=3)          # soil line
    # roots
    s += polyline([(cx, ground), (cx - 60, ground + 120)], sw=3)
    s += polyline([(cx, ground), (cx + 70, ground + 140)], sw=3)
    s += polyline([(cx, ground), (cx - 10, ground + 160)], sw=3)
    s += polyline([(cx - 30, ground + 60), (cx - 90, ground + 110)], sw=2)
    s += polyline([(cx + 30, ground + 70), (cx + 100, ground + 90)], sw=2)
    # stem
    s += line(cx, ground, cx, 360, sw=4)
    # leaves
    s += ellipse(cx - 90, 520, 70, 34, sw=3)
    s += ellipse(cx + 90, 470, 70, 34, sw=3)
    s += line(cx, 520, cx - 150, 520, sw=2)
    s += line(cx, 470, cx + 150, 470, sw=2)
    # flower
    s += circle(cx, 320, 34, sw=3)
    for a in range(0, 360, 60):
        px = cx + 66 * math.cos(math.radians(a))
        py = 320 + 66 * math.sin(math.radians(a))
        s += ellipse(px, py, 30, 20, sw=3)
    return s + svg_close()


def sci_wave_transverse():
    s = svg_open()
    y0 = H / 2
    x0, x1 = 90, W - 90
    s += line(x0, y0, x1, y0, sw=1, color=GRAY)   # rest axis (light)
    amp = 150
    pts = []
    n = 400
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        y = y0 - amp * math.sin(2 * math.pi * 2.5 * i / n)
        pts.append((x, y))
    s += polyline(pts, sw=4)
    return s + svg_close()


def sci_circuit_simple():
    """Pictorial closed loop: battery + bulb + wires. No schematic symbols/text."""
    s = svg_open()
    x, y, w, h = 170, 360, 476, 300
    # wire loop
    s += rect(x, y, w, h, sw=4, fill="none")
    # battery (cylinder) on bottom side
    bx, by = CX - 70, y + h - 20
    s += rect(bx, by - 40, 140, 40, sw=3, rx=8, fill="#ffffff")
    s += rect(bx + 140, by - 30, 12, 20, sw=3, fill="#ffffff")  # terminal nub
    # cover wire behind battery
    s += rect(bx, y + h - 4, 152, 8, sw=0, fill="#ffffff")
    # bulb on top side
    bcx, bcy = CX, y
    s += rect(bcx - 22, y - 6, 44, 26, sw=3, fill="#ffffff")   # base
    s += circle(bcx, bcy - 46, 40, sw=3, fill="#ffffff")       # glass
    s += polyline([(bcx - 14, bcy - 40), (bcx - 4, bcy - 60),
                   (bcx + 4, bcy - 34), (bcx + 14, bcy - 60)], sw=2)  # filament
    s += rect(bcx - 40, y - 4, 80, 8, sw=0, fill="#ffffff")    # cover wire behind base
    return s + svg_close()


# ---------------------------------------------------------------------------
# SCIENCE formula triangles (science_formula_triangle): variables only
# ---------------------------------------------------------------------------
def _formula_triangle(top, left, right):
    s = svg_open()
    cx, cy = CX, H / 2 + 20
    size = 460
    ax = (cx, cy - size * 0.62)
    bx = (cx - size / 2, cy + size * 0.38)
    cxr = (cx + size / 2, cy + size * 0.38)
    s += polygon([ax, bx, cxr], sw=5)
    # horizontal divider between top and bottom two
    midy = cy + size * 0.02
    lx = cx - (size / 2) * (1 - 0.62 - (-0.38)) / 1  # approximate; draw across triangle
    # compute intersection of horizontal line with the two slanted edges at midy
    def x_on_edge(p1, p2, y):
        return p1[0] + (p2[0] - p1[0]) * (y - p1[1]) / (p2[1] - p1[1])
    xl = x_on_edge(ax, bx, midy)
    xr = x_on_edge(ax, cxr, midy)
    s += line(xl, midy, xr, midy, sw=5)
    # vertical divider in the bottom half
    s += line(cx, midy, cx, cy + size * 0.38, sw=5)
    # variables (single letters only)
    s += text(cx, ax[1] + (midy - ax[1]) * 0.62 + 18, top, size=90)
    s += text(cx - size * 0.22, cy + size * 0.30, left, size=90)
    s += text(cx + size * 0.22, cy + size * 0.30, right, size=90)
    return s + svg_close()


def ft_density():      # D = m / V  -> m over D,V
    return _formula_triangle('m', 'D', 'V')


def ft_avg_speed():    # s = d / t  -> d over s,t
    return _formula_triangle('d', 's', 't')


def ft_net_force():    # F = m a    -> F over m,a
    return _formula_triangle('F', 'm', 'a')


def ft_work():         # W = F d    -> W over F,d
    return _formula_triangle('W', 'F', 'd')


# ---------------------------------------------------------------------------
# REGISTRY
# ---------------------------------------------------------------------------
REGISTRY = [
    # ---- MATH ----
    dict(fn=math_number_chart_100, file="math-g3_5-number-chart-100.svg",
         folder="candidates/math/grade-3", aid_type="math_number_chart",
         subject="Math", grade="3-5", concept="Hundreds chart (1-100)",
         teks="counting, patterns, number relationships", status="CANDIDATE",
         source="Elementary math cue cards (number/place value)",
         cue="Recall counting/skip-count patterns", notes="Plain chart; no highlighting/shading."),
    dict(fn=math_place_value_whole, file="math-g3_5-place-value-whole-blank.svg",
         folder="candidates/math/grade-4", aid_type="math_place_value_chart",
         subject="Math", grade="3-5", concept="Blank whole-number place-value chart",
         teks="place value to millions", status="CANDIDATE",
         source="Elementary math 'Place Value' cue card",
         cue="Align digits by place", notes="Blank cells + period commas only; no words/examples."),
    dict(fn=math_place_value_decimal, file="math-g5-place-value-decimal-blank.svg",
         folder="candidates/math/grade-5", aid_type="math_place_value_chart",
         subject="Math", grade="5", concept="Blank decimal place-value chart",
         teks="decimals to thousandths", status="CANDIDATE",
         source="Elementary math 'Place Value' cue card",
         cue="Align digits around the decimal point", notes="Blank cells + decimal point only."),
    dict(fn=math_fraction_bars, file="math-g3_5-fraction-bars-blank.svg",
         folder="candidates/math/grade-3", aid_type="math_fraction_model",
         subject="Math", grade="3-5", concept="Unlabeled fraction bars (wall)",
         teks="fractions, equivalence", status="CANDIDATE",
         source="Elementary math 'Fractions' cue card",
         cue="Compare partition sizes", notes="Partitioning only; no numbers/labels/equivalency."),
    dict(fn=math_fraction_circles, file="math-g3_5-fraction-circles-blank.svg",
         folder="candidates/math/grade-3", aid_type="math_fraction_model",
         subject="Math", grade="3-5", concept="Unlabeled fraction circles",
         teks="fractions, equivalence", status="CANDIDATE",
         source="Elementary math 'Fractions' cue card",
         cue="See equal partitions of a whole", notes="Partitioning only; no numbers/labels."),
    dict(fn=math_geometry_2d_basic, file="math-g3-2d-figures.svg",
         folder="candidates/math/grade-3", aid_type="math_geometry_2d",
         subject="Math", grade="3-5", concept="Basic 2-D geometric figures",
         teks="classify 2-D figures", status="CANDIDATE",
         source="Math geometry cue material",
         cue="Recall figure shapes", notes="Outlines only; no names/measures. Keep 2-D and 3-D separate (§6D)."),
    dict(fn=math_geometry_2d_full, file="math-g5_7-2d-figures.svg",
         folder="candidates/math/grade-5", aid_type="math_geometry_2d",
         subject="Math", grade="5-7", concept="Expanded 2-D geometric figures",
         teks="classify triangles/quadrilaterals/polygons", status="CANDIDATE",
         source="Math geometry cue material",
         cue="Recall figure shapes", notes="Outlines only; no names/measures/angles."),
    dict(fn=math_geometry_3d, file="math-g6_8-3d-figures.svg",
         folder="candidates/math/grade-6", aid_type="math_geometry_3d",
         subject="Math", grade="6-8", concept="3-D geometric solids",
         teks="3-D figures, nets/volume context", status="CANDIDATE",
         source="Math geometry cue material",
         cue="Recall solid shapes", notes="Solids only (no nets); no labels/measures. Separate from 2-D (§6D)."),
    dict(fn=math_mnemonic_pemdas, file="math-g6-mnemonic-pemdas.svg",
         folder="candidates/math/mnemonics", aid_type="mnemonic",
         subject="Math", grade="5-8", concept="Order-of-operations acronym",
         teks="order of operations", status="NEEDS TEA/LOCAL VERIFICATION",
         source="Order of operations instruction",
         cue="Recall the operation order", notes="Acronym letters only; no decoded words/symbols (§5). Local review: confirm acronym mnemonics are accepted."),
    dict(fn=blank_venn, file="math-venn-blank.svg",
         folder="candidates/math/blank-organizers", aid_type="blank_graphic_organizer",
         subject="Math/Science", grade="3-8", concept="Blank Venn diagram",
         teks="compare/contrast, sort", status="CANDIDATE",
         source="Classroom graphic organizers",
         cue="Sort into overlapping sets", notes="Genuinely blank; no words/labels/numbers."),
    dict(fn=blank_tchart, file="math-tchart-blank.svg",
         folder="candidates/math/blank-organizers", aid_type="blank_graphic_organizer",
         subject="Math/Science", grade="3-8", concept="Blank T-chart",
         teks="organize pairs/relationships", status="CANDIDATE",
         source="Classroom graphic organizers",
         cue="Two-column structure", notes="Genuinely blank; no words/labels/numbers."),
    dict(fn=blank_frayer, file="math-frayer-blank.svg",
         folder="candidates/math/blank-organizers", aid_type="blank_graphic_organizer",
         subject="Math/Science", grade="3-8", concept="Blank four-quadrant organizer",
         teks="organize a concept", status="CANDIDATE",
         source="Classroom graphic organizers",
         cue="Four-part structure", notes="Genuinely blank; no words/labels/numbers."),
    dict(fn=blank_grid, file="math-grid-blank.svg",
         folder="candidates/math/blank-organizers", aid_type="blank_graphic_organizer",
         subject="Math/Science", grade="3-8", concept="Blank table grid",
         teks="organize data", status="CANDIDATE",
         source="Classroom graphic organizers",
         cue="Rows/columns structure", notes="Genuinely blank; no words/labels/numbers."),

    # ---- SCIENCE GRAPHICS ----
    dict(fn=sci_states_of_matter, file="science-g5_8-states-of-matter-unlabeled.svg",
         folder="candidates/science/grade-8", aid_type="science_graphic",
         subject="Science", grade="5-8", concept="States of matter (particle spacing)",
         teks="particle model of solids/liquids/gases", status="CANDIDATE",
         source="Science 'States of Matter' cue card",
         cue="Recall particle spacing/arrangement", notes="Grayscale particles; no labels/arrows/color-coding."),
    dict(fn=sci_element_compound_mixture, file="science-g8-element-compound-mixture-unlabeled.svg",
         folder="candidates/science/grade-8", aid_type="science_graphic",
         subject="Science", grade="8", concept="Element / compound / mixture particles",
         teks="classification of matter", status="CANDIDATE",
         source="Science 'Elements, Compounds & Mixtures' cue card",
         cue="Distinguish particle groupings", notes="Grayscale particles; no labels/arrows/color."),
    dict(fn=sci_mixtures_simple, file="science-g5-mixture-unlabeled.svg",
         folder="candidates/science/grade-5", aid_type="science_graphic",
         subject="Science", grade="5", concept="Mixture (two particle types)",
         teks="mixtures keep their properties", status="CANDIDATE",
         source="Elementary science 'Mixtures & Solutions' cue card",
         cue="Two materials mixed, not bonded", notes="Two neutral shapes; no labels/color."),
    dict(fn=sci_atomic_structure, file="science-g8-atomic-structure-unlabeled.svg",
         folder="candidates/science/grade-8", aid_type="science_graphic",
         subject="Science", grade="8", concept="Atomic structure (generic Bohr model)",
         teks="atomic structure", status="CANDIDATE",
         source="Science 'Atomic Structure' cue card",
         cue="Nucleus + electron shells layout", notes="Generic (no element implied); no numbers/labels."),
    dict(fn=sci_moon_phases, file="science-g5_8-moon-phases-unlabeled.svg",
         folder="candidates/science/grade-8", aid_type="science_graphic",
         subject="Science", grade="5-8", concept="Moon phases (illumination shapes)",
         teks="lunar cycle", status="NEEDS TEA/LOCAL VERIFICATION",
         source="Science 'Phases of the Moon' cue card",
         cue="Recall the illuminated-shape sequence", notes="Shading depicts illumination (not a color label). Local review: confirm grayscale illumination is acceptable; no numbers/arrows/labels."),
    dict(fn=sci_plate_boundaries, file="science-g8-plate-boundaries-unlabeled.svg",
         folder="candidates/science/grade-8", aid_type="science_graphic",
         subject="Science", grade="8", concept="Plate-boundary cross-sections",
         teks="plate tectonics", status="NEEDS TEA/LOCAL VERIFICATION",
         source="Science 'Plate Boundaries' cue card",
         cue="Recall boundary geometry", notes="No arrows/labels. Local review: confirm the geometry is unambiguous without motion arrows; otherwise classroom-only."),
    dict(fn=sci_cell_animal, file="science-g8-bio-animal-cell-unlabeled.svg",
         folder="candidates/science/grade-8", aid_type="science_graphic",
         subject="Science", grade="8/Biology", concept="Animal cell (unlabeled organelles)",
         teks="cell structure", status="CANDIDATE",
         source="Science 'Cell Structures' cue card",
         cue="Recall organelle shapes/locations", notes="Line art; no labels/color/arrows."),
    dict(fn=sci_cell_plant, file="science-g8-bio-plant-cell-unlabeled.svg",
         folder="candidates/science/grade-8", aid_type="science_graphic",
         subject="Science", grade="8/Biology", concept="Plant cell (unlabeled organelles)",
         teks="cell structure", status="CANDIDATE",
         source="Science 'Cell Structures' cue card",
         cue="Recall wall/vacuole/organelle layout", notes="Line art; no labels/color/arrows."),
    dict(fn=sci_plant_parts, file="science-g5-plant-parts-unlabeled.svg",
         folder="candidates/science/grade-5", aid_type="science_graphic",
         subject="Science", grade="3-5", concept="Plant parts (unlabeled)",
         teks="plant structures/functions", status="CANDIDATE",
         source="Elementary science 'Plant Parts & Functions' cue card",
         cue="Recall roots/stem/leaves/flower", notes="Line art; no labels/color/arrows."),
    dict(fn=sci_wave_transverse, file="science-g8-transverse-wave-unlabeled.svg",
         folder="candidates/science/grade-8", aid_type="science_graphic",
         subject="Science", grade="8", concept="Transverse wave (unlabeled)",
         teks="wave properties", status="CANDIDATE",
         source="Science 'Wave Properties' cue card",
         cue="Recall amplitude/wavelength shape", notes="Curve + faint rest axis; no labels/measures/arrows."),
    dict(fn=sci_circuit_simple, file="science-g5-simple-circuit-unlabeled.svg",
         folder="candidates/science/grade-5", aid_type="science_graphic",
         subject="Science", grade="4-5", concept="Simple closed circuit (pictorial)",
         teks="electricity, closed circuit", status="NEEDS TEA/LOCAL VERIFICATION",
         source="Elementary science 'Electricity & Circuits' cue card",
         cue="Recall a complete loop", notes="Pictorial (not schematic symbols); no text. Local review: confirm pictorial circuit is acceptable; otherwise classroom-only."),

    # ---- SCIENCE FORMULA TRIANGLES (G8 science ref sheet only) ----
    dict(fn=ft_density, file="science-g8-formula-triangle-density.svg",
         folder="candidates/science/grade-8", aid_type="science_formula_triangle",
         subject="Science", grade="8", concept="Density relationship (variables only)",
         teks="density = mass/volume", status="CANDIDATE",
         source="Science 'Density' formula-triangle cue card",
         cue="Recall the m/D/V relationship", notes="On G8 science reference sheet. Variables only; no name/units/operators."),
    dict(fn=ft_avg_speed, file="science-g8-formula-triangle-average-speed.svg",
         folder="candidates/science/grade-8", aid_type="science_formula_triangle",
         subject="Science", grade="8", concept="Average speed relationship (variables only)",
         teks="speed = distance/time", status="CANDIDATE",
         source="Science 'Average Speed' formula-triangle cue card",
         cue="Recall the d/s/t relationship", notes="On G8 science reference sheet. Variables only."),
    dict(fn=ft_net_force, file="science-g8-formula-triangle-net-force.svg",
         folder="candidates/science/grade-8", aid_type="science_formula_triangle",
         subject="Science", grade="8", concept="Net force relationship (variables only)",
         teks="F = m x a", status="CANDIDATE",
         source="Science 'Force' formula-triangle cue card",
         cue="Recall the F/m/a relationship", notes="On G8 science reference sheet. Variables only."),
    dict(fn=ft_work, file="science-g8-formula-triangle-work.svg",
         folder="candidates/science/grade-8", aid_type="science_formula_triangle",
         subject="Science", grade="8", concept="Work relationship (variables only)",
         teks="W = F x d", status="CANDIDATE",
         source="Science 'Work' formula-triangle cue card",
         cue="Recall the W/F/d relationship", notes="On G8 science reference sheet. Variables only."),
]

# Classroom-only determinations (documented, NOT built as candidates).
CLASSROOM_ONLY = [
    dict(source="Science formula triangle: Weight (W=mg)", subject="Science", reason="Not on G8 science reference sheet (fail-closed, §10)."),
    dict(source="Science formula triangle: Momentum (p=mv)", subject="Science", reason="Not on G8 science reference sheet."),
    dict(source="Science formula triangle: Pressure (P=F/A)", subject="Science", reason="Not on G8 science reference sheet."),
    dict(source="Science formula triangle: Power (P=W/t)", subject="Science", reason="Not on G8 science reference sheet."),
    dict(source="Science formula triangle: Wave speed (v=fλ)", subject="Science", reason="Not on G8 science reference sheet."),
    dict(source="Science formula triangle: Ohm's law (V=IR)", subject="Science", reason="Not on G8 science reference sheet."),
    dict(source="Water cycle diagram", subject="Science", reason="Meaning depends on arrows/labels; ambiguous when stripped (§9)."),
    dict(source="Rock cycle diagram", subject="Science", reason="Cyclic process needs arrows/labels (§9)."),
    dict(source="Weathering/erosion/deposition", subject="Science", reason="Process meaning depends on arrows/labels."),
    dict(source="Life cycles", subject="Science", reason="Sequence meaning depends on arrows/order."),
    dict(source="Food chains / food webs", subject="Science", reason="Energy-flow arrows are essential (§9)."),
    dict(source="Ecological succession", subject="Science", reason="Time-sequence meaning depends on order/labels."),
    dict(source="Heat transfer (conduction/convection/radiation)", subject="Science", reason="Distinctions depend on arrows/labels."),
    dict(source="Electromagnetic spectrum", subject="Science", reason="Meaning depends on labels/scale/values."),
    dict(source="Physical vs chemical change", subject="Science", reason="Abstract; requires labels/examples."),
    dict(source="Photosynthesis", subject="Science", reason="Requires chemical formula/labels."),
    dict(source="Newton's laws / net force diagrams", subject="Science", reason="Force arrows/vectors/labels prohibited (§9)."),
    dict(source="All MATH formula sheets / formula triangles", subject="Math", reason="Math formula aids not a permitted category (§7)."),
    dict(source="Multiplication/operation strategy cards", subject="Math", reason="Procedures/strategies not permitted (§7)."),
    dict(source="Conversion / measurement rule cards", subject="Math", reason="Rule/procedure content not permitted (§7)."),
]


def main():
    manifest = []
    for a in REGISTRY:
        svg = a["fn"]()
        out_dir = os.path.join(ROOT, a["folder"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, a["file"]), "w") as f:
            f.write(svg)
        entry = {k: v for k, v in a.items() if k != "fn"}
        entry["path"] = os.path.join(a["folder"], a["file"])
        manifest.append(entry)
        print("wrote", entry["path"])
    with open(os.path.join(ROOT, "tools", "aids.json"), "w") as f:
        json.dump({"aids": manifest, "classroom_only": CLASSROOM_ONLY}, f, indent=2)
    print(f"\n{len(manifest)} candidate aids; {len(CLASSROOM_ONLY)} classroom-only determinations")


if __name__ == "__main__":
    main()
