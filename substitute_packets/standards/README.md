# Standards lock

Single source of truth for the TEKS student expectations the packets cite.

## Files
- `standards-lock.json` — one record per cited SE. Each has the display code, a
  canonical code (with TAC section), subject, grade, strand, **exact official
  wording** (`student_expectation`, when `status: "verified"`), a plain-language
  `focus`, `source_url`, `verified_on`, and `status`. A `packet_map` lists the
  display codes per packet id.
- `schemas/standard.schema.json` — the record schema.
- `validate.mjs` — checks every record against the schema and cross-checks that
  each manifest's cited code exists in the lock. `node standards/validate.mjs`.
- `apply-lock.mjs` — rewrites each packet manifest's `standards.primary` from the
  lock (matching by subject + code, since display codes like `6.6C` collide across
  subjects). `node standards/apply-lock.mjs`, then re-run `node build-catalog.mjs`.

## Status values
- **verified** — code confirmed *and* exact official wording quoted from the
  `source_url` (Cornell LII / 19 Tex. Admin. Code for RLA, math, social studies;
  teksguide.org for the 2021 science TEKS).
- **code-verified** — the code/grade/subject/strand are confirmed against a cited
  source, but the exact official wording has not been transcribed into the record.
- **pending** — not yet confirmed (none currently).

As of the last run: **106 verified, 4 code-verified, 0 pending** across 110 records
(grades 3–8 in all four core subjects, plus **16 high-school courses**: English I–IV,
Algebra I, Geometry, Algebra II, Biology, IPC, Chemistry, Physics, World Geography,
World History, U.S. Government, U.S. History, and Economics). High-school records
carry `course`/`course_id` and `grade: null`. Verification caught **repealed**
sections that must not be cited: Biology's old §112.34 → active **§112.42**, and the
2017 high-school science sections (§§112.31–112.39) → the 2020 set (**IPC §112.44,
Chemistry §112.43, Physics §112.45**). Always re-verify against the official source
before a release.

## Important caveat
Code verification is **not** the same as the plan's human *alignment* review. A
Texas educator should still confirm that each packet's task performs the verb in
its cited expectation before high-stakes use. Re-verify against the official source
before each release and update `verified_on`.
