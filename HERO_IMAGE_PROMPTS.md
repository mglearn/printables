# Codex image prompts — Hero banners for the new printables pages

Three wide hero banners, each modeled on the existing **Science Supplemental Aids**
hero (`supplemental_aids/assets/sa_hero.png`) so the new pages match the site.
**Prepend the SHARED HERO SPEC to every prompt**, then append the per-hero prompt.

Save each with the **exact absolute path** in its heading. After they're in place no
build step is needed for heroes (the pages already reference them).

---

## SHARED HERO SPEC (prepend to every prompt)

> Wide landscape web hero banner, **2172 × 724 px (≈3:1), 300 DPI**, flat modern
> vector infographic style for a teacher-printables website. Pale background
> (#F5FAFF) with very faint, light-blue line-art doodles of the subject scattered
> subtly behind everything (never competing with the text). Clean, airy, professional.
>
> **Layout (match the reference exactly):**
> 1. **Upper-left block (~60% width):** a big bold navy (#14213A) wordmark TITLE, then
>    one short description sentence in slate (#3A4A66) beneath it, then a line with a
>    green (#1AA39A) circular checkmark and bold green tagline
>    **"Free to use, print, share, and adapt."**
> 2. **Upper-right:** a row of **four benefit badges**, each a rounded-square colored
>    icon tile above a two-line label:
>    • **PRINT / Friendly** (teal printer icon)
>    • **SHARE / Freely** (green share-nodes icon)
>    • **ADAPT / to Your Classroom** (orange pencil icon)
>    • **SUPPORT / Student Success** (violet graduation-cap icon)
> 3. **Bottom band:** a horizontal row of **five small preview "mini-cards"**, evenly
>    spaced. Each mini-card is a white rounded rectangle with a **colored header bar**
>    (white ALL-CAPS label) and a tiny simplified illustration of that topic inside.
>    Header colors left→right: teal #1596A3, blue #2F6FDB, green #1AA39A, navy #0B3D6B,
>    violet #6B4FBB.
> 4. **Subject illustrations:** one friendly flat illustration tucked in the lower-left
>    corner and one in the far right of the title band (like the microscope + beaker in
>    the reference), colored, simple, not photographic.
>
> **Palette:** navy #14213A / #0B3D6B, teal #1596A3, blue #2F6FDB, green #1AA39A,
> violet #6B4FBB, orange #F39C2D, amber #F4B400. Bold heavy sans-serif
> (Poppins / Montserrat / Nunito feel). All text spelled correctly, evenly kerned,
> fully inside the frame — nothing clipped. No photographic elements, no heavy
> shadows, no watermark, no logo, no outer border.

Keep all three heroes visually consistent with each other and with the science
reference — same badge row, same tagline, same mini-card treatment.

---

### /home/mg/Documents/vibecoding/mglearn/printables/supplemental_aids_math/assets/hero.png
**Math Supplemental Aids hero.**
- TITLE: "Math Supplemental Aids"
- Description: "Visual cue cards for grades 6–8 that help students retrieve what they
  already learned — integer rules, fractions and percents, ratios and proportions,
  equations, the coordinate plane, and slope."
- Corner illustrations: lower-left a protractor + ruler + pencil; far-right a friendly
  calculator with a few floating operation symbols (＋ − × ÷).
- Five bottom mini-cards (header + tiny content):
  1. **FORMULA REFERENCE** (teal) — a small rectangle and triangle with A = l w and
     A = ½ b h.
  2. **NUMBER & OPERATIONS** (blue) — signed-number tiles (+ / −) and a fraction bar 3/4.
  3. **PROPORTIONALITY** (green) — a ratio "3 : 2" with dots and a small percent bar.
  4. **EXPRESSIONS & EQUATIONS** (navy) — a balance scale holding "x" with "2x + 3 = 11".
  5. **DATA & STATISTICS** (violet) — a tiny 4-bar chart with "mean · median · mode".

### /home/mg/Documents/vibecoding/mglearn/printables/supplemental_aids_elem_science/assets/hero.png
**Elementary Science Supplemental Aids (STAAR) hero.**
- TITLE: "Elementary Science Supplemental Aids"  (add a smaller teal kicker line above
  or beside it: "Grades 3–5 · STAAR review")
- Description: "Visual cue cards for grades 3–5 that help students retrieve what they
  already learned for the Grade 5 Science STAAR — across the four reporting categories."
- Corner illustrations: lower-left a hand lens over a green leaf; far-right a globe with
  a small Sun and cloud.
- Five bottom mini-cards (header + tiny content):
  1. **SCIENCE SKILLS** (teal) — a hand lens + ruler + safety goggles.
  2. **MATTER & ENERGY** (blue) — a beaker and solid/liquid/gas particle dots.
  3. **FORCE, MOTION & ENERGY** (green) — a light bulb, a simple circuit, and a motion arrow.
  4. **EARTH & SPACE** (navy) — the Sun, a water-cycle arrow loop, and a small globe.
  5. **ORGANISMS & ENVIRONMENTS** (violet) — a leaf/plant with a food-chain arrow to an animal.

### /home/mg/Documents/vibecoding/mglearn/printables/math/assets/hero.png
**Math Printables hub hero (grades 3–8).**
- TITLE: "Math Printables"  (add a smaller teal kicker line: "Free math resources for
  grades 3–8")
- Description: "Classroom-ready math printables you can download, print, and adapt —
  visual cue cards, formula references, and supports across the grade band. More
  collections on the way."
- Corner illustrations: lower-left geometric shapes (triangle, circle, square) with a
  ruler; far-right a protractor and a few large friendly numbers (3 … 8).
- Five bottom mini-cards — reuse the math strand set so the hub previews its flagship
  collection, but tint them to read as a spanning grade-band ribbon:
  1. **NUMBER & OPERATIONS** (teal) — signed-number tiles and a fraction bar.
  2. **PROPORTIONALITY** (blue) — a ratio "3 : 2" and a percent bar.
  3. **EXPRESSIONS & EQUATIONS** (green) — a balance scale with "x".
  4. **GEOMETRY & MEASUREMENT** (navy) — a rectangle/triangle with formulas.
  5. **DATA & STATISTICS** (violet) — a small bar chart.
  (Optional: a thin "GRADES 3–8" ribbon along the bottom edge.)
