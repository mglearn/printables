# Texas Grab-and-Go Substitute Packets

Print-and-go substitute lessons a teacher can pick, print, and leave — a full class period with
no prep, no logins, no internet, and ordinary classroom materials. Part of
**[Teacher Printables](../index.html)** (`mglearn.github.io/printables/substitute_packets/`).

Each packet is standards-driven, review-gated, and ships as separate files so the answer key is
never handed to students by accident.

## Status

**In development — building one vertical slice at a time.** The first packet is the Grade 7
Science pilot; the twelve-packet grades 6–8 pilot (one per grade × core subject) follows. See
[`plan.md`](plan.md) for the full development plan, data model, and phased rollout.

> Standards references are **provisional and pending educator verification** against the current
> official Texas Administrative Code. Packets do **not** claim formal alignment or use the phrase
> "TEKS-aligned" until a Texas educator has reviewed them.

## What ships per packet

Every packet folder (e.g. `G07_SCI_ThermalEnergy_01/`) contains:

| File | Audience | Notes |
|------|----------|-------|
| `index.html` | Everyone | Accessible HTML version + the packet's landing page (print buttons, links) |
| `student.html` | Students | Printable student packet — **no answers** |
| `subguide.html` | Substitute | One-to-two-page guide, readable in 5 min, no subject expertise needed |
| `answerkey.html` | Teacher | **Separate** answer key with a CER rubric and misconception notes |
| `manifest.json` | Catalog | Machine-readable record (grade, subject, duration, standards, files, review status) |

Print any `*.html` to PDF (**Print → Save as PDF**, US Letter) for a copier-ready handout.

## The routine (every packet)

`Start → Build → Apply → Explain → ACE close → (optional) Continue`

Students recognize the routine even when the subject changes. Target: ~45–60 minutes, independent
work, pencil and printed packet only.

## Shared styles

`assets/packet.css` is the one print + screen stylesheet for all packets. It sets a restrained
accent per subject (`<body data-subject="rla|math|science|social">`) and is **grayscale-safe** —
meaning never depends on color alone. Reuse its classes rather than adding new visual systems; see
the Grade 7 Science packet for the reference structure.

## Adding a packet

1. Create `Gxx_SUBJ_Topic_NN/` and author `student.html`, `subguide.html`, `answerkey.html`,
   `index.html`, and `manifest.json` against `assets/packet.css`.
2. Keep all content original (or public-domain / openly licensed with attribution in the manifest);
   render required text, labels, formulas, and diagrams as HTML/SVG, never as raster images.
3. Verify each standard against the current official source before removing the `pending` flag.
4. Add a card to this collection's `index.html`, and (for a new collection) a dashboard card in
   `../index.html`.

## Deploy

Push `main` in the `mglearn/printables` repo — GitHub Pages serves it at
`mglearn.github.io/printables/`.

## License

© 2026 TCEA, created by Miguel Guhlin. Content CC BY-NC 4.0 · code MIT. See
[`../licensing.html`](../licensing.html).
