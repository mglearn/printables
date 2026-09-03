# Teacher Printables

A space where teachers freely share ideas and creations — the "give one, take one"
answer to Teachers Pay Teachers. Everything here is free to download, print, and adapt.

**Live site:** https://mglearn.github.io/printables/

## Structure

```
printables/
  index.html            Hub dashboard — cards for each collection
  assets/
    styles.css          Shared styles (dashboard + galleries)
    thumb-srf.png        Dashboard card thumbnails
    thumb-gtky.png
    thumb-case-files.png
    thumb-phase-change.png
  srf/                  Student Refusal Forms collection
    index.html          Gallery of the forms
    research.html       The reflection/ACE/Visible Learning writeup
    assets/
      srf-app.js        Gallery logic (vanilla JS)
      srf-manifest.js   AUTO-GENERATED — do not edit by hand
    build-manifest.sh   Regenerates the manifest from the PNGs + curated titles
    build-pdfs.sh       Makes a print-ready 2-page PDF next to each PNG
    srf_*.png / *.pdf   The forms (color PNG + 2-page print PDF)
  phase_change_stations/  Phase Change Station Lab collection
    index.html          Gallery of the seven stations (lab order, no categories)
    assets/
      pcs-app.js        Gallery logic (vanilla JS)
      pcs-manifest.js   AUTO-GENERATED — do not edit by hand
    build-manifest.sh   Regenerates the manifest (title, transition, focus question)
    build-pdfs.sh       Makes a print-ready 2-page PDF next to each PNG
    pcs_*.png / *.pdf   The station sheets (color PNG + 2-page print PDF)
  supplemental_aids/    Science Supplemental Aids collection
    index.html          Gallery of the strand sheets (flat list, no categories)
    assets/
      sa-app.js         Gallery logic (vanilla JS)
      sa-manifest.js    AUTO-GENERATED — do not edit by hand
    build-manifest.sh   Regenerates the manifest (strand, title, blurb, packet)
    build-pdfs.sh       Makes a print-ready 2-page PDF next to each PNG
    build-packets.sh    Splits activity_packets_master.pdf into per-card packets
    activity_packets_master.pdf   Combined 4-page-per-concept activity packets
    sa_*.png / *.pdf    The strand sheets (color PNG + 2-page print PDF)
    sa_*_packet.pdf     4-page activity packet per concept card (Retrieve/Apply/ACE/key)
```

The dashboard groups the cards into a **Science** section (Phase Change Station
Lab, Science Supplemental Aids, CER & ACE Case Files) and a **Classroom
Management** section (Student Refusal Forms, Getting to Know You).

The **Getting to Know You** card links out to its own repo/site at
`mglearn.github.io/gtky`. The **CER & ACE Case Files** card links out to the
Learning Activities Hub at `mglearn.github.io/activities/science/case-files/`.

## Adding or updating Student Refusal Forms

1. Drop the new `srf_*.png` into `srf/`.
2. Add a row to the `CATALOG` in `srf/build-manifest.sh` (base name, category,
   subject, exact title — the title comes from the artwork, not the filename).
3. From `srf/`, run:
   ```bash
   ./build-pdfs.sh        # 2-page PDF (color + B&W print page) per PNG
   ./build-manifest.sh    # regenerates assets/srf-manifest.js
   ```
   Both scripts warn if a PNG is missing from the catalog (or vice-versa).

## Adding or updating Phase Change stations

1. Drop the new `pcs_*.png` into `phase_change_stations/`.
2. Add a row to the `CATALOG` in `phase_change_stations/build-manifest.sh` (base
   name, station number, phase-change transition, exact title, focus question —
   all curated from the artwork). Row order is the gallery display order.
3. From `phase_change_stations/`, run:
   ```bash
   ./build-pdfs.sh        # 2-page PDF (color + B&W print page) per PNG
   ./build-manifest.sh    # regenerates assets/pcs-manifest.js
   ```
   Both scripts warn if a PNG is missing from the catalog (or vice-versa).

## Adding or updating Supplemental Aids

1. Drop the new `sa_*.png` into `supplemental_aids/`.
2. Add a row to the `CATALOG` in `supplemental_aids/build-manifest.sh` (base name,
   TEKS strand, exact title, and a short "what's on it" blurb — all curated from
   the artwork). Row order is the gallery display order.
3. From `supplemental_aids/`, run:
   ```bash
   ./build-pdfs.sh        # 2-page PDF (color + B&W print page) per PNG
   ./build-packets.sh     # splits activity_packets_master.pdf into sa_*_packet.pdf
   ./build-manifest.sh    # regenerates assets/sa-manifest.js (picks up pdf + packet)
   ```
   Both scripts warn if a PNG is missing from the catalog (or vice-versa).

Each concept card also offers a 4-page **activity packet** (Retrieve · Apply · ACE
· teacher key). The packets live combined in `activity_packets_master.pdf`
(4 pages per concept, grouped by strand); `build-packets.sh` splits them into one
`sa_<base>_packet.pdf` per card via the base→first-page table it carries. The
manifest auto-includes a packet whenever `sa_<base>_packet.pdf` exists, so the
overview and the four strand-overview posters simply have none. To revise a
packet, replace the master PDF and re-run `build-packets.sh` then
`build-manifest.sh`.

## Deploy

GitHub Pages serves this repo as a project site at `mglearn.github.io/printables`
(Deploy from branch → `main` / root). Push to `main` to publish. The old
`mglearn.github.io/tgt/` path is served by a separate redirect-stub repo
(`mglearn/tgt`) that forwards to the matching `/printables/…` path.

## License & provenance

© 2026 TCEA, created by Miguel Guhlin. **Content** is licensed
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/); **code** is MIT.
The authoritative statement — reuse terms, attribution, provenance, and privacy —
lives at [`licensing.html`](licensing.html) (`mglearn.github.io/printables/licensing.html`),
surfaced on every page by the quiet one-line footer that `licensing-footer.js` injects.
