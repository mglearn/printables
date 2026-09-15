# Plan — Math + Elementary-Science Supplemental Aids

Two new collections that mirror the existing `supplemental_aids/` (middle-school
science) pipeline. Scaffolding is committed; the only remaining step is generating
the PNGs from the Codex prompt files, then running the build scripts.

## What was created

```
printables/
  supplemental_aids_math/                 # Middle School Math, grades 6–8 (prefix ma_)
    index.html                            # gallery page (dashboard + lightbox)
    build-manifest.sh                     # curated CATALOG → assets/sa-manifest.js (16 rows)
    build-pdfs.sh                         # each ma_*.png → 2-page PDF (color + B&W)
    build-packets.sh                      # renders packets_src/*.html → *_packet.pdf
    assets/sa-app.js                      # gallery logic (shared design)
    assets/sa-manifest.js                 # GENERATED, already contains all 16 rows
    packets_src/packet.css                # packet stylesheet (for later authoring)
    MATH_IMAGE_PROMPTS.md                 # ← Codex prompts (16 sheets + hero + thumb)

  supplemental_aids_elem_science/         # Elementary Science STAAR, grades 3–5 (prefix es_)
    index.html
    build-manifest.sh                     # 28 rows across the 4 STAAR reporting categories
    build-pdfs.sh / build-packets.sh
    assets/sa-app.js / assets/sa-manifest.js
    packets_src/packet.css
    ELEM_SCIENCE_IMAGE_PROMPTS.md         # ← Codex prompts (28 sheets + hero + thumb)

  index.html                              # home: added Elementary Science card (Science
                                          #   group) + new Math group; total-count → 114
```

## Design decisions (confirmed with the user)

- **Two sibling pages**, not extra groups on the science page — keeps each page
  focused and each collection independently buildable.
- **Math v1 = focused starter set (16 sheets)**; expand later by adding CATALOG rows
  + prompts. Groups: Start here · Reference · Number & Operations · Proportionality ·
  Expressions, Equations & Relationships · Data & Statistics.
- **Elementary science = grades 3–5 spiral (28 sheets)** toward the Grade-5 STAAR;
  groups map to the four reporting categories (Matter & Energy; Force, Motion &
  Energy; Earth & Space; Organisms & Environments) plus Start here + Science Skills.
- **House style** reused verbatim: flat-vector letter-portrait cue cards, navy title
  + teal/violet subtitle, rounded colored panels, numbered badges, teal checkmarks,
  amber "key idea" callout. The STYLE BLOCK in each prompt file enforces this so the
  set matches the existing science sheets.
- **Distinct file prefixes** (`ma_`, `es_`) keep generated images organized and let
  each `build-*.sh` glob only its own collection.

## How to finish (per collection)

1. Generate the PNGs with Codex using the prompt file. Prepend the STYLE BLOCK to
   every per-sheet prompt; save each with the exact filename in its heading (into the
   collection folder; hero → `assets/hero.png`; the two home-page thumbnails →
   `../assets/thumb-math-supplemental-aids.png` and `../assets/thumb-elem-science.png`).
2. `./build-pdfs.sh` — writes a 2-page print PDF (color + grayscale) beside each PNG.
3. `./build-manifest.sh` — refreshes `assets/sa-manifest.js` and auto-links the PDFs
   (and any packets). The page is already wired; images appear as they land.
4. Open `index.html` locally to spot-check the gallery, dashboard, and lightbox.

## Follow-up (optional, not blocking launch)

- **Activity packets** (Retrieve · Apply · ACE · Teacher Key). The science page split
  these from a master PDF; for these collections author one HTML per concept card in
  `packets_src/` (pattern: the science `packets_src/*.html` + `packet.css`), then
  `./build-packets.sh` renders `<base>_packet.pdf`. The manifest links a packet
  automatically once its PDF exists — no page edits needed.
- Bump the concept counts on the home-page cards if the sets grow.

## Notes

- `total-count` on the home page was set to **114** (70 existing + 16 + 28),
  assuming both collections are fully generated. Adjust if you stage the rollout.
- Both pages depend on the shared `printables/assets/styles.css` (already contains
  the `sa-dashboard`, `card`, and lightbox classes) — no CSS changes were needed.
