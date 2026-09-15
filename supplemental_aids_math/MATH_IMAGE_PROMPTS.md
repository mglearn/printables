# Codex image prompts — Math Supplemental Aids (grades 6–8)

Generate one PNG per section below into this folder
(`printables/supplemental_aids_math/`) using the **exact filename** in each
heading. All sheets share the house style described first — **prepend the STYLE
BLOCK to every prompt**, then append the per-sheet prompt.

After generating, run:

```bash
./build-pdfs.sh          # makes color + B&W print PDF next to each PNG
./build-manifest.sh      # refreshes assets/sa-manifest.js (auto-links PDFs)
```

---

## STYLE BLOCK (prepend to every prompt)

> Flat vector infographic "cue card" for a classroom printable, in a clean modern
> educational style. **Portrait, US Letter proportions (8.5 × 11), render at
> ~2550 × 3300 px, 300 DPI**, with generous white margins and a pure white (#FFFFFF)
> background. No photographic elements, no 3-D bevels, no drop shadows heavier than a
> soft 4px, no gradients except very subtle flat tints. Crisp geometric shapes,
> rounded corners (12–20px radius), bold flat fills, thin (2–3px) outline accents.
>
> **Typography:** bold heavy sans-serif (Poppins / Montserrat / Nunito feel).
> Main **title** in deep navy (#14213A), large and centered at top. A **subtitle**
> directly under it in teal (#1596A3) or violet (#6B4FBB), smaller. Body labels in
> dark slate (#14213A) on light panels. All text must be spelled correctly, evenly
> kerned, and fully inside the margins — no cut-off words.
>
> **Palette:** navy #14213A / #0B3D6B, teal #1596A3, violet #6B4FBB, blue #2F6FDB,
> green #1AA39A, coral #EF6F6C, amber #F4B400. Numbered step badges are filled
> circles with a white number. Bullet checks are teal circular checkmarks. Use a
> single amber star "key idea" callout bar near the bottom when noted.
>
> **Layout:** title + subtitle band at top; a clear central diagram or a grid of
> 2–4 rounded panels; a one-line takeaway callout at the bottom. Balanced, airy,
> lots of whitespace. Consistent icon style: simple flat line-and-fill icons.
> Print-safe (high contrast, works in grayscale). No watermark, no logo, no border
> frame, no page numbers.

Keep every sheet visually consistent with the others: same title treatment, same
badge/checkmark shapes, same palette. Think "a matching set."

---

## Hero + thumbnail (site chrome)

### assets/hero.png — collection hero banner
**See `HERO_IMAGE_PROMPTS.md`** for the full, science-matching hero spec
(2172 × 724, wordmark + description + tagline + PRINT/SHARE/ADAPT/SUPPORT badges + a
row of five mini strand-cards). Generate the hero from that file, not from here.

### ../assets/thumb-math-supplemental-aids.png — home-page card thumbnail
**Square-ish, ~1200 × 900 px.** A neat 2 × 2 tile of four miniature cue cards
(integer rules, a formula-reference triangle, a percent bar, a coordinate plane),
same flat palette, to advertise the collection on the Teacher Printables home page.

---

## Start here

### ma_overview.png — "Middle School Math — Overview"
Title "Middle School Math" (navy), subtitle "Supplemental Aids · Grades 6–8"
(teal). Below, a one-page map of the collection: **four labeled rounded panels in a
2 × 2 grid**, one per strand, each with a small icon and 2–3 sample topics:
1. **Number & Operations** (icon: ± signs / fraction bar) — integers, order of
   operations, fractions, fraction–decimal–percent.
2. **Proportionality** (icon: two nested ratios / percent) — ratios & unit rate,
   proportions, percent applications.
3. **Expressions, Equations & Relationships** (icon: balance scale with x) —
   like terms, one/two-step equations, inequalities, coordinate plane, slope.
4. **Data & Statistics** (icon: small bar chart) — mean/median/mode/range,
   probability.
Bottom amber callout: "One picture per skill — a cue students already understand."

## Reference

### ma_formula_reference.png — "Measurement Formula Reference"
Title "Measurement Formulas" (navy), subtitle "Perimeter · Area · Volume · Surface
Area" (teal). A tidy **grid of small shape tiles**, each showing the flat shape with
its dimensions labeled and the formula beneath:
- Rectangle: A = l × w ; P = 2l + 2w
- Triangle: A = ½ b h
- Parallelogram: A = b h
- Trapezoid: A = ½ (b₁ + b₂) h
- Circle: A = π r² ; C = 2π r (or π d)
- Rectangular prism: V = l w h ; SA = 2(lw + lh + wh)
- Cylinder: V = π r² h
- Cube: V = s³
Each shape drawn as a clean flat diagram with dimension labels (l, w, h, b, r).
Bottom amber callout: "Match the shape to its formula, then substitute and solve."

## Number & Operations

### ma_integer_operations.png — "Integer Operation Rules"
Title "Integer Rules" (navy), subtitle "Adding · Subtracting · Multiplying ·
Dividing" (teal). Two stacked sections in rounded panels:
- **Add & Subtract** panel: "Same signs → add & keep the sign" (example: −3 + −5 =
  −8) and "Different signs → subtract & take the sign of the larger absolute value"
  (example: −7 + 4 = −3). Small number-line cue.
- **Multiply & Divide** panel: a 2 × 2 sign grid — (+)(+) = + , (−)(−) = + ,
  (+)(−) = − , (−)(+) = − . Cue: "Same signs → positive · Different signs →
  negative."
Bottom amber callout: "Even number of negatives → positive; odd → negative."

### ma_order_of_operations.png — "Order of Operations (GEMDAS)"
Title "Order of Operations" (navy), subtitle "GEMDAS" (teal). A **vertical numbered
ladder of 4 badge steps**:
1. **G** — Grouping symbols ( ), [ ]
2. **E** — Exponents
3. **MD** — Multiply & Divide, left → right
4. **AS** — Add & Subtract, left → right
Right side: one worked example evaluated step by step, e.g.
`3 + 2 × (5 − 1)² = 3 + 2 × 16 = 3 + 32 = 35`, each line aligned to its step.
Bottom amber callout: "Multiply/Divide and Add/Subtract go left to right — not M
before D."

### ma_fraction_operations.png — "Fraction Operations"
Title "Fraction Operations" (navy), subtitle "Add · Subtract · Multiply · Divide"
(teal). Four rounded panels, each with a tiny fraction-bar picture and a worked mini
example:
- **Add / Subtract**: "Common denominator first," e.g. 1/4 + 2/4 = 3/4.
- **Multiply**: "Multiply across," e.g. 2/3 × 3/5 = 6/15 = 2/5.
- **Divide (KCF)**: "Keep · Change · Flip," e.g. 1/2 ÷ 1/4 = 1/2 × 4/1 = 2.
- **Simplify**: divide top and bottom by the GCF, e.g. 6/15 = 2/5.
Bottom amber callout: "Add/subtract need a common denominator — multiply/divide do
not."

### ma_fraction_decimal_percent.png — "Fractions, Decimals & Percents"
Title "Fractions · Decimals · Percents" (navy), subtitle "Three ways to say the same
value" (teal). A **triangle diagram** with the three forms at its corners and the
conversion on each edge:
- Fraction → Decimal: "divide top ÷ bottom"
- Decimal → Percent: "× 100, move decimal 2 right, add %"
- Percent → Fraction: "put over 100, simplify"
Plus a small reference row: 1/2 = 0.5 = 50% ; 1/4 = 0.25 = 25% ; 3/4 = 0.75 = 75% ;
1/10 = 0.1 = 10%. Bottom amber callout: "Percent means 'out of 100.'"

## Proportionality

### ma_ratios_unit_rate.png — "Ratios & Unit Rate"
Title "Ratios & Unit Rate" (navy), subtitle "Comparing quantities" (teal). Top
panel: a ratio shown three ways — "3 to 2", "3 : 2", "3/2" — with a small picture of
3 blue dots to 2 green dots. Bottom panel: **unit rate** = "divide to get per ONE,"
worked example: "$6 for 3 apples → $2 per apple," with the division shown. Bottom
amber callout: "A unit rate has a denominator of 1."

### ma_proportions.png — "Proportions & Cross Products"
Title "Proportions" (navy), subtitle "Two equal ratios" (teal). Center: two
fractions set equal, `a/b = c/d`, with big diagonal **cross-multiply arrows**
showing a × d = b × c. Worked example: `3/4 = x/12 → 4x = 36 → x = 9`. A small
scaling picture (a shape enlarged) reinforces "same ratio, different size." Bottom
amber callout: "Cross-multiply, then solve for the missing value."

### ma_percent_applications.png — "Percent Applications"
Title "Percent Problems" (navy), subtitle "Part · Whole · Percent" (teal). Top: the
relationship `part = percent × whole` with a **percent bar model** (a 0–100% bar
split into a shaded part). Three worked mini panels:
- **Percent of a number**: 20% of 50 = 0.20 × 50 = 10.
- **Percent change**: (new − old) ÷ old × 100.
- **Tax / tip / discount**: total = price ± (percent × price).
Bottom amber callout: "Turn the percent into a decimal before you multiply."

## Expressions, Equations & Relationships

### ma_combining_like_terms.png — "Expressions: Like Terms & Distributive"
Title "Simplifying Expressions" (navy), subtitle "Like Terms · Distributive
Property" (teal). Two panels:
- **Combine like terms**: like terms share the same variable & exponent; color-code
  matching terms, e.g. `3x + 5 + 2x = 5x + 5` (the x-terms highlighted one color, the
  constant another).
- **Distributive property**: `a(b + c) = ab + ac` with curved arrows from a over
  each term, worked example `3(x + 4) = 3x + 12`.
Bottom amber callout: "You can only combine terms that are truly alike."

### ma_one_two_step_equations.png — "Solving One- & Two-Step Equations"
Title "Solving Equations" (navy), subtitle "Undo with inverse operations" (teal).
Center: a **balance-scale** motif emphasizing "do the same to both sides." Two
worked columns:
- **One-step**: `x + 7 = 12 → −7 both sides → x = 5`.
- **Two-step**: `2x + 3 = 11 → −3 → 2x = 8 → ÷2 → x = 4`.
Show the inverse operation labeled next to each step. Bottom amber callout: "Undo
addition/subtraction first, then multiplication/division."

### ma_inequalities.png — "Solving & Graphing Inequalities"
Title "Inequalities" (navy), subtitle "Solve · Graph · Flip" (teal). Left: the four
symbols with meanings (< less than, > greater than, ≤ at most, ≥ at least). Center: a
worked example `−2x < 6 → x > −3` with a bold red note **"flip the sign when you
multiply or divide by a negative."** Right: a **number line** showing an open circle
(< or >) vs. a closed/filled circle (≤ or ≥) with the shaded ray. Bottom amber
callout: "Open circle = not included; closed circle = included."

### ma_coordinate_plane.png — "The Coordinate Plane"
Title "The Coordinate Plane" (navy), subtitle "Plotting ordered pairs (x, y)"
(teal). A large **four-quadrant grid** with labeled x-axis and y-axis, the origin
(0,0), and quadrants I–IV marked with their sign patterns (+,+), (−,+), (−,−),
(+,−). Plot one example point, e.g. (3, 2), with dashed guide lines showing "over 3,
up 2." Bottom amber callout: "x first (over), then y (up or down)."

### ma_slope_linear.png — "Slope & Linear Relationships"
Title "Slope & Linear Equations" (navy), subtitle "y = mx + b" (teal). A coordinate
grid with a straight line, a **slope triangle** showing rise over run
(e.g. rise 2, run 1 → slope = 2), the **y-intercept** b marked where the line crosses
the y-axis, and callouts: "m = slope = rise/run," "b = y-intercept." Small strip of
the four slope types (positive, negative, zero, undefined). Bottom amber callout:
"m tilts the line; b slides it up or down."

## Data & Statistics

### ma_measures_of_center.png — "Mean, Median, Mode & Range"
Title "Measures of Center & Spread" (navy), subtitle "Mean · Median · Mode · Range"
(teal). Use one small data set throughout, e.g. **3, 5, 5, 8, 9**, and four panels:
- **Mean** — "average: add, then divide by how many" → (3+5+5+8+9)/5 = 6.
- **Median** — "middle when ordered" → 5.
- **Mode** — "most often" → 5.
- **Range** — "highest − lowest" → 9 − 3 = 6.
Bottom amber callout: "Order the numbers first — it makes median and range easy."

### ma_probability.png — "Simple Probability"
Title "Simple Probability" (navy), subtitle "How likely is it?" (teal). Center:
`P(event) = favorable outcomes ÷ total outcomes`, with a worked example using a spinner
or bag of marbles, e.g. "3 red of 5 marbles → P(red) = 3/5." A **0-to-1 likelihood
scale** labeled impossible (0) · unlikely · even chance (½) · likely · certain (1).
Small note: "experimental (from trials) vs. theoretical (from what's possible)."
Bottom amber callout: "Probability is always between 0 and 1."
