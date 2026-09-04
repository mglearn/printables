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

As of the last run: **44 verified, 4 code-verified, 0 pending** across 48 records
(grades 5–8, all four core subjects).

## Important caveat
Code verification is **not** the same as the plan's human *alignment* review. A
Texas educator should still confirm that each packet's task performs the verb in
its cited expectation before high-stakes use. Re-verify against the official source
before each release and update `verified_on`.
