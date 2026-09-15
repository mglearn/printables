#!/usr/bin/env bash
# Regenerates assets/sa-manifest.js by reading the curated CATALOG below (titles,
# group, and the "what's on it" blurb come from the intended artwork, not the
# filename). Add a row when you plan/drop in a new sheet. Run from
# printables/supplemental_aids_elem_science/.
#
# Emits a row for every CATALOG entry even before its PNG exists, so the gallery
# page is fully wired while you generate the images with Codex (missing PNGs simply
# 404 until produced). It notes which are still missing. .pdf and _packet.pdf links
# are added only once those files exist.
#
# Groups map to the four Grade-5 Science STAAR reporting categories, spanning the
# grades 3–5 TEKS (an elementary spiral toward the tested grade).
set -euo pipefail
cd "$(dirname "$0")"

# base|group|title|blurb
read -r -d '' CATALOG <<'ROWS' || true
es_overview|Start here|Grades 3–5 Science — Overview|A one-page map of the collection: the four STAAR reporting categories and the cue cards inside each.
es_science_tools_safety|Science Skills|Science Tools & Safety|Match the tool to the job — hand lens, balance, graduated cylinder, thermometer, ruler — plus lab-safety reminders.
es_investigation_evidence|Science Skills|Investigation & Evidence|The cycle of a fair test — ask, predict, observe, measure, record, and explain from the evidence you collect.
es_matter_energy_overview|Matter & Energy|Matter & Energy — Five Cue Cards|Physical properties, states of matter, measuring matter, mixtures and solutions, and changes to matter.
es_physical_properties|Matter & Energy|Physical Properties of Matter|Observe and measure — mass, magnetism, relative density (sink or float), solubility, and the ability to conduct heat or electricity.
es_states_of_matter|Matter & Energy|States of Matter|Solid, liquid, and gas as a simple particle model — shape and volume, and how heating or cooling changes state.
es_measuring_matter|Matter & Energy|Measuring Matter|Which tool and unit — mass on a balance (g), volume in a graduated cylinder (mL), length with a ruler (cm), temperature (°C).
es_mixtures_solutions|Matter & Energy|Mixtures & Solutions|A mixture combines materials that keep their properties; a solution is a mixture that looks the same throughout; ways to separate them.
es_force_motion_energy_overview|Force, Motion & Energy|Force, Motion & Energy — Five Cue Cards|Forms of energy, light, electricity and circuits, force and motion, and heat/thermal energy.
es_forms_of_energy|Force, Motion & Energy|Forms of Energy|Mechanical, light, sound, thermal (heat), and electrical energy — with an everyday example of each.
es_light_energy|Force, Motion & Energy|Light Energy|Light travels in straight lines and can reflect (bounce), refract (bend), or be absorbed — shadows and mirrors.
es_electricity_circuits|Force, Motion & Energy|Electricity & Circuits|A complete (closed) circuit lets current flow; open circuits stop it — conductors vs. insulators.
es_force_and_motion|Force, Motion & Energy|Force & Motion|Pushes and pulls change position, speed, or direction — gravity, friction, and measuring motion.
es_thermal_energy|Force, Motion & Energy|Heat & Thermal Energy|Heat moves from warmer to cooler; some materials conduct heat well (metals) and some insulate — everyday examples.
es_earth_space_overview|Earth & Space|Earth & Space — Five Cue Cards|The water cycle, weather, rocks/soil/fossils, changes to Earth's surface, and objects in the sky.
es_water_cycle|Earth & Space|The Water Cycle|Sun-powered — evaporation, condensation, precipitation, and collection move water around Earth again and again.
es_weather_climate|Earth & Space|Weather & Weather Tools|Measure weather with the right instrument — thermometer, rain gauge, wind vane, anemometer — and weather vs. climate.
es_rocks_soil_fossils|Earth & Space|Rocks, Soil & Fossils|How soil forms in layers, natural resources, and how fossils in sedimentary rock give clues about the past.
es_changing_earth|Earth & Space|Changing Earth's Surface|Slow and fast changes — weathering breaks it down, erosion carries it away, and deposition drops it somewhere new.
es_day_night_seasons|Earth & Space|Day, Night & Seasons|Earth's rotation makes day and night; its year-long orbit and tilt bring the seasons and changing daylight.
es_moon_phases|Earth & Space|Phases of the Moon|The Moon's changing appearance over about a month — waxing (growing) and waning (shrinking) as it orbits Earth.
es_solar_system|Earth & Space|The Solar System|The Sun as our closest star, the planets that orbit it, and how stars differ in brightness because of distance.
es_organisms_environments_overview|Organisms & Environments|Organisms & Environments — Five Cue Cards|Plant parts, life cycles, inherited traits vs. learned behaviors, adaptations, and food chains and ecosystems.
es_plant_parts|Organisms & Environments|Plant Parts & Functions|Roots, stem, leaves, and flower — the job each structure does to help a plant get water, light, and reproduce.
es_life_cycles|Organisms & Environments|Life Cycles|How living things grow and change — complete vs. incomplete metamorphosis, and the plant life cycle.
es_inherited_learned|Organisms & Environments|Inherited Traits & Learned Behaviors|Traits passed from parents versus behaviors learned from experience — how to tell them apart.
es_adaptations|Organisms & Environments|Adaptations for Survival|Structural and behavioral adaptations that help organisms survive in their environment — examples from several habitats.
es_food_chains_ecosystems|Organisms & Environments|Food Chains & Ecosystems|Energy flows from the Sun through producers, consumers, and decomposers — food chains, food webs, and dependence.
ROWS

esc() { printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g'; }

out=assets/sa-manifest.js
n=0; missing=0
{
  echo "/* AUTO-GENERATED by build-manifest.sh — do not edit by hand. */"
  echo "window.ES_MANIFEST = ["
  while IFS='|' read -r base group title blurb; do
    [ -n "$base" ] || continue
    png="${base}.png"
    [ -f "$png" ] || { echo "NOTE: $png not generated yet (row skipped)." >&2; missing=$((missing+1)); continue; }
    pdf="${base}.pdf";        pdfval="";    [ -f "$pdf" ]    && pdfval="$pdf"
    packet="${base}_packet.pdf"; packetval=""; [ -f "$packet" ] && packetval="$packet"
    printf '  { "strand": "%s", "title": "%s", "blurb": "%s", "file": "%s", "pdf": "%s", "packet": "%s" },\n' \
      "$(esc "$group")" "$(esc "$title")" "$(esc "$blurb")" "$png" "$pdfval" "$packetval"
    n=$((n+1))
  done <<< "$CATALOG"
  echo "];"
} > "$out"

for png in es_*.png; do
  [ -e "$png" ] || continue
  base="${png%.png}"
  grep -q "^${base}|" <<< "$CATALOG" || echo "NOTE: $png is on disk but not in CATALOG (add a row)." >&2
done

echo "Wrote $out ($n entries, $missing image(s) not yet generated)"
