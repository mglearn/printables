#!/usr/bin/env python3
"""
Automated aid-type linter (spec section 14).

Reads tools/aids.json and checks each candidate SVG against the content rules for
its declared aid_type. Fail-closed: any violation is reported and exits non-zero.

This is a mechanical backstop, NOT a substitute for the human QA checklist
(section 15) or for local testing review.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

ALLOWED_COLORS = {"#000000", "#ffffff", "#fff", "#666666", "none", "black", "white"}
# Colors permitted: black/white/gray only (no semantic color). section 8/12.

FORMULA_VARS = set("mDVdstFaW")           # variables on the four G8 triangles
OPERATORS = set("=+-*/×÷><±")

NO_TEXT_TYPES = {
    "science_graphic", "blank_graphic_organizer",
    "math_geometry_2d", "math_geometry_3d", "math_fraction_model",
}


def texts(svg):
    return re.findall(r"<text[^>]*>(.*?)</text>", svg, re.S)


def colors(svg):
    out = set()
    for attr in ("fill", "stroke"):
        out |= set(re.findall(attr + r'="([^"]*)"', svg))
    return out


def check(entry, svg):
    t = entry["aid_type"]
    errs = []
    # 1) color rule (all types): grayscale only
    for c in colors(svg):
        if c.lower() not in ALLOWED_COLORS:
            errs.append(f"non-grayscale color '{c}'")
    # 2) marker/arrowhead check (no <marker>/marker-end anywhere)
    if "<marker" in svg or "marker-end" in svg or "marker-start" in svg:
        errs.append("arrow marker present")
    tx = [x.strip() for x in texts(svg)]
    # 3) per-type text rules
    if t in NO_TEXT_TYPES:
        if tx:
            errs.append(f"text not allowed for {t}: {tx!r}")
    elif t == "science_formula_triangle":
        for s in tx:
            if len(s) != 1 or s not in FORMULA_VARS:
                errs.append(f"triangle text must be a single approved variable, got {s!r}")
            if any(ch in OPERATORS for ch in s):
                errs.append(f"operator in triangle text {s!r}")
    elif t == "math_number_chart":
        for s in tx:
            if not s.isdigit():
                errs.append(f"number chart text must be digits, got {s!r}")
    elif t == "math_place_value_chart":
        for s in tx:
            if s not in {",", "."}:
                errs.append(f"place-value text may only be ',' or '.', got {s!r}")
    elif t == "mnemonic":
        if len(tx) != 1 or not re.fullmatch(r"[A-Z]+", tx[0] or ""):
            errs.append(f"mnemonic must be one all-caps acronym token, got {tx!r}")
    else:
        errs.append(f"unknown aid_type {t}")
    return errs


def main():
    data = json.load(open(os.path.join(HERE, "aids.json")))
    total = 0
    failed = 0
    for entry in data["aids"]:
        p = os.path.join(ROOT, entry["path"])
        svg = open(p).read()
        errs = check(entry, svg)
        total += 1
        tag = f"[{entry['aid_type']}] {os.path.basename(entry['path'])}"
        if errs:
            failed += 1
            print(f"FAIL {tag}")
            for e in errs:
                print(f"     - {e}")
        else:
            print(f"ok   {tag}")
    print(f"\n{total - failed}/{total} passed; {failed} failed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
