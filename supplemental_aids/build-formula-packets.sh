#!/usr/bin/env bash
# Renders each formula-triangle activity packet in packets_src/*.html to a 4-page
# print PDF (sa_<base>_packet.pdf) via headless Chrome. These packets are authored
# here (not split from activity_packets_master.pdf like the others). Run from
# printables/supplemental_aids/.
set -euo pipefail
cd "$(dirname "$0")"

CHROME=$(command -v google-chrome || command -v chromium || command -v chromium-browser || true)
[ -n "$CHROME" ] || { echo "ERROR: no Chrome/Chromium found." >&2; exit 1; }

made=0
for html in packets_src/*.html; do
  [ -e "$html" ] || continue
  base=$(basename "$html" .html)
  out="${base}_packet.pdf"
  "$CHROME" --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="$out" "file://$PWD/$html" >/dev/null 2>&1
  pages=$(pdfinfo "$out" 2>/dev/null | awk '/Pages/{print $2}')
  if [ "$pages" != 4 ]; then
    echo "WARNING: $out rendered $pages pages (expected 4) — check content length in $html" >&2
  fi
  made=$((made+1))
done
echo "Formula-triangle packets rendered: $made"
