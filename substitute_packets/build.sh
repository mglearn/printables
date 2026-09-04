#!/usr/bin/env bash
# Texas Grab-and-Go Substitute Packets — build all outputs.
# For each Gxx_* packet: render Student / SubGuide / AnswerKey PDFs, assemble a
# TeacherMaster (guide + student + divider + key), make a Preview.webp, then
# regenerate catalog.json/csv and the per-grade / per-subject / all bulk ZIPs.
# Deterministic and safe to re-run. Requires: google-chrome, pdfunite, pdftoppm, cwebp, zip, node.
set -euo pipefail
cd "$(dirname "$0")"
ROOT="$PWD"
CHROME="${CHROME:-google-chrome}"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

render() { # in.html out.pdf
  "$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
    --virtual-time-budget=6000 --print-to-pdf="$2" "file://$ROOT/$1" >/dev/null 2>&1
}

echo "→ divider"; render assets/divider.html "$TMP/divider.pdf"

shopt -s nullglob
built=0
for dir in G[0-9][0-9]_*/ HS_*/; do
  id="${dir%/}"
  [ -f "$dir/student.html" ] || { echo "  skip $id (no student.html)"; continue; }
  echo "→ $id"
  render "$dir/student.html"   "$dir/${id}_Student.pdf"
  render "$dir/subguide.html"  "$dir/${id}_SubGuide.pdf"
  render "$dir/answerkey.html" "$dir/${id}_AnswerKey.pdf"
  pdfunite "$dir/${id}_SubGuide.pdf" "$dir/${id}_Student.pdf" "$TMP/divider.pdf" "$dir/${id}_AnswerKey.pdf" "$dir/${id}_TeacherMaster.pdf"
  pdftoppm -png -singlefile -r 96 "$dir/${id}_Student.pdf" "$TMP/prev" >/dev/null 2>&1
  cwebp -quiet -q 82 "$TMP/prev.png" -o "$dir/${id}_Preview.webp" >/dev/null 2>&1
  built=$((built+1))
done
echo "built $built packets"

echo "→ catalog"; node build-catalog.mjs

echo "→ bulk zips"
mkdir -p dist
zipset() { # out.zip  glob...
  local out="$1"; shift
  rm -f "dist/$out"
  local files=(); for g in "$@"; do for f in $g; do [ -e "$f" ] && files+=("$f"); done; done
  [ ${#files[@]} -gt 0 ] && zip -qj "dist/$out" "${files[@]}" && echo "  dist/$out (${#files[@]} files)"
}
for g in 03 04 05 06 07 08; do zipset "grade-${g}-packets.zip" "G${g}_*/*_Student.pdf" "G${g}_*/*_SubGuide.pdf" "G${g}_*/*_AnswerKey.pdf"; done
zipset "highschool-packets.zip" "HS_*/*_Student.pdf" "HS_*/*_SubGuide.pdf" "HS_*/*_AnswerKey.pdf"
# subject bundles (HS folders are named by course, so add them explicitly per subject)
zipset "subject-rla-packets.zip"  "G[0-9][0-9]_RLA_*/*_Student.pdf" "G[0-9][0-9]_RLA_*/*_SubGuide.pdf" "G[0-9][0-9]_RLA_*/*_AnswerKey.pdf" "HS_ENG*/*_Student.pdf" "HS_ENG*/*_SubGuide.pdf" "HS_ENG*/*_AnswerKey.pdf"
zipset "subject-math-packets.zip" "G[0-9][0-9]_MATH_*/*_Student.pdf" "G[0-9][0-9]_MATH_*/*_SubGuide.pdf" "G[0-9][0-9]_MATH_*/*_AnswerKey.pdf" "HS_ALG*/*_Student.pdf" "HS_ALG*/*_SubGuide.pdf" "HS_ALG*/*_AnswerKey.pdf"
zipset "subject-sci-packets.zip"  "G[0-9][0-9]_SCI_*/*_Student.pdf" "G[0-9][0-9]_SCI_*/*_SubGuide.pdf" "G[0-9][0-9]_SCI_*/*_AnswerKey.pdf" "HS_BIO*/*_Student.pdf" "HS_BIO*/*_SubGuide.pdf" "HS_BIO*/*_AnswerKey.pdf"
zipset "subject-soc-packets.zip"  "G[0-9][0-9]_SOC_*/*_Student.pdf" "G[0-9][0-9]_SOC_*/*_SubGuide.pdf" "G[0-9][0-9]_SOC_*/*_AnswerKey.pdf" "HS_USH*/*_Student.pdf" "HS_USH*/*_SubGuide.pdf" "HS_USH*/*_AnswerKey.pdf"
zipset "all-packets.zip" "G[0-9][0-9]_*/*_Student.pdf" "G[0-9][0-9]_*/*_SubGuide.pdf" "G[0-9][0-9]_*/*_AnswerKey.pdf" "G[0-9][0-9]_*/*_TeacherMaster.pdf" "HS_*/*_Student.pdf" "HS_*/*_SubGuide.pdf" "HS_*/*_AnswerKey.pdf" "HS_*/*_TeacherMaster.pdf"

echo "done."
