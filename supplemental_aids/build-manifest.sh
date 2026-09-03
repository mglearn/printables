#!/usr/bin/env bash
# Regenerates assets/sa-manifest.js by scanning the Supplemental Aids PNGs in this
# folder. Titles, the TEKS strand, and the "what's on it" blurb are curated here
# (they come from the artwork, not the filename), so add a row to CATALOG when you
# drop in a new sheet. Run from printables/supplemental_aids/.
set -euo pipefail
cd "$(dirname "$0")"

# base|strand|title|blurb
# The gallery groups sheets under the strand headings below, in this order.
# Each strand leads with its one-page "five cue cards" overview poster, followed by
# the individual concept cue cards.
read -r -d '' CATALOG <<'ROWS' || true
sa_overview|Start here|All Four Strands — Overview|A one-page map of the collection: the four science strands and the cue cards inside each.
sa_matter_and_energy|Matter & Energy|Matter & Energy — Five Cue Cards|States of matter, evidence of chemical change (GTPC), physical vs. chemical change, particle motion, and conservation of mass.
sa_atomic_structure|Matter & Energy|Atomic Structure|Protons (positive, in the nucleus), neutrons (no charge, in the nucleus), and electrons (negative, outside the nucleus).
sa_elements_compounds_mixtures|Matter & Energy|Elements, Compounds & Mixtures|How particles are grouped — one kind of atom, elements chemically bonded, or substances mixed but not bonded.
sa_metals_nonmetals_metalloids|Matter & Energy|Metals, Nonmetals & Metalloids|Compare properties — shiny conductors, dull brittle nonmetals, and in-between metalloids along the periodic table's stair-step.
sa_states_of_matter|Matter & Energy|States of Matter|Particle-model quick cue for solid, liquid, and gas — shape, volume, and how more space means more motion.
sa_physical_properties|Matter & Energy|Physical Properties of Matter|Mass, volume, density, solubility, conductivity, and magnetism — observed or measured without changing the substance's identity.
sa_chemical_formulas|Matter & Energy|Chemical Formulas|Count the atoms — a subscript counts one element; a coefficient multiplies the whole formula.
sa_chemical_changes|Matter & Energy|Chemical Changes|Four signs a reaction happened — color change, gas forms, a precipitate forms, and temperature or light change.
sa_force_motion_energy|Force, Motion & Energy|Force, Motion & Energy — Five Cue Cards|Average-speed and force formula triangles, Newton's three laws, heat transfer, and wave properties.
sa_net_force|Force, Motion & Energy|Net Force|Add forces in the same direction, subtract opposite directions — the net force is the overall push or pull.
sa_balanced_unbalanced_forces|Force, Motion & Energy|Balanced & Unbalanced Forces|Balanced forces cancel and motion doesn't change; unbalanced forces have a winning direction and motion changes.
sa_newtons_laws|Force, Motion & Energy|Newton's Laws of Motion|Quick cues for the three laws — inertia, F = m × a, and action–reaction.
sa_friction_surface_type|Force, Motion & Energy|Friction & Surface Type|Smooth surfaces mean less friction, rough surfaces mean more — friction acts opposite the direction of motion.
sa_distance_time_graphs|Force, Motion & Energy|Distance-Time Graphs|Read motion from the slope — flat means stopped, sloped means constant speed, steeper means faster.
sa_potential_kinetic_energy|Force, Motion & Energy|Potential & Kinetic Energy|Stored energy of position versus energy of motion — higher position means more gravitational potential energy.
sa_heat_transfer|Force, Motion & Energy|Heat Transfer|Conduction, convection, and radiation — how heat moves from warmer to cooler areas.
sa_wave_properties|Force, Motion & Energy|Wave Properties|Amplitude, wavelength, and frequency on a transverse wave — higher frequency means shorter wavelength.
sa_electromagnetic_spectrum|Force, Motion & Energy|Electromagnetic Spectrum|Radio to gamma by wavelength, frequency, and energy — visible light is a small part of the spectrum.
sa_earth_and_space|Earth & Space|Earth & Space — Five Cue Cards|Plate boundaries, rock layers and fossils, weather systems, the star life cycle, and galaxy types.
sa_plate_boundaries|Earth & Space|Plate Boundaries|Earth's moving crust — divergent, convergent, and transform boundaries and what each one forms.
sa_rock_cycle|Earth & Space|The Rock Cycle|How igneous, sedimentary, and metamorphic rock change over time through Earth's processes.
sa_weathering_erosion_deposition|Earth & Space|Weathering, Erosion & Deposition|How Earth's surface changes — weathering breaks it, erosion moves it, deposition drops it.
sa_weather_water_cycle|Earth & Space|Weather Systems & the Water Cycle|The Sun-powered water cycle — evaporation, condensation, precipitation, runoff, and collection.
sa_phases_of_the_moon|Earth & Space|Phases of the Moon|The eight moon phases as seen from Earth, with waxing (growing light) vs. waning (shrinking light).
sa_star_life_cycle|Earth & Space|Star Life Cycle|From nebula to white dwarf, neutron star, or black hole — a star's mass determines its path.
sa_organisms_environments|Organisms & Environments|Organisms & Environments — Five Cue Cards|Plant and animal cells, cell structures, photosynthesis, ecological succession, and food chains and webs.
sa_cell_structures|Organisms & Environments|Cell Structures|Mnemonic and picture guide (MWNRCMCV) for eight key cell parts and what each one does.
sa_photosynthesis|Organisms & Environments|Photosynthesis|The big idea — sunlight, carbon dioxide, and water become glucose and oxygen (6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂).
sa_food_chains_webs|Organisms & Environments|Food Chains & Food Webs|How energy flows — a single food-chain path versus a food web of many connected chains.
sa_ecological_succession|Organisms & Environments|Ecological Succession|How ecosystems change over time from bare rock to mature forest, with biodiversity increasing.
ROWS

esc() { printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g'; }

out=assets/sa-manifest.js
n=0
{
  echo "/* AUTO-GENERATED by build-manifest.sh — do not edit by hand. */"
  echo "window.SA_MANIFEST = ["
  while IFS='|' read -r base strand title blurb; do
    [ -n "$base" ] || continue
    png="${base}.png"
    if [ ! -f "$png" ]; then
      echo "  WARNING: $png listed in CATALOG but not found on disk" >&2
      continue
    fi
    pdf="${base}.pdf"
    pdfval=""
    [ -f "$pdf" ] && pdfval="$pdf"
    # Optional 4-page activity packet (built by build-packets.sh); concept cards
    # have one, the overview and strand-overview posters do not.
    packet="${base}_packet.pdf"
    packetval=""
    [ -f "$packet" ] && packetval="$packet"
    printf '  { "strand": "%s", "title": "%s", "blurb": "%s", "file": "%s", "pdf": "%s", "packet": "%s" },\n' \
      "$(esc "$strand")" "$(esc "$title")" "$(esc "$blurb")" "$png" "$pdfval" "$packetval"
    n=$((n+1))
  done <<< "$CATALOG"
  echo "];"
} > "$out"

# Flag any PNG on disk that is missing from the CATALOG.
for png in sa_*.png; do
  [ -e "$png" ] || continue
  base="${png%.png}"
  grep -q "^${base}|" <<< "$CATALOG" || echo "NOTE: $png is on disk but not in CATALOG (add a row)." >&2
done

echo "Wrote $out ($n entries)"
