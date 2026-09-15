# Codex image prompts — Elementary Math Supplemental Aids (grades 3–5)

Generate one PNG per section below into this folder
(`printables/supplemental_aids_elem_math/`) using the **exact filename** in each
heading. All sheets share the house style described first — **prepend the STYLE
BLOCK to every prompt**, then append the per-sheet prompt.

After generating, run from this folder:

```bash
./build-pdfs.sh          # makes color + B&W print PDF next to each PNG
./build-manifest.sh      # refreshes assets/sa-manifest.js (auto-links PDFs)
```

Groups follow the four Grade 3–5 Math STAAR reporting categories.

---

## STYLE BLOCK (prepend to every prompt)

> Flat vector infographic "cue card" for an elementary classroom printable, clean
> modern educational style, friendly and colorful but uncluttered. **Portrait, US
> Letter proportions (8.5 × 11), render at ~2550 × 3300 px, 300 DPI**, generous white
> margins, pure white (#FFFFFF) background. No photographic elements, no 3-D bevels,
> no heavy drop shadows, no busy textures. Crisp geometric shapes, rounded corners
> (12–20px), bold flat fills, thin (2–3px) outline accents. Simple, cheerful flat
> icons and math diagrams that a 3rd–5th grader can read at a glance.
>
> **Typography:** bold heavy sans-serif (Poppins / Montserrat / Nunito feel). Main
> **title** in deep navy (#14213A), large and centered at top. A **subtitle**
> beneath it in teal (#1596A3) or violet (#6B4FBB). Body labels in dark slate on
> light panels, large and legible. All numbers, symbols, and text spelled/typeset
> correctly, evenly kerned, fully inside the margins — no cut-off words. Any math
> shown must be arithmetically correct.
>
> **Palette:** navy #14213A / #0B3D6B, teal #1596A3, violet #6B4FBB, blue #2F6FDB,
> green #1F9E57, coral #EF6F6C, amber #F4B400. Numbered step badges are filled
> circles with a white number. Bullet checks are teal circular checkmarks. Use a
> single amber star "key idea" callout bar near the bottom when noted.
>
> **Layout:** title + subtitle band at top; a clear central diagram or a grid of
> 2–5 rounded panels; a one-line takeaway callout at the bottom. Balanced, airy,
> lots of whitespace. Consistent icon style across the whole set. Print-safe (high
> contrast, works in grayscale). No watermark, no logo, no border frame, no page
> numbers.

Keep every sheet visually consistent — same title treatment, badges, checkmarks,
palette. Think "a matching set," and consistent with the elementary science set.

---

## Hero + thumbnail (site chrome)

### assets/hero.png — collection hero banner
Wide landscape web hero banner, **2172 × 724 px (≈3:1), 300 DPI**, matching the
existing Science Supplemental Aids hero. Pale (#F5FAFF) background with faint math
doodles. Upper-left: bold navy wordmark **"Elementary Math Supplemental Aids"** with
a teal kicker "Grades 3–5 · STAAR" and a one-line description ("Visual cue cards that
help students retrieve what they already learned"), then a green circular checkmark +
green tagline **"Free to use, print, share, and adapt."** Upper-right: four benefit
badges — **PRINT / Friendly** (teal), **SHARE / Freely** (green), **ADAPT / to Your
Classroom** (orange), **SUPPORT / Student Success** (violet). Bottom band: five small
preview mini-cards with colored headers (teal, blue, green, navy, violet) —
Place Value, Fractions, Multiplication, Shapes & Area, Graphs — each with a tiny flat
diagram. Corner illustrations: lower-left a ruler + pencil + geometric shapes;
far-right a friendly abacus or number blocks. No photographic elements.

### ../assets/thumb-elem-math.png — home/hub card thumbnail
**Square-ish, ~1200 × 900 px.** A neat 2 × 2 tile of four miniature cue cards
(a place-value chart, a fraction bar 3/4, a multiplication array, and a rectangle
labeled area), same flat palette, to advertise the collection on the Math Printables
hub and Teacher Printables home page.

---

## Start here

### em_overview.png — "Grades 3–5 Math — Overview"
Title "Elementary Math" (navy), subtitle "STAAR Reporting Categories · Grades 3–5"
(teal). A 2 × 2 grid of rounded panels, one per category, each with a big friendly
icon and 2–3 sample topics:
1. **Numbers & Fractions** (place-value blocks) — place value, rounding, fractions, decimals.
2. **Operations & Algebra** (± × ÷) — add/subtract, multiply, divide, patterns, equations.
3. **Geometry & Measurement** (shapes + ruler) — 2D/3D shapes, perimeter, area, volume, time.
4. **Data & Financial Literacy** (bar graph + coin) — graphs, tables, money and budgeting.
Bottom amber callout: "One picture per skill — recall, not re-teach."

## Numbers & Fractions

### em_place_value.png — "Place Value"
Title "Place Value" (navy), subtitle "Every place is 10 times the next" (teal). A
**place-value chart** with columns from thousands down to thousandths, one number
placed in it (e.g., 3,472.85) with each digit's value labeled (3,000 · 400 · 70 · 2 ·
0.8 · 0.05). Arrow strip: "×10 as you move left, ÷10 as you move right." Bottom amber
callout: "The place tells you the value of the digit."

### em_rounding.png — "Rounding Numbers"
Title "Rounding" (navy), subtitle "Find the place · check the neighbor" (teal). Steps:
1) underline the rounding place, 2) look at the digit to its right, 3) "5 or more →
round up; 4 or less → stay the same," 4) digits after become 0. A **number-line**
example rounding 47 to 50 (nearest ten). Bottom amber callout: "Look right to decide;
everything after becomes zero."

### em_compare_order.png — "Comparing & Ordering Numbers"
Title "Comparing Numbers" (navy), subtitle "Line up the places" (teal). Show the
symbols with a mouth cue: **>** greater than, **<** less than, **=** equal ("the
alligator eats the bigger number"). Example comparing 4,512 vs 4,521 by lining up
place values from the left. A small ordering strip least → greatest. Bottom amber
callout: "Compare from the left, one place at a time."

### em_decimals.png — "Decimals & Place Value"
Title "Decimals" (navy), subtitle "Tenths · Hundredths · Thousandths" (teal). A
**10×10 grid** shaded to show 0.25 = 25/100, next to a place-value chart for a decimal
(e.g., 0.375). Money tie-in: $0.50 = 5 tenths = 50 hundredths. Bottom amber callout:
"A decimal names part of a whole, just like a fraction."

### em_fractions_intro.png — "Understanding Fractions"
Title "Understanding Fractions" (navy), subtitle "Equal parts of a whole" (teal). A
big fraction (3/4) with **numerator** labeled "parts we have" and **denominator**
"equal parts in all," beside a circle and a bar each split into 4 equal parts with 3
shaded. Small note: bigger denominator → smaller pieces. Bottom amber callout: "The
bottom number tells how many equal parts make one whole."

### em_equivalent_fractions.png — "Equivalent Fractions"
Title "Equivalent Fractions" (navy), subtitle "Same amount, different name" (teal).
Show 1/2 = 2/4 = 4/8 with three same-size bars split into 2, 4, and 8 parts, equal
shading. The rule: "multiply or divide top and bottom by the same number" (×2/×2
arrows). Bottom amber callout: "Multiply or divide top and bottom by the same
number."

### em_compare_fractions.png — "Comparing Fractions"
Title "Comparing Fractions" (navy), subtitle "Which is bigger?" (teal). Three cases in
panels: **same denominator** (compare numerators: 3/5 > 2/5), **same numerator**
(fewer parts are bigger: 1/3 > 1/4), and **make a common denominator**. Fraction bars
show each comparison. Bottom amber callout: "Same bottoms? Compare tops. Same tops?
Fewer pieces win."

### em_fractions_decimals.png — "Fractions & Decimals"
Title "Fractions & Decimals" (navy), subtitle "Two names, one value" (teal). A
**number line** from 0 to 1 marking 1/4 = 0.25, 1/2 = 0.5, 3/4 = 0.75, with a 10×10
grid and place-value chart connecting 5/10 and 0.5. Bottom amber callout: "A fraction
and a decimal can name the exact same amount."

## Operations & Algebra

### em_addition_subtraction.png — "Multi-Digit Addition & Subtraction"
Title "Add & Subtract" (navy), subtitle "Line up the places" (teal). Two worked
column examples side by side: an addition with **regrouping/carry** (e.g., 367 + 158)
and a subtraction with **borrowing** (e.g., 502 − 148), each aligned by place value
with the regroup marks shown. Bottom amber callout: "Line up ones, tens, hundreds —
regroup when a column is 10 or more."

### em_multiplication.png — "Multiplication"
Title "Multiplication" (navy), subtitle "Equal groups & arrays" (teal). Show 3 × 4 as
3 groups of 4 dots and as a 3-by-4 **array** (= 12), plus an **area model** for a
two-digit product (e.g., 12 × 13 split into 10+2 and 10+3). Bottom amber callout:
"Multiplication is repeated equal groups."

### em_division.png — "Division"
Title "Division" (navy), subtitle "Sharing into equal groups" (teal). Show 12 ÷ 3 = 4
as 12 dots shared into 3 equal groups, with parts labeled **dividend ÷ divisor =
quotient**, and one example with a **remainder** (e.g., 13 ÷ 4 = 3 R1). Bottom amber
callout: "Division splits a total into equal groups."

### em_fraction_add_sub.png — "Adding & Subtracting Fractions"
Title "Add & Subtract Fractions" (navy), subtitle "Same denominator first" (teal).
Fraction bars showing 1/4 + 2/4 = 3/4 (add the numerators, keep the denominator) and
3/5 − 1/5 = 2/5. A reminder that the denominator does not change. Bottom amber
callout: "Add or subtract the top numbers; keep the bottom the same."

### em_number_patterns.png — "Number Patterns & Tables"
Title "Number Patterns" (navy), subtitle "Find the rule" (teal). An **input–output
table** (in: 1,2,3,4 → out: 3,6,9,12) with the rule "× 3" shown, and a growing
picture pattern. Prompt: "What comes next?" Bottom amber callout: "Find the rule, then
use it to extend the pattern."

### em_expressions_equations.png — "Expressions & Equations"
Title "Expressions & Equations" (navy), subtitle "Order of operations & unknowns"
(teal). Left: order of operations for grades 3–5 — grouping symbols ( ) first, then
multiply/divide, then add/subtract, with a worked example 2 × (3 + 4) = 14. Right: a
simple equation with a box/letter for the unknown, e.g., 5 + ▢ = 12 → ▢ = 7. Bottom
amber callout: "Do the parentheses first; a letter or box stands for a missing
number."

## Geometry & Measurement

### em_2d_shapes.png — "2D Shapes & Attributes"
Title "2D Shapes" (navy), subtitle "Sort by sides & angles" (teal). A tidy grid of
polygons labeled with side/angle counts — triangle, square, rectangle, rhombus,
trapezoid, pentagon, hexagon — plus a note on the **quadrilateral family**. Bottom
amber callout: "Classify shapes by their number of sides and angles."

### em_3d_shapes.png — "3D Solids"
Title "3D Solids" (navy), subtitle "Faces · Edges · Vertices" (teal). Flat drawings of
a cube, rectangular prism, pyramid, cylinder, cone, and sphere, each labeled with its
number of faces, edges, and vertices. Bottom amber callout: "Solids have faces (flat
sides), edges, and vertices (corners)."

### em_perimeter_area.png — "Perimeter & Area"
Title "Perimeter & Area" (navy), subtitle "Around vs. inside" (teal). A rectangle
(length 5, width 3) shown twice: **perimeter** = add all sides (5+3+5+3 = 16 units)
with the border highlighted, and **area** = l × w = 15 square units with the inside
filled with unit squares. Bottom amber callout: "Perimeter is the distance around;
area is the square units inside."

### em_volume.png — "Volume"
Title "Volume" (navy), subtitle "Filling with unit cubes" (teal). A rectangular prism
built from unit cubes (e.g., 4 × 2 × 3) showing V = l × w × h = 24 cubic units, with
one layer highlighted. Bottom amber callout: "Volume counts the unit cubes that fill a
solid."

### em_measurement_units.png — "Measurement Units"
Title "Measurement Units" (navy), subtitle "Length · Weight · Capacity" (teal). Two
columns — **Customary** (inch/foot/yard; ounce/pound; cup/pint/quart/gallon) and
**Metric** (cm/m/km; gram/kilogram; milliliter/liter) — with a small "gallon man" or
stair-step for converting within a system. Bottom amber callout: "Pick the unit that
fits what you're measuring; convert within one system."

### em_elapsed_time.png — "Telling & Elapsed Time"
Title "Telling Time" (navy), subtitle "Read it · count it" (teal). An analog clock
reading a time (e.g., 3:15) next to a **number-line** jump strip counting elapsed time
from 3:15 to 4:00 (start → +45 min → end). Bottom amber callout: "Count up on a number
line to find how much time has passed."

### em_angles_lines.png — "Lines & Angles"
Title "Lines & Angles" (navy), subtitle "Name what you see" (teal). Panels: point,
line, ray, and segment; **parallel** vs **perpendicular** lines; and **right, acute,
obtuse** angles with a small square marking the right angle. Bottom amber callout:
"A right angle is a square corner; acute is smaller, obtuse is larger."

### em_coordinate_grid.png — "The Coordinate Grid"
Title "The Coordinate Grid" (navy), subtitle "Plot ordered pairs (x, y)" (teal). A
**first-quadrant grid** with labeled x- and y-axes and the origin, one point plotted
(e.g., (3, 2)) with dashed guides showing "over 3, then up 2." Bottom amber callout:
"Go over on the x-axis first, then up on the y-axis."

## Data & Financial Literacy

### em_graphs.png — "Reading Graphs"
Title "Reading Graphs" (navy), subtitle "Bar · Picture · Dot plot" (teal). Three small
sample graphs — a bar graph, a pictograph with a key, and a dot plot — each with a
one-line "how to read it" and a sample question. Bottom amber callout: "Read the title,
labels, and key before you answer."

### em_data_tables.png — "Frequency Tables & Dot Plots"
Title "Organizing Data" (navy), subtitle "Tally · Table · Dot plot" (teal). Show the
same small data set as **tally marks**, a **frequency table**, and a **dot plot**, so
students see one data set three ways. Bottom amber callout: "Tally it, table it, then
plot it."

### em_financial_literacy.png — "Money & Financial Literacy"
Title "Money Smarts" (navy), subtitle "Earn · Save · Spend" (teal). Panels: counting
coins and bills and **making change** (count up from the price), the difference
between **saving and spending**, **income** (earned vs. gift), and a simple **budget**
(needs vs. wants). Bottom amber callout: "A budget plans money for needs, wants, and
saving."
