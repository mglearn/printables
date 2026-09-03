#!/usr/bin/env bash
# Splits the combined activity-packet master (activity_packets_master.pdf) into one
# 4-page packet per concept cue card: sa_<base>_packet.pdf.
# Each concept's packet is 4 consecutive pages in the master, in this order:
#   1) Retrieve It   2) Apply It   3) ACE It   4) Teacher Key
# The overview and the four strand-overview posters have no packet.
# Curated base|first-page table below (last page = first + 3). Run from
# printables/supplemental_aids/.
set -euo pipefail
cd "$(dirname "$0")"

SRC=activity_packets_master.pdf
[ -f "$SRC" ] || { echo "ERROR: $SRC not found." >&2; exit 1; }

# base (matches the sa_<base>.png cue card) | first page in the master
read -r -d '' MAP <<'ROWS' || true
sa_atomic_structure|1
sa_elements_compounds_mixtures|5
sa_metals_nonmetals_metalloids|9
sa_states_of_matter|13
sa_physical_properties|17
sa_chemical_formulas|21
sa_chemical_changes|25
sa_net_force|29
sa_balanced_unbalanced_forces|33
sa_newtons_laws|37
sa_friction_surface_type|41
sa_distance_time_graphs|45
sa_potential_kinetic_energy|49
sa_heat_transfer|53
sa_wave_properties|57
sa_electromagnetic_spectrum|61
sa_plate_boundaries|65
sa_rock_cycle|69
sa_weathering_erosion_deposition|73
sa_weather_water_cycle|77
sa_phases_of_the_moon|81
sa_star_life_cycle|85
sa_cell_structures|89
sa_photosynthesis|93
sa_food_chains_webs|97
sa_ecological_succession|101
ROWS

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
n=0
while IFS='|' read -r base start; do
  [ -n "$base" ] || continue
  end=$((start + 3))
  if [ ! -f "${base}.png" ]; then
    echo "NOTE: ${base}.png not found on disk (packet still built)." >&2
  fi
  pdfseparate -f "$start" -l "$end" "$SRC" "$tmp/pg-%d.pdf"
  pdfunite "$tmp/pg-${start}.pdf" "$tmp/pg-$((start+1)).pdf" "$tmp/pg-$((start+2)).pdf" "$tmp/pg-${end}.pdf" "${base}_packet.pdf"
  rm -f "$tmp"/pg-*.pdf
  n=$((n+1))
done <<< "$MAP"

echo "Activity packets generated: $n (4 pages each)"
