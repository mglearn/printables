# Texas Grab-and-Go Substitute Packets

## Codex Development Plan

**Initial grade band:** Grades 6–8  
**Later expansion:** Grades 3–5, followed by grades 9–12  
**Core content areas:** Reading Language Arts, Mathematics, Science, and Social Studies  
**Document status:** Planning specification  
**Standards verification date:** September 3, 2026

---

## 1. Bottom Line

Build this as a standards-driven publishing system, not as a folder of manually formatted worksheets.

Each packet should begin as structured content linked to a verified TEKS record. Codex should use shared templates to generate:

1. A substitute-facing guide
2. A student activity packet
3. A separate answer key
4. An optional all-in-one teacher master
5. An accessible HTML version
6. A preview image and catalog record
7. Grade-level and subject-area ZIP files

The first production goal should be twelve pilot packets: one packet for each grade and core subject combination. Do not attempt the full library until the templates, standards data, PDF build process, and quality checks work on those twelve packets.

---

## 2. Project Goal

Create printable, self-contained substitute lessons that a classroom teacher can select, print, and leave with little or no preparation.

A successful packet should:

- Fill a normal class period
- Require no student login or internet access
- Use only common classroom materials
- Review or apply grade-level TEKS without depending on the class's current unit
- Include all readings, data, diagrams, maps, examples, directions, and response space
- Be usable by a substitute who may not know the subject
- Give the classroom teacher useful evidence of student thinking
- Include a complete, accurate answer key
- Print clearly in color or grayscale
- Remain editable and regenerable from source files

### Working title

**Texas Grab-and-Go Substitute Packets**

A different public-facing title can be selected later without changing the repository or content model.

---

## 3. Product Definition

### 3.1 Default classroom assumptions

Design the first release around these assumptions:

- Class period: 45–60 minutes
- Student work mode: Independent by default
- Required materials: Pencil and printed packet
- Optional materials: Colored pencils, ruler, calculator, or blank paper when listed
- Technology: None required
- Teacher preparation: Five minutes or less
- Substitute preparation: Five minutes or less
- Reading level: Grade appropriate, with plain-language directions
- Language: English first, with architecture ready for Spanish versions
- Printing: US Letter, copier safe, duplex friendly
- Activity purpose: Review, reasoning, application, and retrieval rather than first-time instruction

### 3.2 Non-goals

The packets should not:

- Replace a district curriculum
- Claim to cover every TEKS student expectation
- Depend on a specific textbook or commercial program
- Reproduce copyrighted textbook passages or worksheets
- Require the substitute to lecture
- Require lab chemicals, heat sources, outdoor work, or specialized equipment
- Depend on a classroom's current pacing calendar
- Present themselves as official TEA, STAAR, or SST materials
- Use the phrase “TEKS-aligned” until a human reviewer confirms the alignment
- Put answer keys inside student-facing files
- Collect student data

---

## 4. Standards Baseline

Use official Texas Education Agency and Texas Administrative Code sources as the single source of truth.

### 4.1 Grades 6–8 standards chapters

| Subject | Current middle school sections to ingest |
|---|---|
| Reading Language Arts | 19 TAC Chapter 110, §§110.22–110.24 |
| Mathematics | 19 TAC Chapter 111, §§111.26–111.28 |
| Middle School Advanced Mathematics | 19 TAC Chapter 111, §§111.29–111.31 |
| Science | 19 TAC Chapter 112, §§112.26–112.28 |
| Social Studies | 19 TAC Chapter 113, §§113.18–113.20 |
| English Language Proficiency Standards | 19 TAC Chapter 120, §120.21, Grades 4–12 |

### 4.2 Current implementation notes

- The current science TEKS for grades 6–8 were adopted in 2021 and implemented beginning with the 2024–2025 school year.
- The current social studies TEKS for grades 6–8 were adopted in 2022 and implemented beginning with the 2024–2025 school year.
- The new ELPS for grades 4–12 are implemented beginning with the 2026–2027 school year.
- Middle School Advanced Mathematics TEKS were adopted in 2025 and may be used beginning with the 2025–2026 school year.
- Standard mathematics and Middle School Advanced Mathematics must be treated as separate course paths.

### 4.3 Standards source rules

Codex must never invent a TEKS code, wording, adoption year, or implementation date.

For every student expectation stored in the project, capture:

- Exact code
- Exact official wording
- Subject
- Grade or course
- Strand
- Knowledge and skills statement
- Student expectation
- Adoption year
- Effective or implementation year
- Official source URL
- Date verified
- Verification status
- Notes about amendments or course variants

Store standards separately from packet content so they can be updated without rewriting packets.

---

## 5. Rollout Strategy

### 5.1 Recommended release levels

| Release | Scope | Packet count | Purpose |
|---|---:|---:|---|
| Template proof | One grade 7 science packet | 1 | Prove the complete build and review process |
| Subject proof | One grade 7 packet in each core subject | 4 | Confirm that one template system can support different subject structures |
| Middle school pilot | One packet per grade and subject | 12 | Test all grades and content areas |
| Release 1 | Four packets per grade and subject | 48 | Provide one packet for each major content family |
| Full middle school library | Eight packets per grade and subject | 96 | Add choice, spiral review, and second treatments of major standards |
| Grades 3–5 expansion | Four to eight packets per grade and subject | 48–96 | Reuse the system with elementary design changes |
| Grades 9–12 expansion | Organize by course rather than grade | To be scoped | Support common high school courses and block schedules |

### 5.2 Why four packets per grade and subject is the first full release

Four packets create a useful library without producing dozens of near-duplicate worksheets.

The first four packets should correspond to major content families:

#### Reading Language Arts

1. Comprehension and response
2. Multiple genres
3. Author's purpose and craft
4. Composition, revision, editing, and research

#### Mathematics

1. Numerical representations and relationships
2. Computations and algebraic relationships
3. Geometry and measurement
4. Data analysis and personal financial literacy

#### Science

1. Matter and energy
2. Force, motion, and energy
3. Earth and space
4. Organisms and environments

Scientific and engineering practices and recurring themes should appear across all four science packets.

#### Social Studies

1. History
2. Geography and culture
3. Government and citizenship
4. Economics, science, technology, and society

Social studies skills should appear across all four packets.

---

## 6. Standard Packet Package

Every packet should generate the following files.

```text
G07_SCI_ThermalEnergy_01/
  G07_SCI_ThermalEnergy_01_SubGuide.pdf
  G07_SCI_ThermalEnergy_01_Student.pdf
  G07_SCI_ThermalEnergy_01_AnswerKey.pdf
  G07_SCI_ThermalEnergy_01_TeacherMaster.pdf
  G07_SCI_ThermalEnergy_01.html
  G07_SCI_ThermalEnergy_01_Preview.webp
  manifest.json
```

### 6.1 Substitute guide

Target length: One or two pages.

Include:

- Packet title, grade, subject, and estimated time
- Plain-language learning goal
- Primary and supporting TEKS
- Materials
- Five-minute setup
- Suggested timing
- A short script the substitute can read
- Directions for independent work
- What to do when students ask for help
- Which tools students may use
- Early-finisher directions
- Accommodation and language-support notes
- Collection instructions
- A note that the answer key is separate
- Teacher follow-up suggestion

The substitute guide should be usable without opening the answer key.

### 6.2 Student packet

Target length: Four to six pages.

Include:

1. Name, class period, and date fields
2. A short “Start Here” box
3. A five-minute retrieval or noticing task
4. A brief reference, model, reading, data set, map, diagram, or worked example
5. One substantial main activity
6. A reasoning or evidence response
7. An ACE close
8. An optional early-finisher task
9. A final check that tells students what to turn in

### 6.3 Answer key

Target length: Two to four pages.

Include:

- Answers by page and question number
- Worked steps for mathematics
- Evidence locations for RLA and social studies
- Model explanations for science
- Acceptable alternate answers
- Short constructed-response rubric
- Common misconception notes
- A note when more than one answer is defensible
- Estimated completion time by section
- Teacher follow-up suggestions based on likely errors

### 6.4 Teacher master

Combine, in this order:

1. Substitute guide
2. Student packet
3. Answer key

Add a visible divider page before the answer key so it is not accidentally copied for students.

### 6.5 Accessible HTML version

The HTML version should:

- Use semantic headings, lists, tables, and form labels
- Preserve the full student activity
- Include alt text for informative images
- Avoid color-only directions
- Be keyboard readable
- Reflow on phones and at high zoom
- Provide a print button
- Link to the student PDF
- Keep the answer key on a separate teacher-facing page or file

---

## 7. Common Learning Sequence

Use a predictable sequence across subjects. Students should recognize the routine even when the content changes.

### Part 1: Start

Time: Five minutes

Purpose:

- Settle the room
- Activate prior knowledge
- Give every student an immediate task
- Reduce the amount of oral direction required from the substitute

Possible formats:

- Notice and wonder
- Two retrieval questions
- Vocabulary match
- Estimate and explain
- Quick source observation
- Diagram label
- Error analysis

### Part 2: Build

Time: Five to ten minutes

Purpose:

- Supply the minimum information needed for independent work
- Review a procedure or concept
- Prevent the packet from becoming a test of memory alone

Possible formats:

- Short original passage
- Worked example
- Reference box
- Map, timeline, chart, or diagram
- Formula or vocabulary bank
- Brief model response

### Part 3: Apply

Time: Twenty to twenty-five minutes

Purpose:

- Ask students to use the standard in a meaningful task
- Produce observable evidence of reasoning

Possible formats:

- Analyze a scenario
- Interpret a data set
- Compare sources
- Complete a multi-step problem
- Classify and justify
- Revise a draft
- Build or evaluate a model
- Make a decision from evidence

### Part 4: Explain

Time: Five to ten minutes

Purpose:

- Require reasoning, evidence, or a check of the process
- Give the classroom teacher something useful to review

### Part 5: ACE Close

Time: Five minutes

Use a short common closure:

- **Articulate:** Explain the main idea or method in your own words
- **Connect:** Show how it connects to the reading, data, model, or something already learned
- **Extend:** Apply it to a new example, question, or situation

The ACE close should be short enough to complete even when the class moves slowly.

### Part 6: Continue

Time: Five to fifteen minutes, optional

Use an extension that does not require new materials:

- Create another example
- Correct a flawed response
- Write a challenge problem
- Compare two solutions
- Draw a model
- Apply the idea to a new context
- Write a question for another student

---

## 8. Subject-Specific Design Specifications

## 8.1 Reading Language Arts

### Default structure

- One or two original or openly licensed texts
- A short vocabulary or context task
- Comprehension and inference questions
- Text-evidence questions
- Author's craft or structure task
- Short constructed response
- Revision or editing task when appropriate
- ACE close

### Recommended activity types

- Compare two short texts
- Trace a central idea or theme
- Analyze character change
- Identify claim, evidence, and reasoning
- Examine word choice and tone
- Sequence and summarize
- Revise an unfocused paragraph
- Edit for conventions in context
- Evaluate which evidence best supports a response
- Write a paragraph using supplied evidence

### Content rules

- Write original passages whenever possible.
- Use public-domain or clearly licensed sources only when original text is not appropriate.
- Store source and license information in the packet manifest.
- Avoid long passages that turn the packet into silent reading for the whole period.
- Do not use isolated grammar drills as the entire packet.
- Give enough response space for the expected answer.
- Make every text-dependent question answerable from the included text.
- Label open-ended questions clearly when several responses may be valid.

### Evidence expected

- Selected evidence
- Annotation
- Short written explanation
- Revised sentence or paragraph
- Organized response using the text

---

## 8.2 Mathematics

### Default structure

- Two retrieval problems
- One worked example or reference box
- A visual or contextual problem set
- One error-analysis item
- One multi-step application
- One explanation or justification
- ACE close
- Optional challenge

### Recommended activity types

- Match tables, graphs, equations, and situations
- Analyze a flawed solution
- Compare two strategies
- Complete a real-world planning task
- Interpret a scale drawing
- Use data to make a decision
- Solve and explain
- Estimate before calculating
- Identify which information is relevant
- Build a representation from a scenario

### Content rules

- State whether calculators are allowed.
- Include every formula that the student is expected to use unless recall is part of the aligned expectation.
- Use realistic numbers and units.
- Avoid trick questions.
- Do not require a substitute to teach a new algorithm.
- Show complete worked solutions in the key.
- Test every item with an independent solver.
- Use diagrams drawn as SVG or deterministic shapes, not generated images.
- Keep standard and Middle School Advanced Mathematics packets in separate catalogs.

### Evidence expected

- Accurate calculations
- Labeled representations
- Strategy choice
- Written explanation
- Check or estimate
- Error correction

---

## 8.3 Science

### Default structure

- A phenomenon, image, model, or data set
- Observation and inference prompts
- A short content reference
- Data, model, or classification task
- Claim, evidence, and reasoning response
- ACE close
- Optional design or prediction task

### Recommended activity types

- Analyze a scientific model
- Interpret a graph or table
- Classify matter or organisms using evidence
- Evaluate an investigation design
- Identify patterns and relationships
- Compare models and their limitations
- Explain a phenomenon
- Predict what changes when one variable changes
- Use a paper-based engineering design scenario
- Correct a scientific misconception

### Safety rules

The default substitute packet must not require:

- Chemicals
- Heat
- Glassware
- Open flames
- Food tasting
- Outdoor collection
- Live organisms
- Student-built electrical circuits
- Unsupervised physical demonstrations

A paper investigation may use supplied data from a described experiment.

### Grade 6 content examples

- Pure substances and mixtures
- Metals, nonmetals, and metalloids
- Evidence of chemical change
- Net force and Newton's Third Law
- Potential and kinetic energy
- Seasons, tides, and Earth systems
- Ecosystem relationships
- Cells and variation

### Grade 7 content examples

- Elements and compounds
- Physical and chemical changes
- Solutions and dissolution
- Motion and Newton's First Law
- Thermal energy transfer
- Solar system organization and gravity
- Plate tectonics and the hydrosphere
- Organ systems, reproduction, selection, energy flow, and classification

### Grade 8 content examples

- Elements, compounds, mixtures, acids, bases, and conservation of mass
- Newton's Second Law and the three laws acting in systems
- Waves and energy transfer
- Stars, galaxies, weather, ocean systems, and climate
- Organelles, genes, chromosomes, traits, and environmental change

Scientific and engineering practices should be paired with grade-level content rather than treated as an isolated packet family.

### Evidence expected

- Observation versus inference
- Graph or model interpretation
- Scientific claim
- Cited data or model evidence
- Reasoning that links evidence to the claim
- Prediction or design decision

---

## 8.4 Social Studies

### Grade-level course frame

- Grade 6: Contemporary societies, geography, culture, government, economics, and related historical context
- Grade 7: Texas history from early times to the present
- Grade 8: United States history from the early colonial period through Reconstruction

### Default structure

- One or more short sources
- A map, timeline, chart, image, or table
- Source observation and context prompts
- Comparison or cause-and-effect task
- Evidence-based written response
- ACE close
- Optional connection task

### Recommended activity types

- Compare two historical accounts
- Analyze a map and population data
- Build a cause-and-effect chain
- Sequence events and explain significance
- Evaluate a claim using two sources
- Interpret a political cartoon that is public domain or original
- Compare systems of government
- Make a decision using economic data
- Analyze change and continuity
- Correct an inaccurate summary

### Content rules

- Use original summaries, public-domain primary sources, or openly licensed materials.
- Preserve historical context when excerpting a source.
- Avoid present-day partisan prompts.
- Do not ask students to infer facts that are not in the packet.
- Clearly identify source creator, date, and source type when known.
- Distinguish fact, interpretation, and opinion.
- Include maps with readable labels and a grayscale-safe legend.

### Evidence expected

- Source-based observation
- Chronology
- Geographic interpretation
- Cause-and-effect reasoning
- Comparison
- Claim supported by evidence
- Explanation of historical significance

---

## 9. Twelve-Packet Pilot Matrix

Exact TEKS codes must be added only after the standards records are imported and reviewed.

| Grade | Subject | Provisional pilot topic | Main student product |
|---:|---|---|---|
| 6 | RLA | Central idea, inference, and evidence across two informational texts | Evidence-based paragraph |
| 6 | Mathematics | Ratios, rates, percentages, and representations | Completed decision task with explanation |
| 6 | Science | Classifying matter from physical-property data | Classification table and CER response |
| 6 | Social Studies | Comparing contemporary societies with maps and data | Comparison and evidence response |
| 7 | RLA | Theme, character change, and author's craft in short fiction | Theme explanation with evidence |
| 7 | Mathematics | Proportional relationships and percent applications | Multi-representation solution |
| 7 | Science | Thermal energy transfer in a building-design scenario | Model analysis and CER response |
| 7 | Social Studies | A Texas history turning point using a timeline and short sources | Cause-and-effect explanation |
| 8 | RLA | Analyzing an argument, evidence quality, and revision | Revised claim and evidence response |
| 8 | Mathematics | Linear relationships from tables, graphs, equations, and contexts | Matched representations and justification |
| 8 | Science | Newton's laws in a transportation-safety scenario | Force analysis and design recommendation |
| 8 | Social Studies | Constitutional principles or Reconstruction using short sources | Source-based historical claim |

### Pilot order

Build in this sequence:

1. Grade 7 science
2. Grade 7 RLA
3. Grade 7 mathematics
4. Grade 7 social studies
5. Grade 6 versions
6. Grade 8 versions

Grade 7 provides a useful middle point for testing reading load, page design, directions, and content complexity before adjusting down for grade 6 or up for grade 8.

---

## 10. Content Data Model

Keep packet content in structured YAML and long-form text in Markdown files.

### 10.1 Packet manifest example

```yaml
id: G07_SCI_ThermalEnergy_01
version: 0.1.0
status: draft

audience:
  level_type: grade
  grade: 7
  course_id: null

subject:
  code: SCI
  name: Science

title: Thermal Energy at School
slug: thermal-energy-at-school

duration:
  core_minutes: 45
  extension_minutes: 15

materials:
  required:
    - pencil
    - printed packet
  optional:
    - colored pencils

work_mode:
  default: independent
  optional: partner-check

standards:
  primary:
    - code: "7.x.x"
      verification_status: pending
  supporting: []

language_supports:
  vocabulary:
    - conduction
    - convection
    - radiation
    - thermal equilibrium
  sentence_stems:
    - "The evidence shows..."
    - "Energy transfers from ___ to ___ because..."
  visual_supports: true

accessibility:
  color_required: false
  calculator_allowed: false
  read_aloud_allowed: true
  response_options:
    - written
    - labeled_diagram

source_files:
  substitute_guide: sub-guide.md
  student_content: student.md
  answer_key: answer-key.md

copyright:
  text: original
  images: original-svg
  license: CC-BY-4.0

review:
  standards_reviewed_by: null
  content_reviewed_by: null
  copyedited_by: null
  print_checked_by: null
  last_verified: null
```

### 10.2 Question model

Every question needs a stable ID.

```yaml
questions:
  - id: Q01
    section: start
    type: short_response
    prompt: "What do you notice about the temperatures in the diagram?"
    points: 1
    expected_minutes: 2
    answer:
      type: acceptable_examples
      values:
        - "The metal surface is warmer than the wood surface."
    rubric_id: null

  - id: Q08
    section: explain
    type: constructed_response
    prompt: "Which design would reduce heat transfer most effectively? Use two pieces of evidence."
    points: 3
    expected_minutes: 8
    answer:
      type: rubric
      rubric_id: CER_3PT
```

### 10.3 Standards record example

```json
{
  "code": "112.27.b.8.A",
  "display_code": "7.8A",
  "subject": "science",
  "grade": 7,
  "course": null,
  "strand": "Force, motion, and energy",
  "knowledge_statement": "Official text from the current TAC",
  "student_expectation": "Official text from the current TAC",
  "adopted_year": 2021,
  "implementation_year": "2024-2025",
  "source_url": "https://tea.texas.gov/...",
  "verified_on": "2026-09-03",
  "status": "verified"
}
```

Do not store only shortened codes such as `7.8A`. The canonical record should include the TAC chapter and section so duplicate or ambiguous codes cannot collide.

---

## 11. Repository Structure

```text
texas-substitute-packets/
  README.md
  LICENSE
  package.json
  tsconfig.json

  docs/
    PROJECT_PLAN.md
    CONTENT_GUIDE.md
    STYLE_GUIDE.md
    TEKS_VERIFICATION.md
    ACCESSIBILITY_CHECKLIST.md
    REVIEW_WORKFLOW.md
    RELEASE_CHECKLIST.md
    CODEX_TASKS.md

  standards/
    sources/
      tea-source-index.yml
    normalized/
      elar-6-8.json
      math-6-8.json
      math-advanced-6-8.json
      science-6-8.json
      social-studies-6-8.json
      elps-4-12.json
    schemas/
      standard.schema.json
    standards-lock.json

  content/
    grade-06/
      rla/
      math/
      science/
      social-studies/
    grade-07/
      rla/
      math/
      science/
      social-studies/
    grade-08/
      rla/
      math/
      science/
      social-studies/

  templates/
    layouts/
      substitute-guide.njk
      student-packet.njk
      answer-key.njk
      teacher-master.njk
      packet-page.njk
      catalog-page.njk
    components/
      header.njk
      timing-box.njk
      standards-box.njk
      vocabulary-box.njk
      ace-close.njk
      rubric.njk
      footer.njk

  styles/
    tokens.css
    print.css
    screen.css
    subjects.css

  assets/
    shared/
      icons/
      diagrams/
    grade-06/
    grade-07/
    grade-08/

  schemas/
    packet.schema.json
    questions.schema.json
    catalog.schema.json

  scripts/
    import-standards.ts
    validate-standards.ts
    validate-packets.ts
    validate-answers.ts
    validate-assets.ts
    render-html.ts
    render-pdfs.ts
    render-previews.ts
    build-catalog.ts
    build-zips.ts
    check-overflow.ts
    check-links.ts
    check-pdf-output.ts

  tests/
    standards/
    content/
    rendering/
    fixtures/

  site/
    index.html
    catalog.json
    assets/

  dist/
    packets/
    zips/
    previews/
    catalog.csv
    catalog.json

  .github/
    workflows/
      validate.yml
      build.yml
      release.yml
```

---

## 12. Technical Build Approach

### 12.1 Recommended stack

- Current Node.js LTS
- TypeScript
- YAML for packet manifests
- Markdown for longer content
- JSON Schema plus Ajv for validation
- Nunjucks for HTML templates
- Playwright or Puppeteer for PDF rendering
- Vitest for unit and integration tests
- Sharp for preview thumbnails
- A simple Node build script for the static catalog
- GitHub Actions for validation and release builds

Avoid a large web framework unless the catalog later requires features that cannot be handled by a static site.

### 12.2 Source-to-output pipeline

```text
Official standards sources
        ↓
Normalized TEKS and ELPS records
        ↓
Packet YAML and Markdown content
        ↓
Schema and alignment validation
        ↓
HTML templates and print CSS
        ↓
Accessible HTML packet
        ↓
Student, guide, key, and master PDFs
        ↓
Preview images, catalog records, and ZIP files
        ↓
Static download site
```

### 12.3 PDF requirements

- US Letter page size
- Selectable text
- Embedded or reliable system fonts
- No page content clipped outside margins
- Consistent page numbers
- No accidental blank pages
- Student and answer-key files remain separate
- Charts and diagrams remain legible in grayscale
- No required content exists only as an image
- Hyperlinks may appear in the teacher guide but should not be necessary to complete the activity
- The source HTML should remain available as the accessible alternative

### 12.4 Subject design tokens

Use one restrained accent per subject while preserving grayscale usability.

```css
:root {
  --ink: #172033;
  --muted: #5a6680;
  --paper: #ffffff;
  --panel: #f4f6f9;
  --line: #c8d0dc;

  --rla-accent: #6b3fa0;
  --math-accent: #0a5f8f;
  --science-accent: #17745b;
  --social-studies-accent: #9a5b17;
}
```

The subject color may help navigation, but icons, labels, headings, and patterns must also communicate the subject.

---

## 13. Print and Visual Design Rules

### 13.1 Page layout

- US Letter
- Portrait by default
- Landscape only when a map, chart, or mathematical representation needs it
- Minimum half-inch margins
- Body text approximately 11.5–12.5 points
- Student directions larger than body text
- Strong heading hierarchy
- One main task per page when possible
- No decorative background textures
- No low-contrast gray body text
- No edge-to-edge color blocks that consume toner
- No URL or promotional footer on student pages
- Packet ID and page number in a small footer
- Adequate writing space for the expected answer

### 13.2 Image rules

- Use SVG for diagrams, graphs, timelines, icons, and maps whenever practical.
- Use original, public-domain, or openly licensed images.
- Record source and license information.
- Do not rely on an image generator to create required wording, labels, formulas, or data.
- Render all required text deterministically in HTML, SVG, or the PDF layout.
- Add alt text in the HTML version.
- Test images at copier quality.

### 13.3 Grayscale check

Every packet must remain understandable when printed on a basic black-and-white copier.

Check:

- Legends
- Graph lines
- Map regions
- Correct and incorrect examples
- Category cards
- Callout boxes
- Scientific diagrams

Use labels, line patterns, symbols, or shapes in addition to color.

---

## 14. Accessibility and Language Supports

### 14.1 Common accessibility features

Each packet should include or support:

- Clear, numbered directions
- Short direction chunks
- Visible examples
- Sufficient white space
- Consistent question numbering
- High contrast
- No color-only meaning
- Read-aloud compatibility unless the aligned skill requires independent reading
- Alternative response options when they do not change the skill
- Vocabulary support
- Sentence stems
- Chunked multi-step tasks
- A clear stopping point and turn-in direction

### 14.2 ELPS integration

Do not add a generic ELPS code to every packet.

Instead:

1. Identify the language action students must perform.
2. Select the applicable current Grades 4–12 ELPS.
3. Add a specific support that helps students perform that action.
4. Explain the support in the substitute guide.
5. Keep the grade-level academic task intact.

Examples:

- Read a complex source with a small glossary
- Describe a pattern using a sentence frame
- Compare two ideas using a transition bank
- Explain evidence using a labeled organizer
- Rehearse an oral response before writing

### 14.3 Translation readiness

Store directions, labels, and reusable components in separate locale files.

```text
locales/
  en.yml
  es.yml
```

Do not machine-translate complete packets without human review by a bilingual educator.

---

## 15. Copyright, Privacy, and Safety

### 15.1 Copyright

Use:

- Original passages
- Public-domain texts and images
- Government sources where reuse is permitted
- Openly licensed materials with attribution
- Original SVG diagrams, maps, and charts

Do not:

- Copy textbook passages
- Reproduce commercial worksheets
- Scrape quiz sites
- Rebuild released assessment items with minor wording changes
- Use copyrighted photographs without a documented license

Recommended licensing:

- Original instructional content: CC BY 4.0
- Code: MIT
- Third-party sources: Retain the original license and attribution

### 15.2 Privacy

The packets and site should:

- Require no accounts
- Collect no student names beyond the printed name field
- Send no student responses anywhere
- Use no third-party forms
- Use no advertising trackers
- Avoid analytics on typed responses
- Process any optional site filtering in the browser

### 15.3 Safety

Science packets should be paper-based unless the classroom teacher deliberately selects a separate hands-on version.

Substitute packets must not place the substitute in charge of a hazardous activity.

---

## 16. Validation and Quality Gates

## 16.1 Automated validation

Codex should create scripts that fail the build when any of these checks fail.

### Standards checks

- Every TEKS code exists in the standards lock
- Grade and subject match
- Primary TEKS are not duplicated accidentally
- Every standards record has a source URL and verification date
- No `pending` standards appear in a release build
- Standard and advanced mathematics are not mixed

### Content checks

- Required manifest fields exist
- Every question has a unique ID
- Every question has an answer or rubric
- Every answer refers to an existing question
- Every page reference in the key exists
- Timing values are present
- Required materials are listed
- Copyright and source fields are complete
- Student files do not contain answer-key markers
- No banned placeholder text remains

### Rendering checks

- All expected HTML and PDF files are created
- PDF page size is US Letter
- Page count falls within the expected range
- No HTML element overflows its printable container
- No missing image or font asset
- No broken internal link
- No accidental blank page
- Preview images are generated
- File naming follows the convention

### Catalog checks

- Every released packet appears in the catalog
- Every catalog link points to an existing file
- Grade, subject, duration, materials, and version filters are populated
- No draft packet appears in the public release

## 16.2 Human review

A packet is not ready because the code built successfully.

Require four human checks:

1. **Standards review:** A Texas educator verifies each TEKS link and alignment rationale.
2. **Content review:** A subject-area educator solves the packet and checks accuracy.
3. **Substitute usability review:** An educator outside that content area follows the substitute guide.
4. **Print review:** Someone prints the packet in grayscale and checks writing space, clipping, order, and readability.

### 16.3 Independent solve test

A reviewer should complete the student packet without reading the answer key.

Record:

- Actual completion time
- Questions that were unclear
- Missing information
- Unexpected alternate answers
- Reading-load concerns
- Places where the packet assumes current-unit knowledge

Revise before release.

---

## 17. Per-Packet Definition of Done

A packet is complete only when all statements are true.

### Standards

- [ ] Primary TEKS are verified against the current official source
- [ ] Supporting TEKS are verified
- [ ] Alignment is explained, not merely listed
- [ ] The task asks students to perform the verb in the student expectation
- [ ] ELPS are included only when matched to an actual language demand

### Substitute use

- [ ] The guide can be understood in five minutes
- [ ] The substitute does not need subject expertise
- [ ] Timing totals 45–60 minutes
- [ ] Early-finisher work is included
- [ ] Required materials are ordinary classroom items
- [ ] No unsafe activity is required

### Student use

- [ ] Students can begin from the printed directions
- [ ] All needed text, data, formulas, maps, and diagrams are included
- [ ] The task does not depend on the current unit
- [ ] Response space matches the expected response
- [ ] Directions are numbered and plain
- [ ] The packet includes a reasoning response
- [ ] The packet includes an ACE close
- [ ] The final turn-in direction is obvious

### Answer key

- [ ] Every question is answered
- [ ] Mathematics includes worked steps
- [ ] Evidence locations are provided when applicable
- [ ] Alternate defensible responses are identified
- [ ] Constructed responses include a rubric
- [ ] Common misconceptions are noted

### Production

- [ ] Student, guide, key, master, HTML, preview, and manifest files build
- [ ] Files use the correct names
- [ ] PDFs print correctly in grayscale
- [ ] No clipping or overflow appears
- [ ] Images and sources are licensed and documented
- [ ] The packet appears in the catalog
- [ ] Version and review dates are current

---

## 18. Static Download Site

The first site can be simple.

### 18.1 Catalog filters

- Grade
- Subject
- Content family
- Estimated time
- Calculator allowed
- Color or grayscale
- Student pages
- Materials
- Language
- Standard or advanced mathematics
- Version

### 18.2 Packet card

Each card should show:

- Title
- Grade and subject
- One-sentence activity description
- Time
- Materials
- Primary TEKS
- Student page count
- Preview
- Student PDF button
- Teacher files button
- Accessible HTML button

### 18.3 Bulk downloads

Generate:

- All grade 6 packets
- All grade 7 packets
- All grade 8 packets
- All RLA packets
- All mathematics packets
- All science packets
- All social studies packets
- Complete grades 6–8 library
- Standard mathematics only
- Middle School Advanced Mathematics only

### 18.4 Answer-key caution

Publicly hosted answer keys cannot be treated as secure.

Keep keys out of student pages and student PDFs. A teacher-only section may make them less obvious, but it should not claim to prevent student access.

---

## 19. Development Phases for Codex

## Phase 0: Repository and source lock

Deliver:

- Repository structure
- Project README
- Standards schemas
- Packet schema
- Source index
- Current grades 6–8 TEKS records
- Current Grades 4–12 ELPS records
- Standards lock with verification date
- Validation scripts

Gate:

- No packet authoring begins until the standards records validate.

## Phase 1: Rendering system

Deliver:

- Shared templates
- Print CSS
- Subject design tokens
- HTML renderer
- PDF renderer
- Preview renderer
- Overflow checks
- Sample fixture packet

Gate:

- The sample fixture generates all expected files and passes print checks.

## Phase 2: Grade 7 science vertical slice

Deliver:

- Full thermal-energy packet
- Substitute guide
- Student packet
- Answer key
- Teacher master
- HTML version
- Preview
- Catalog record
- Automated tests

Gate:

- Standards, subject, substitute, and print reviews pass.

## Phase 3: Grade 7 subject proof

Deliver:

- One packet each for RLA, mathematics, science, and social studies
- Subject-specific components and rubrics
- Revised common template based on actual use

Gate:

- The renderer supports all four subjects without subject-specific hacks scattered through the code.

## Phase 4: Twelve-packet pilot

Deliver:

- One packet for each grade and subject combination
- Pilot feedback form
- Review log
- Updated style and content guides
- Grade-level ZIP files

Gate:

- At least one educator reviews each subject.
- At least one substitute or non-specialist reviews the guide format.
- All packets pass independent solve and grayscale print tests.

## Phase 5: Release 1 library

Deliver:

- Four packets per grade and subject
- Forty-eight complete packet packages
- Static download catalog
- Bulk ZIP files
- Catalog JSON and CSV
- Versioned release

Gate:

- No draft standards or missing source fields
- No failed automated or manual review items
- All catalog links validated

## Phase 6: Full middle school library

Deliver:

- Eight packets per grade and subject
- Ninety-six complete packet packages
- Standard and advanced mathematics separated
- Spiral-review and alternate-context packets
- Optional Spanish pilot packets

## Phase 7: Grades 3–5

Adjust:

- Reading load
- Page density
- Writing space
- Directions
- Visual supports
- Manipulative-free math models
- Elementary science and social studies topics
- Read-aloud guidance

Keep the same data, build, review, and catalog system.

## Phase 8: Grades 9–12

Organize by course, not only by grade.

Likely course families:

- English I, English II, English III, and English IV
- Algebra I, Geometry, Algebra II, and common advanced mathematics courses
- Biology, Integrated Physics and Chemistry, Chemistry, and Physics
- World Geography, World History, United States History, Government, and Economics

Add:

- `course_id`
- Standard class and 90-minute block timing
- Course prerequisites
- Course-specific TEKS source records
- More substantial readings and data sets
- Optional independent research extensions that still work without student logins

---

## 20. Codex Working Rules

Place these rules in `AGENTS.md` or `CODEX.md`.

```markdown
# Codex Working Rules

1. Read `docs/PROJECT_PLAN.md`, `docs/CONTENT_GUIDE.md`, and `docs/TEKS_VERIFICATION.md` before changing packet content.
2. Never invent or guess a TEKS or ELPS code.
3. Treat `standards/standards-lock.json` as the source of truth for release builds.
4. Do not build the entire library in one task.
5. Complete one vertical slice, validate it, and commit it before replication.
6. Keep standards data, instructional content, templates, and generated files separate.
7. Do not edit generated files by hand.
8. Every student question must have a stable ID and a keyed answer or rubric.
9. Never place answer-key content in student-facing files.
10. Use original, public-domain, government, or openly licensed source material.
11. Record source and license information in the manifest.
12. Keep the default packet offline and pencil-ready.
13. Use deterministic HTML and SVG for required text, labels, formulas, maps, charts, and diagrams.
14. Run schema, standards, answer, rendering, link, and overflow tests after every packet change.
15. Do not mark a packet released until human review fields are complete.
16. Keep functions small, names descriptive, and dependencies limited.
17. Avoid copy-pasted subject logic. Create reusable components with clear parameters.
18. Do not collect student data or add account requirements.
19. Preserve a usable accessible HTML version for every packet.
20. Make small commits with a clear description of the completed task.
```

---

## 21. Starter Codex Prompt

```text
You are building a static, standards-driven publishing system for Texas grab-and-go substitute packets.

Begin by reading:
- docs/PROJECT_PLAN.md
- docs/CONTENT_GUIDE.md
- docs/TEKS_VERIFICATION.md
- CODEX.md

Task:
Create Phase 0 only. Set up the repository structure, JSON Schemas, standards source index, standards-lock format, validation scripts, tests, and documentation. Do not author student packets yet.

Requirements:
- Use TypeScript and current Node.js LTS.
- Use YAML for packet manifests and JSON for normalized standards.
- Validate with JSON Schema and Ajv.
- Add records only from current official TEA or Texas Administrative Code sources.
- Store exact source URLs and verification dates.
- Keep standard grades 6–8 mathematics separate from Middle School Advanced Mathematics.
- Include current grades 6–8 RLA, mathematics, science, and social studies sections and the current Grades 4–12 ELPS.
- Never guess missing student expectations. Mark an item pending and stop rather than inventing text.
- Add unit tests for valid and invalid records.
- Add npm scripts for validate, test, and build.
- Document the exact commands in README.md.

Acceptance criteria:
- `npm test` passes.
- `npm run validate` passes.
- No packet content is created.
- Every normalized standards file validates.
- Every record includes a source URL and verified date.
- The repository contains no generated PDFs or temporary files.
- Summarize the files created, tests run, and any standards items left pending.
```

---

## 22. Second Codex Prompt: Rendering Proof

```text
Implement Phase 1 of the substitute packet project.

Read the project documentation and existing schemas first. Do not change verified standards records unless a source correction is required.

Build:
- Nunjucks templates for substitute guide, student packet, answer key, and teacher master
- Shared print and screen CSS
- A fixture packet that uses placeholder instructional content and no released TEKS claim
- HTML rendering
- PDF rendering with Playwright
- Preview rendering
- Automated checks for missing assets, broken links, unexpected page size, blank pages, and printable overflow
- Tests for the rendering pipeline

Requirements:
- US Letter output
- Selectable text
- Grayscale-safe design
- Semantic HTML
- No external runtime dependency for a reader opening the HTML
- Student and answer-key outputs must remain separate
- Generated files must never be edited by hand

Acceptance criteria:
- One command creates the fixture HTML, student PDF, substitute guide PDF, answer key PDF, teacher master PDF, preview image, and manifest
- All tests pass
- No content clips in the PDF
- The HTML reflows at 200 percent zoom and on a narrow screen
- Print output uses no required color-only meaning
```

---

## 23. Third Codex Prompt: First Real Packet

```text
Implement Phase 2 by creating one complete Grade 7 science substitute packet on thermal energy transfer.

Before writing:
1. Locate and verify the exact current Grade 7 science TEKS from the standards lock.
2. Select one primary student expectation and no more than three supporting expectations.
3. Write an alignment rationale that explains how the student task performs the verbs in the selected expectations.
4. Stop and report an error if the required TEKS record is missing or pending.

Packet requirements:
- 45-minute core activity and 15-minute extension
- Pencil and printed packet only
- Independent work by default
- One school-building temperature scenario
- One original diagram or data table
- Observation and inference task
- Short reference section
- Thermal-transfer analysis
- CER response
- ACE close
- Separate substitute guide
- Separate answer key with acceptable alternate responses and a three-point CER rubric
- Accessible HTML and all PDF outputs
- Original text and original SVG graphics only

Validation:
- Every question has a stable ID
- Every question is keyed
- No answer appears in the student file
- All source and license fields are complete
- All automated checks pass
- Render and inspect every page at full size
- Report actual page counts and the commands used
```

---

## 24. Review Log Template

```markdown
# Packet Review Log

## Packet

- Packet ID:
- Title:
- Grade or course:
- Subject:
- Version:
- Review date:

## Standards Review

- Reviewer:
- Primary TEKS verified:
- Supporting TEKS verified:
- Alignment rationale accurate:
- Required correction:

## Content Review

- Reviewer:
- Packet solved independently:
- Completion time:
- Incorrect or ambiguous items:
- Missing information:
- Alternate answers:
- Grade-level concerns:
- Required correction:

## Substitute Usability Review

- Reviewer:
- Guide understood in five minutes:
- Directions require subject expertise:
- Timing realistic:
- Classroom-management concern:
- Required correction:

## Print and Accessibility Review

- Reviewer:
- Grayscale print passed:
- Text size passed:
- Writing space passed:
- No clipping or blank pages:
- Color-independent meaning:
- HTML keyboard and zoom check passed:
- Required correction:

## Release Decision

- Approved:
- Approved with corrections:
- Not approved:
- Final reviewer:
- Final date:
```

---

## 25. Official Sources to Lock Before Development

Use these pages as starting points and follow their current official links.

- TEKS hub: https://tea.texas.gov/curriculum-and-instruction/texas-essential-knowledge-and-skills-teks
- Reading Language Arts: https://tea.texas.gov/educators/subject-areas/english-language-arts-and-reading
- Mathematics: https://tea.texas.gov/educators/subject-areas/mathematics
- Science: https://tea.texas.gov/educators/subject-areas/science/science
- Social Studies: https://tea.texas.gov/educators/subject-areas/social-studies/social-studies
- 19 TAC Chapter 110: https://tea.texas.gov/laws-and-rules/texas-administrative-code/19-tac-chapter-110
- 19 TAC Chapter 111: https://tea.texas.gov/laws-and-rules/texas-administrative-code/19-tac-chapter-111
- 19 TAC Chapter 112: https://tea.texas.gov/laws-and-rules/texas-administrative-code/19-tac-chapter-112
- 19 TAC Chapter 113: https://tea.texas.gov/laws-and-rules/texas-administrative-code/19-tac-chapter-113
- TEKS implementation page: https://tea.texas.gov/curriculum-and-instruction/curriculum-standards/teks-review/teks-implementation
- Middle School Advanced Mathematics: https://tea.texas.gov/curriculum-and-instruction/curriculum-standards/teks-review/2024-middle-school-advanced-mathematics-teks-review

Before each major release:

1. Revisit the source pages.
2. Compare adoption, amendment, and implementation information.
3. Update `standards-lock.json`.
4. Run the standards-diff report.
5. Manually review every packet affected by a changed record.
6. Rebuild the PDFs and catalog.
7. Record the new verification date.

---

## 26. Recommended First Decision

Start with the Grade 7 science vertical slice.

It will test nearly every part of the system:

- Standards ingestion
- Data and diagram rendering
- Subject vocabulary
- Evidence-based writing
- Answer-key rubrics
- Grayscale printing
- Substitute directions
- ACE closure
- Accessible HTML
- PDF generation

Once that packet passes review, build the other three Grade 7 subject packets. Only then should Codex replicate the system across grades 6 and 8.
