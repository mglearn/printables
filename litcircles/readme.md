# Literature Circles Launch Kit — Reference Guide

> Internal reference for the `printables/litcircles/` collection. Not linked from
> any page — kept here so the design, contents, and workflows are documented in one
> place. (The build/sources file is the separate `README.md`; this file is the
> feature-and-capability overview.)

**Live:** https://mglearn.github.io/printables/litcircles/
**Repo:** https://github.com/mglearn/printables (`litcircles/`)
**Audience:** Texas ELAR/ELA teachers, grades 5–12
**License:** Original content CC BY-NC 4.0 · code MIT · © 2026 TCEA, created by Miguel Guhlin. Public-domain texts retain that status; copyrighted titles remain © their owners.

---

## 1. What this collection is

A print-and-go system for running **literature circles** (small-group, student-led
reading discussions) in grades 5–12, aligned to the Texas Essential Knowledge and
Skills (TEKS) for ELAR. It has three layers:

1. **The Launch Kit** — a 21-page teacher-plus-student packet that teaches you how to
   set up, schedule, facilitate, and assess literature circles, with a built-in
   public-domain practice reading so you can run it tomorrow with no purchased books.
2. **Student organizers** — reusable 3–2–1 note sheets and Jigsaw sheets (Appendix A/B).
3. **Per-title planners** — worked + blank literature-circle planners for 13 specific
   TEKS texts, so teachers and students see a *finished* plan for a real book/story and
   get a matching blank to fill in.

Everything is authored in Python generators and rendered to static HTML/CSS and
print-ready US Letter PDFs (headless Chrome). No build tools beyond the Python
standard library and Chrome.

---

## 2. The Launch Kit (`packet.html` / `literature-circles-launch-kit.pdf`)

21 pages: a cover, **10 numbered instructional sections**, and two optional student
organizers in an appendix. Sections carry a number in the footer so teachers can copy
only what each role needs (a section may span more than one PDF page).

| # | Section | Audience | Copy |
|---|---------|----------|------|
| 1 | Launch literature circles (quick start) | Teacher | once |
| 2 | Choose and clear the reading (text approval) | Teacher | once |
| 3 | Plan from the TEKS | Teacher | once |
| 4 | Run the launch and the cycle (facilitation) | Teacher | once |
| 5 | Our circle agreement and calendar | Group | per group |
| 6 | Read, prepare, and bring evidence | Individual | per student |
| 7 | Rotate leadership; share the thinking (roles/talk) | Student | per student |
| 8 | Meeting agenda and group record | Group | per group |
| 9 | Practice with a public-domain fable | Student | per student |
| 10 | Assess, adjust, and keep going | Teacher | once |
| A | 3–2–1 reading notes organizer | Student | optional |
| B | Jigsaw notes and quick-write | Student | optional |

**Copy map:** Teacher pp. 1–4 & 10 once · group pp. 5 & 8 per group · student pp. 6, 7,
9 per student. Print US Letter at 100%; single-sided keeps forms reusable.

### Key capabilities
- **Grab-and-go launch:** a 45-minute first meeting plan and a reusable two-week /
  five-lesson cycle for novels.
- **Local text approval built in:** a screening checklist and a write-in approval log
  (title/edition, reviewer, date, copies/access/alternate) to satisfy district process
  before launch.
- **TEKS planning map** (see §5) linking grade/course codes to observable evidence.
- **Make-learning-visible framing:** explicit learning intentions and success criteria
  on every meeting.
- **Accessibility:** high-contrast print CSS, alt text on all illustrations, and a
  responsive online reading view; sample notes have text transcripts for screen readers.
- **Self-contained practice text:** an original classroom retelling of Aesop's *The
  North Wind and the Sun* (public domain), used to model the routines before transfer
  to the class reading. Completed photographic sample notes are included.

---

## 3. Instructional strategies

The kit is built on a few research-informed routines and cites them:

- **Literature circles** — small groups read a common text, bring their own questions,
  and build interpretation together; roles support (not replace) everyone's thinking.
- **Reciprocal Teaching** — explicit modeling of **predict → question → clarify →
  summarize**, then gradual release of leadership. Every student uses all four moves on
  the individual prep sheet (§6); the role sheet (§7) assigns who *starts* each move.
  Reference: VisibleLearningMetaX (reciprocal teaching).
- **Jigsaw (optional)** — after everyone has read, home-group members take an expert
  **lens** (character, language, plot, theme, and point of view for a 5th reader), meet
  in expert groups, then teach their home group and synthesize. Reference:
  VisibleLearningMetaX (jigsaw method). The kit warns against dividing *unread* novel
  chapters among experts — every reader needs the whole story context.
- **3–2–1 notes** — 3 important ideas, 2 supporting details (with locations), 1 summary,
  plus questions and vocabulary. Adapted from Miguel Guhlin's Notes Organizer v3.
- **Evidence-and-reasoning** — students cite page/paragraph locations, separate summary
  from interpretation, and revise thinking after discussion.

---

## 4. Per-title planners (`planners/`)

For each of 13 texts there are **two** US Letter pages in **two** versions:

- **Worked example** (`<slug>.pdf`) — a finished plan (text/target, reading calendar,
  roles, text-specific discussion questions, Jigsaw lenses) **plus** a completed student
  3–2–1 prep. Sample answers show in tinted italic.
- **Blank companion** (`<slug>-blank.pdf`) — keeps the *teacher scaffolds* (TEKS target,
  learning intention, success criteria, suggested reading chunks, the text-specific
  questions, and the Jigsaw lenses) but leaves the group/calendar/roles and the 3–2–1
  organizer empty for students to fill in.

**Design intent:** the worked version is a model ("what good looks like"); the blank is
the ready-to-use handout. Both mirror kit section 5 (page 1) and section 6 / Organizer A
(page 2), so they drop straight into the larger kit.

Browse: `planners/index.html` (also linked from the kit landing page).

### 4.1 Title roster

| Title | Author | Yr | Grades | Genre | Rights | Chunks | TEKS anchor | PlotPoint room |
|-------|--------|----|--------|-------|--------|--------|-------------|----------------|
| The Gift of the Magi | O. Henry | 1905 | 7–10 | short story | Public domain | 2 | Grade 8 · §110.24 | ✅ `magi` |
| The Necklace | Guy de Maupassant | 1884 | 8–10 | short story | Public domain | 2 | Grade 8 · §110.24 | ✅ `necklace` |
| To Build a Fire | Jack London | 1908 | 8–11 | short story | Public domain | 2 | English I · §110.36 | ✅ `tobuildafire` |
| The Tell-Tale Heart | Edgar Allan Poe | 1843 | 8–11 | short story | Public domain | 2 | Grade 8 · §110.24 | ✅ `poe` |
| The Monkey's Paw | W. W. Jacobs | 1902 | 7–10 | short story | Public domain | 2 | Grade 7 · §110.23 | ✅ `monkeyspaw` |
| The Gettysburg Address | Abraham Lincoln | 1863 | 6–12 | speech (nonfiction) | Public domain | 2 | Grade 8 · §110.24 (nonfiction) | ✅ `gettysburg` |
| The Yellow Wallpaper | Charlotte Perkins Gilman | 1892 | 10–12 | short story | Public domain | 2 | English III · §110.38 | ✅ `yellowwallpaper` |
| The Secret Garden | Frances Hodgson Burnett | 1911 | 5–7 | novel | Public domain | 3 | Grade 6 · §110.22 | — |
| Little Women | Louisa May Alcott | 1868–69 | 7–9 | novel | Public domain | 2 | Grade 8 · §110.24 | — |
| Narrative of the Life of Frederick Douglass | Frederick Douglass | 1845 | 9–12 | memoir (nonfiction) | Public domain | 3 | English III · §110.38 | ✅ `douglass` |
| The Giver | Lois Lowry | 1993 | 6–8 | novel | **Copyrighted** | 3 | Grade 7 · §110.23 | — |
| Kindred | Octavia E. Butler | 1979 | 11–12 | novel | **Copyrighted** | 3 | English III · §110.38 | ✅ `kindred` |
| Brave New World | Aldous Huxley | 1932 | 11–12 | novel | **Copyrighted** | 3 | English IV · §110.39 | ✅ `bnw` |

**Coverage:** 10 public-domain (7 short works + speech/memoir + 2 novels) and 3
copyrighted novels; grades 5–12; short story, novel, speech, and memoir; 10 of 13 have a
matching PlotPoint room.

### 4.2 What each planner contains

**Page 1 — the plan**
- Text / author / edition, group / period / dates.
- Grade + TEKS target (from the kit's map), learning intention, success criteria.
- Reading map & calendar (per-text chunks with suggested stopping points and leaders).
- Members & rotating first-meeting jobs (role rotation across meetings).
- 5 text-specific open discussion questions, one per Reciprocal-Teaching move
  (predict / question / clarify / summarize / interpret-the-theme).
- Optional Jigsaw lenses tuned to the text.
- Preview/content note where a title needs one (see §6).

**Page 2 — student prep (3–2–1)**
- A completed (worked) or blank 3–2–1 organizer: questions, 3 ideas, 2 supporting
  details with locations, vocabulary, a summary, an interpretation, and a two-lens
  synthesis.
- "Bring to the circle" prompts and an after-discussion reflection.
- The TEKS evidence the prep produces, and a pointer to the matching PlotPoint room.

### 4.3 Content/sensitivity notes (carried on the planners)

These titles include a preview note so teachers plan context and support:

- **The Yellow Wallpaper** — mental illness; controlling medical/gender dynamics.
- **The Secret Garden** — colonial attitudes and racist language toward Indian servants;
  disability portrayal; death.
- **Little Women** — period gender expectations; religious references; illness/death.
- **Narrative of the Life of Frederick Douglass** — enslavement, violence, racist
  language.
- **The Giver** — "release" (euthanasia); mature ideas.
- **Kindred** — graphic violence, racism, and sexual violence (mature; grades 11–12).
- **Brave New World** — drug use, sexual content, mature themes (grades 11–12).

---

## 5. TEKS alignment

The kit's page 3 maps enrolled grade/course to the relevant TEKS strands and to the
evidence each produces. Codes refer to subsection (b) of the cited rule; verified
2026-09-16 against TEA Chapter 110, Subchapters A–C.

| Grade / course | Rule | Collaboration | Comprehension / response | Literary focus |
|---|---|---|---|---|
| 5 | §110.7 | 1(D) | 6(B,F,I); 7(C,D) | 8(A) themes |
| 6 | §110.22 | 1(D) | 5(B,F,I); 6(C,D) | 7(A) themes within/across |
| 7 | §110.23 | 1(D) | 5(B,F,I); 6(C,D) | 7(A) themes within/across |
| 8 | §110.24 | 1(D) | 5(B,F,I); 6(C,D) | 7(A) theme via characters/events |
| English I | §110.36 | 1(D) | 4(B,F,I); 5(C,D) | 6(A) theme via characterization/plot |
| English II | §110.37 | 1(D) | 4(B,F,I); 5(C,D) | 6(A) theme; cross-cultural |
| English III | §110.38 | 1(D) | 4(B,F,I); 5(C,D) | 6(A) relationships among elements |
| English IV | §110.39 | 1(D) | 4(B,F,I); 5(C,D) | 6(A) relationships among elements |

- **High school** aligns by **course enrollment**, not grade number.
- **Nonfiction** (Gettysburg Address, Douglass) keeps collaboration/comprehension/
  response targets and swaps the literary focus for the course's informational or
  argumentative-text expectation (e.g., author's purpose, claim, rhetorical devices).
  The nonfiction TEKS codes on those two planners are a best-fit starting point — verify
  against your exact course before publishing to staff.

---

## 6. Copyright handling (copyrighted titles)

The three copyrighted novels (The Giver, Kindred, Brave New World) follow the PlotPoint
copyrighted-work workflow so the planners are transformative companions, not
reproductions:

- **Paraphrase-only, quotation-free** — no passages or quotations from the book.
- **Disclaimer callout** on page 1 (independent educational companion; students need a
  lawful copy; not affiliated with author/publisher).
- **Strengthened content/preview note** (maturity, previewed edition).
- **"Verify against the text"** flags on any specific plot detail in the worked prep.
- **No Gutenberg/LibriVox links** (those are for public-domain texts only).

Public-domain planners may quote briefly and can point to a free reading source; the
practice fable and all public-domain texts retain that status.

---

## 7. PlotPoint connections

PlotPoint (`activities/plotpoint/`) is the sibling collection of interactive
literature-learning "rooms" with evidence-and-reasoning tasks. The two are designed to
work together:

- **Print → interactive:** run a literature circle from a planner, then send students to
  the matching PlotPoint room for more evidence-and-reasoning practice on the same text.
- **Shared analytical stance:** both emphasize paraphrase, text evidence with locations,
  and reasoning about theme/character/structure rather than recall.
- **Aligned copyright rules:** the planners reuse PlotPoint's disclaimer language and
  "no reproduction" rules for copyrighted titles.
- **Rooms available for 10 of 13 titles** (see the roster) — each planner's page 2 links
  its room. No room yet for The Secret Garden, Little Women, or The Giver.

---

## 8. File map

```
litcircles/
├── index.html                         Collection landing page (generated by build.py)
├── packet.html / packet.css           Editable, accessible kit (online + print source)
├── literature-circles-launch-kit.pdf  Print-ready 21-page kit
├── student-organizers.pdf             Appendix A/B only (4 pages)
├── build.py                           Generator for the kit HTML/CSS + landing page
├── build_planners.py                  Generator for the per-title planners
├── README.md                          Sources, licensing, and build instructions
├── readme.md                          ← this reference guide
├── HERO_PROMPT.md / ILLUSTRATION_PROMPTS.md / SAMPLE_NOTES_PROMPTS.md
├── assets/                            Illustrations + completed sample-note images
└── planners/
    ├── index.html                     Planner hub (worked + blank per title)
    ├── <slug>.html / <slug>.pdf        Worked example (13 titles)
    └── <slug>-blank.html / .pdf        Blank companion (13 titles)
```

Slugs: `magi, necklace, tobuildafire, telltale, monkeyspaw, gettysburg, yellowwallpaper,
secretgarden, littlewomen, douglass, giver, kindred, bnw`.

---

## 9. Regenerating & deploying

Uses only the Python standard library plus headless Chrome.

**Kit landing page + packet:**
```bash
cd litcircles
python3 build.py           # regenerates index.html, packet.html/css, README.md
# then render the PDF from packet.html with headless Chrome:
#   --print-to-pdf=literature-circles-launch-kit.pdf --no-pdf-header-footer
# US Letter, 100% scale, no browser headers/footers. Extract the last 4 pages
# to rebuild student-organizers.pdf. Recheck page count after edits.
```

**Per-title planners:**
```bash
cd litcircles
python3 build_planners.py  # writes planners/*.html + planners/index.html
# render every planner to PDF (each must be exactly 2 pages):
for f in planners/*.html; do
  [ "$f" = "planners/index.html" ] && continue
  b="${f%.html}"
  google-chrome-stable --headless --no-sandbox --disable-gpu \
    --print-to-pdf="$b.pdf" --no-pdf-header-footer "$f"
done
```

To add a title: append a dict to `TITLES` in `build_planners.py` (and, for a copyrighted
work, add its disclaimer to the `DISCLAIMER` map and a `prep.paraphrase = True`), then
re-run and re-render. Keep each planner to two pages — the print CSS is tuned so filled
and blank versions both fit; if you add rows, retest the page count.

**Deploy:** the repo's `main` branch is the GitHub Pages production site. Commit and
`git push origin main`; Pages rebuilds in ~1–2 minutes. Verify the live URLs
(`/litcircles/` and `/litcircles/planners/index.html`) return updated content.

---

## 10. Sources

- **Practice fable:** *The Aesop for Children* (1919), public domain —
  https://www.gutenberg.org/ebooks/19994 (original retelling, not a reproduction).
- **Strategy research:** VisibleLearningMetaX — reciprocal teaching and jigsaw method.
- **TEKS:** TEA Chapter 110, Subchapters A–C (verified 2026-09-16).
- **Organizer basis:** Miguel Guhlin's Notes Organizer v3.
- **Copyright disclaimers:** `activities/plotpoint/copyright-disclaimers.md`.
