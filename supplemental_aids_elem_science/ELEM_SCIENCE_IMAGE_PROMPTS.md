# Codex image prompts — Elementary Science Supplemental Aids (STAAR, grades 3–5)

Generate one PNG per section below into this folder
(`printables/supplemental_aids_elem_science/`) using the **exact filename** in each
heading. All sheets share the house style described first — **prepend the STYLE
BLOCK to every prompt**, then append the per-sheet prompt.

After generating, run:

```bash
./build-pdfs.sh          # makes color + B&W print PDF next to each PNG
./build-manifest.sh      # refreshes assets/sa-manifest.js (auto-links PDFs)
```

Groups follow the four Grade-5 Science STAAR reporting categories; the concepts
span the grades 3–5 TEKS as an elementary spiral toward the tested grade.

---

## STYLE BLOCK (prepend to every prompt)

> Flat vector infographic "cue card" for an elementary classroom printable, clean
> modern educational style, friendly and colorful but uncluttered. **Portrait, US
> Letter proportions (8.5 × 11), render at ~2550 × 3300 px, 300 DPI**, generous white
> margins, pure white (#FFFFFF) background. No photographic elements, no 3-D bevels,
> no heavy drop shadows, no busy textures. Crisp geometric shapes, rounded corners
> (12–20px), bold flat fills, thin (2–3px) outline accents. Simple, cheerful flat
> icons and diagrams that a 3rd–5th grader can read at a glance.
>
> **Typography:** bold heavy sans-serif (Poppins / Montserrat / Nunito feel). Main
> **title** in deep navy (#14213A), large and centered at top. A **subtitle**
> beneath it in teal (#1596A3) or violet (#6B4FBB). Body labels in dark slate on
> light panels, large and legible. All text spelled correctly, evenly kerned, fully
> inside the margins — no cut-off words.
>
> **Palette:** navy #14213A / #0B3D6B, teal #1596A3, violet #6B4FBB, blue #2F6FDB,
> green #1AA39A, coral #EF6F6C, amber #F4B400. Numbered step badges are filled
> circles with a white number. Bullet checks are teal circular checkmarks. Use a
> single amber star "key idea" callout bar near the bottom when noted.
>
> **Layout:** title + subtitle band at top; a clear central diagram or a grid of
> 2–5 rounded panels; a one-line takeaway callout at the bottom. Balanced, airy,
> lots of whitespace. Consistent icon style across the whole set. Print-safe (high
> contrast, works in grayscale). No watermark, no logo, no border frame, no page
> numbers.

Keep every sheet visually consistent — same title treatment, badges, checkmarks,
palette. Think "a matching set."

The five **"— Five Cue Cards"** overview posters use a shared template: title band,
then five numbered rounded panels (a 2-then-3 or vertical stack) each naming one of
the concept cards in that category with its icon and a one-line idea.

---

## Hero + thumbnail (site chrome)

### assets/hero.png — collection hero banner
**See `HERO_IMAGE_PROMPTS.md`** for the full, science-matching hero spec
(2172 × 724, wordmark + description + tagline + PRINT/SHARE/ADAPT/SUPPORT badges + a
row of five mini category-cards). Generate the hero from that file, not from here.

### ../assets/thumb-elem-science.png — home-page card thumbnail
**Square-ish, ~1200 × 900 px.** A 2 × 2 tile of four miniature category icons
(Matter & Energy, Force/Motion/Energy, Earth & Space, Organisms & Environments) in
the flat palette, to advertise the collection on the Teacher Printables home page.

---

## Start here

### es_overview.png — "Grades 3–5 Science — Overview"
Title "Elementary Science" (navy), subtitle "STAAR Reporting Categories · Grades
3–5" (teal). A 2 × 2 grid of rounded panels, one per reporting category, each with a
big friendly icon and 2–3 sample topics:
1. **Matter & Energy** (beaker) — properties, states, mixtures & solutions.
2. **Force, Motion & Energy** (bulb + arrow) — forms of energy, light, circuits, motion.
3. **Earth & Space** (globe + Sun) — water cycle, weather, Earth's surface, sky.
4. **Organisms & Environments** (leaf + animal) — plants, life cycles, adaptations,
   food chains.
Bottom amber callout: "One picture per idea — recall, not re-teach."

## Science Skills

### es_science_tools_safety.png — "Science Tools & Safety"
Title "Science Tools & Safety" (navy), subtitle "Match the tool to the job" (teal).
A grid of labeled flat tool icons with a one-line use each: **hand lens** (look
closely), **balance** (measure mass, g), **graduated cylinder** (measure liquid
volume, mL), **thermometer** (temperature, °C), **ruler/meter stick** (length, cm),
**safety goggles** (protect eyes). A small amber safety strip: "Goggles on · walk,
don't run · follow directions · clean up." Bottom amber callout: "The right tool
gives the right measurement."

### es_investigation_evidence.png — "Investigation & Evidence"
Title "Science Investigation" (navy), subtitle "How scientists find out" (teal). A
**circular numbered cycle** of 6 badges: 1 Ask a question · 2 Predict · 3 Plan a
fair test · 4 Observe & measure · 5 Record data · 6 Explain from evidence. Small note
about a **fair test**: "change one thing, keep the rest the same." Bottom amber
callout: "A conclusion must be backed by the evidence you collected."

## Matter & Energy

### es_matter_energy_overview.png — "Matter & Energy — Five Cue Cards"
Overview poster (shared template). Five panels: 1 Physical Properties · 2 States of
Matter · 3 Measuring Matter · 4 Mixtures & Solutions · 5 Changes to Matter, each with
its icon and one-line idea.

### es_physical_properties.png — "Physical Properties of Matter"
Title "Physical Properties" (navy), subtitle "Observe & measure" (teal). Panels for
each property with an icon: **mass** (balance), **magnetism** (magnet + attracted
objects), **relative density / sink or float** (objects in water), **solubility**
(sugar dissolving in water), **conducts heat or electricity** (metal spoon / wire).
Bottom amber callout: "A physical property can be observed without changing what the
object is made of."

### es_states_of_matter.png — "States of Matter"
Title "States of Matter" (navy), subtitle "Solid · Liquid · Gas" (teal). Three
colored panels with a simple **particle model** in each: SOLID (blue, tightly packed
in a grid — definite shape & volume), LIQUID (teal, close but flowing — takes the
container's shape, definite volume), GAS (violet, spread far apart — fills the
container). A small arrow strip: "heating → particles move more; cooling → particles
slow down." Bottom amber callout: "Heating and cooling can change the state of
matter."

### es_measuring_matter.png — "Measuring Matter"
Title "Measuring Matter" (navy), subtitle "Which tool? Which unit?" (teal). Four
panels pairing a quantity, tool, and unit: **mass** → balance → grams (g);
**volume of a liquid** → graduated cylinder → milliliters (mL); **length** → ruler →
centimeters (cm); **temperature** → thermometer → degrees Celsius (°C). Show reading
each correctly (eye level for the meniscus). Bottom amber callout: "Match the tool
and unit to what you're measuring."

### es_mixtures_solutions.png — "Mixtures & Solutions"
Title "Mixtures & Solutions" (navy), subtitle "Combined, but not changed" (teal).
Two panels: **Mixture** (trail mix / salad bowl — parts keep their own properties and
can be separated) and **Solution** (salt water / lemonade — a mixture that looks the
same throughout, the solute dissolved in the solvent). A small strip of **ways to
separate**: sieve, filter, magnet, evaporation. Bottom amber callout: "In a mixture,
each material keeps its own properties."

## Force, Motion & Energy

### es_force_motion_energy_overview.png — "Force, Motion & Energy — Five Cue Cards"
Overview poster (shared template). Five panels: 1 Forms of Energy · 2 Light Energy ·
3 Electricity & Circuits · 4 Force & Motion · 5 Heat & Thermal Energy.

### es_forms_of_energy.png — "Forms of Energy"
Title "Forms of Energy" (navy), subtitle "Energy is the ability to cause change"
(teal). Five icon panels with an everyday example: **mechanical** (a moving
bicycle), **light** (a lamp/Sun), **sound** (a bell / speaker with waves), **thermal
/ heat** (a stove burner), **electrical** (a plug / battery). Bottom amber callout:
"Energy can change from one form to another."

### es_light_energy.png — "Light Energy"
Title "Light Energy" (navy), subtitle "How light behaves" (teal). A central diagram:
light travels in **straight lines** (rays from the Sun). Three labeled cases:
**reflect** (bounces off a mirror, ray in = ray out), **refract** (bends passing into
water — a straw looks bent), **absorb** (dark surface, ray stops → makes a shadow).
Bottom amber callout: "Light travels in straight lines until something reflects,
bends, or blocks it."

### es_electricity_circuits.png — "Electricity & Circuits"
Title "Electricity & Circuits" (navy), subtitle "Complete the path" (teal). Two
simple circuit diagrams side by side: a **closed circuit** (battery, wires, lit bulb
— "complete path, current flows, bulb lights") and an **open circuit** (a gap /
open switch — "broken path, no flow, bulb off"). A small strip: **conductors** (metal
wire, allow flow) vs. **insulators** (rubber, plastic, wood — stop flow). Bottom
amber callout: "A bulb lights only when the circuit makes a complete loop."

### es_force_and_motion.png — "Force & Motion"
Title "Force & Motion" (navy), subtitle "Pushes & pulls" (teal). Panels: a **push**
and a **pull** changing an object's position/speed/direction; **gravity** (an apple
falling / a ball pulled down); **friction** (a box slowing on a rough surface, arrow
opposing motion); **measuring motion** (start → finish with a ruler/clock, "distance
and time"). Bottom amber callout: "A force can start, stop, speed up, slow down, or
turn an object."

### es_thermal_energy.png — "Heat & Thermal Energy"
Title "Heat & Thermal Energy" (navy), subtitle "Heat moves warmer → cooler" (teal).
Center: a warm object and a cool object with an arrow showing heat flowing from warm
to cool until they even out. Two panels: **conductors** (metal spoon in soup gets hot
fast) vs. **insulators** (wooden spoon, oven mitt, foam cup keep heat in/out). Bottom
amber callout: "Heat always moves from warmer things to cooler things."

## Earth & Space

### es_earth_space_overview.png — "Earth & Space — Five Cue Cards"
Overview poster (shared template). Five panels: 1 The Water Cycle · 2 Weather &
Weather Tools · 3 Rocks, Soil & Fossils · 4 Changing Earth's Surface · 5 Objects in
the Sky (Day/Night, Moon, Solar System).

### es_water_cycle.png — "The Water Cycle"
Title "The Water Cycle" (navy), subtitle "Powered by the Sun" (teal). A classic
labeled **cycle diagram**: Sun heating a lake → **evaporation** (arrows rising) →
**condensation** (clouds forming) → **precipitation** (rain/snow) → **collection /
runoff** (water returning to lakes and rivers), arrows forming a loop. Bottom amber
callout: "The Sun's energy keeps water moving through the cycle again and again."

### es_weather_climate.png — "Weather & Weather Tools"
Title "Weather" (navy), subtitle "Measure it with the right tool" (teal). Icon
panels: **thermometer** (temperature), **rain gauge** (precipitation), **wind vane**
(wind direction), **anemometer** (wind speed), **barometer** (air pressure). Small
strip contrasting **weather** (day to day) vs. **climate** (the usual pattern over a
long time). Bottom amber callout: "Weather is right now; climate is the long-term
pattern."

### es_rocks_soil_fossils.png — "Rocks, Soil & Fossils"
Title "Rocks, Soil & Fossils" (navy), subtitle "Clues from the ground" (teal).
Panels: a **soil-layer cross-section** (topsoil, subsoil, rock) with what soil is
made of; **natural resources** from Earth (water, rock, soil, fuels); a **fossil** in
sedimentary rock layers ("clues about living things from long ago"). Bottom amber
callout: "Fossils in rock layers tell us about the past."

### es_changing_earth.png — "Changing Earth's Surface"
Title "Changing Earth's Surface" (navy), subtitle "Weathering · Erosion ·
Deposition" (teal). Three sequential panels with arrows: **weathering** (rock breaks
into smaller pieces), **erosion** (wind/water carries the pieces away), **deposition**
(the pieces are dropped in a new place, forming sandbars/deltas). A small strip of
**fast vs. slow** changes (earthquake/volcano vs. a canyon carved over time). Bottom
amber callout: "Break it → move it → drop it."

### es_day_night_seasons.png — "Day, Night & Seasons"
Title "Day, Night & Seasons" (navy), subtitle "Earth in motion" (teal). Two panels:
**Rotation** (Earth spinning once a day → the lit side has day, the dark side has
night, ~24 hours) and **Revolution** (Earth orbiting the Sun once a year, with a
tilt → seasons and changing daylight). Bottom amber callout: "Rotation makes day and
night; revolution and tilt make the seasons."

### es_moon_phases.png — "Phases of the Moon"
Title "Phases of the Moon" (navy), subtitle "About a month to cycle" (teal). The
**eight moon phases** in order around a ring as seen from Earth: new, waxing crescent,
first quarter, waxing gibbous, full, waning gibbous, last quarter, waning crescent,
each labeled. Cue: **waxing** = light growing (right side), **waning** = light
shrinking (left side). Bottom amber callout: "The Moon doesn't change shape — we see
different amounts of its lit half."

### es_solar_system.png — "The Solar System"
Title "The Solar System" (navy), subtitle "The Sun and what orbits it" (teal). A
flat diagram of the **Sun** at center with the eight planets on orbit rings, labeled
in order (Mercury → Neptune), the Sun marked "our closest star." A small note: stars
look different in brightness mostly because of **distance**. Bottom amber callout:
"The Sun is a star; planets orbit it, and Earth is the third planet."

## Organisms & Environments

### es_organisms_environments_overview.png — "Organisms & Environments — Five Cue Cards"
Overview poster (shared template). Five panels: 1 Plant Parts & Functions · 2 Life
Cycles · 3 Inherited Traits & Learned Behaviors · 4 Adaptations · 5 Food Chains &
Ecosystems.

### es_plant_parts.png — "Plant Parts & Functions"
Title "Plant Parts & Functions" (navy), subtitle "Each part has a job" (teal). A
labeled flat diagram of a plant with callouts: **roots** (take in water & anchor),
**stem** (carries water & holds the plant up), **leaves** (make food using sunlight),
**flower** (makes seeds to reproduce). Bottom amber callout: "Each structure helps
the plant survive and grow."

### es_life_cycles.png — "Life Cycles"
Title "Life Cycles" (navy), subtitle "How living things grow & change" (teal). Three
labeled cycles: **complete metamorphosis** (butterfly: egg → larva → pupa → adult),
**incomplete metamorphosis** (grasshopper: egg → nymph → adult), and a **plant life
cycle** (seed → seedling → mature plant → flower/seeds), each drawn as a small
arrowed loop. Bottom amber callout: "Living things follow a repeating life cycle."

### es_inherited_learned.png — "Inherited Traits & Learned Behaviors"
Title "Inherited vs. Learned" (navy), subtitle "Passed down or picked up?" (teal).
Two contrasting panels: **Inherited traits** (from parents — eye color, fur color, a
dog's floppy ears, a plant's flower color) vs. **Learned behaviors** (from experience
— a dog doing a trick, riding a bike, a bird taught a song). Bottom amber callout:
"Inherited traits come from parents; learned behaviors come from experience."

### es_adaptations.png — "Adaptations for Survival"
Title "Adaptations" (navy), subtitle "Built to survive" (teal). Panels showing
**structural adaptations** (a cactus's spines & thick stem, a duck's webbed feet, a
polar bear's thick fur) and **behavioral adaptations** (birds migrating, bears
hibernating). Each with a one-line "helps it survive because…". Bottom amber callout:
"Adaptations help an organism survive in its environment."

### es_food_chains_ecosystems.png — "Food Chains & Ecosystems"
Title "Food Chains & Ecosystems" (navy), subtitle "Energy flows from the Sun" (teal).
A **food chain** with arrows showing energy flow: Sun → producer (grass) → consumer
(grasshopper) → consumer (frog) → consumer (snake), with roles labeled **producer,
consumer, decomposer**. A small **food web** inset (several chains linked). Bottom
amber callout: "Arrows point in the direction the energy flows — toward the eater."
