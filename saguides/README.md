# STAAR Supplemental Aid Candidate Library

A library of paper-based science and mathematics **supplemental-aid candidates**
designed to follow current Texas Education Agency (TEA) requirements for STAAR
supplemental aids. It is built from the existing classroom **Visual Cue Cards**
(science and math) as source material — but the cue cards are **not** reformatted.
Each source resource is analyzed and rebuilt **only** when its underlying concept
can be represented with a type of supplemental aid currently permitted by TEA. The
original cue cards remain available as classroom/review resources.

> **These resources are designed to follow current Texas Education Agency guidance
> for locally created STAAR supplemental aids. TEA does not review or approve
> locally created supplemental aids. A resource's inclusion in this library does
> not make it automatically allowable for a particular student. Eligibility,
> routine use, documentation, individualization, and local testing procedures must
> still be reviewed before state assessment use.**

Preferred wording for any candidate:

> Designed to follow current TEA supplemental-aid guidance. Final student
> eligibility and use remain subject to current TEA requirements and local testing
> procedures.

These resources are **never** described as TEA approved, STAAR approved, TEA
certified, guaranteed compliant, or automatically allowable during STAAR.

---

## Two clearly different libraries

| Classroom Visual Cue Cards | STAAR Supplemental Aid Candidates (this library) |
|---|---|
| Rich instructional resources | Minimal resources rebuilt around current TEA restrictions |
| May contain vocabulary, definitions, labels, explanations, formulas, examples, color coding, mnemonics, procedures | Contain only what current guidance permits for their specific aid type |
| For teaching, intervention, retrieval practice, review | Candidate paper aids for eligible students who already use them routinely |

The classroom cue cards live at `printables/supplemental_aids/`,
`printables/supplemental_aids_elem_science/`, `printables/supplemental_aids_math/`,
and `printables/supplemental_aids_elem_math/`. Do not confuse the two.

## What a supplemental aid is (and is not)

A STAAR supplemental aid is a **paper-based resource that helps an eligible student
independently recall information**. It is **not** a mini-textbook, a vocabulary or
formula sheet, a worked example, directions, a test-taking strategy, a
step-by-step guide, or a packet automatically given to every student.

## Permitted aid categories used here

`mnemonic`, `blank_graphic_organizer`, `math_number_chart`,
`math_place_value_chart`, `math_fraction_model`, `math_geometry_2d`,
`math_geometry_3d`, `science_graphic`, `science_formula_triangle`.

Per section 7, **no mathematics formula sheets or formula triangles** are created.
Per section 10, a science formula triangle is created **only** when the relationship
appears on the current state-supplied science reference materials — in this build
that is Density, Average speed, Net force, and Work (STAAR Grade 8 science). Weight,
momentum, pressure, power, wave speed, and Ohm's law are **classroom-use-only**
because they are not on that sheet (fail-closed).

## Individualization (section 19)

> Select only the supplemental aid or small set of aids that the individual student
> routinely, independently, and effectively uses during instruction and classroom
> testing. Do not automatically provide every student with the same collection.

There is deliberately **no** "complete STAAR packet." The master library is for
educator selection; each aid is a separate one-page file.

## Student aids vs. the master library (section 4)

- **Student-facing aid files** (`candidates/**`) contain **no** titles, TEKS codes,
  instructions, explanations, branding, URLs, copyright text, teacher notes, or the
  words "STAAR Supplemental Aid." The filename may describe the aid even though the
  printed page has no such words.
- **The teacher master library** (`teacher-guide/`, `compliance-matrix.md`) carries
  all of that descriptive metadata and is **not** itself a student testing aid. It
  is marked *TEACHER REFERENCE — NOT A STUDENT TESTING AID*.

## Folder structure

```
saguides/
├── README.md                 ← this file (disclaimer, rules)
├── compliance-matrix.md      ← per-resource status (section 16)
├── qa-checklist.md           ← human QA (section 15)
├── sources/                  ← TEA source + reference-material logs (section 1)
├── originals/                ← pointer to the classroom cue-card sources
├── candidates/               ← student-facing aids (SVG + PDF + PNG), by subject/grade
├── classroom-only/           ← where ambiguous items are retired to (section 11)
└── teacher-guide/            ← teacher catalog (index.html) + data
```

## Reproducing the build

Everything is deterministic (no generative imagery on any test-use aid, section 13):

```bash
python3 tools/generate_aids.py     # write all candidate SVGs + aids.json
python3 tools/lint_aids.py         # aid-type linter (section 14) — must pass
bash    tools/render.sh            # SVG -> print-ready PDF + high-res PNG (headless Chrome)
python3 tools/build_catalog.py     # compliance-matrix.md + teacher-guide/catalog-data.js
```

Update the review date in one place: `REVIEW_DATE` in `tools/build_catalog.py`
(and re-run it). See `sources/` before every major revision (section 25): never
assume last year's TEA rules are unchanged.

## Status vocabulary

`CANDIDATE` · `CLASSROOM USE ONLY` · `NEEDS TEA/LOCAL VERIFICATION` · `RETIRED` ·
`LOCAL REVIEW COMPLETE`. The value **`TEA APPROVED` is never used.**

**Testing guidance reviewed: September 2026.** This does not imply the library
remains current after that date.
