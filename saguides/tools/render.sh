#!/usr/bin/env bash
# Deterministically render every candidate SVG to a print-ready PDF (vector,
# US Letter) and a high-resolution PNG using headless Chrome. No generative step.
# Usage: tools/render.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="$(command -v google-chrome || command -v chromium || true)"
[ -z "$CHROME" ] && { echo "no chrome/chromium found"; exit 1; }

COMMON=(--headless --no-sandbox --disable-gpu --disable-dev-shm-usage --hide-scrollbars)

count=0
while IFS= read -r svg; do
  base="${svg%.svg}"
  # PDF: vector, Letter page, no header/footer
  "$CHROME" "${COMMON[@]}" --no-pdf-header-footer \
    --print-to-pdf="${base}.pdf" "file://${svg}" >/dev/null 2>&1 || echo "PDF fail: $svg"
  # PNG: window matches the 816x1056 SVG box at 2x device scale -> 1632x2112
  "$CHROME" "${COMMON[@]}" --force-device-scale-factor=2 \
    --default-background-color=FFFFFFFF --window-size=816,1056 \
    --screenshot="${base}.png" "file://${svg}" >/dev/null 2>&1 || echo "PNG fail: $svg"
  count=$((count+1))
done < <(find "$ROOT/candidates" -name '*.svg' | sort)
echo "rendered $count aids (PDF + PNG)"
