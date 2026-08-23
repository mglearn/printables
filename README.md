# Teachers Give Teachers (TGT)

A space where teachers freely share ideas and creations — the "give one, take one"
answer to Teachers Pay Teachers. Everything here is free to download, print, and adapt.

**Live site:** https://mglearn.github.io/tgt/

## Structure

```
tgt/
  index.html            Hub dashboard — cards for each collection
  assets/
    styles.css          Shared styles (dashboard + galleries)
    thumb-srf.png        Dashboard card thumbnails
    thumb-gtky.png
  srf/                  Student Refusal Forms collection
    index.html          Gallery of the forms
    research.html       The reflection/ACE/Visible Learning writeup
    assets/
      srf-app.js        Gallery logic (vanilla JS)
      srf-manifest.js   AUTO-GENERATED — do not edit by hand
    build-manifest.sh   Regenerates the manifest from the PNGs + curated titles
    build-pdfs.sh       Makes a print-ready 2-page PDF next to each PNG
    srf_*.png / *.pdf   The forms (color PNG + 2-page print PDF)
```

The **Getting to Know You** card links out to its own repo/site at
`mglearn.github.io/gtky`.

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

## Deploy

GitHub Pages serves this repo as a project site at `mglearn.github.io/tgt`
(Deploy from branch → `main` / root). Push to `main` to publish.

## License

Resources © Miguel Guhlin, licensed
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
