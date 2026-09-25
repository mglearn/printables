# Human QA Checklist

Per spec section 15. Every test-use candidate must pass this review in addition to
the automated linter (`tools/lint_aids.py`). The linter is a mechanical backstop;
it does not replace human judgment or local testing review.

## Content
- [ ] Fits a currently permitted TEA supplemental-aid type
- [ ] Contains no prohibited words
- [ ] Contains no prohibited labels
- [ ] Contains no prohibited numbers
- [ ] Contains no prohibited variables
- [ ] Contains no prohibited symbols
- [ ] Contains no prohibited semantic color coding
- [ ] Contains no answer
- [ ] Contains no worked example
- [ ] Contains no test-taking strategy
- [ ] Contains no problem-solving procedure
- [ ] Is error-free
- [ ] Is concise
- [ ] Is easily interpreted by a student already trained to use it

## Science Formula Triangles
- [ ] Formula appears on the appropriate current state-supplied reference material
- [ ] Only variables appear
- [ ] No operation symbols appear
- [ ] No formula name appears
- [ ] No units appear

## Mathematics
- [ ] Resource fits one of TEA's currently listed mathematics categories
- [ ] Number chart contains no highlighted special numbers
- [ ] Place-value chart contains no word labels or sample numbers
- [ ] Fraction model contains no fraction/equivalency labels
- [ ] Geometry resource contains no labels or measurements
- [ ] Two-dimensional / three-dimensional restrictions have been checked

## Documentation
- [ ] TEA source checked
- [ ] Source date recorded
- [ ] Testing year recorded
- [ ] Local review still required
- [ ] Resource is not described as TEA approved

---

## Notes for this build (2026-09-25)

- Three aids are held at `NEEDS TEA/LOCAL VERIFICATION` pending human judgment on
  ambiguity/format: moon phases (grayscale illumination), plate-boundary
  cross-sections (no motion arrows), and the pictorial simple circuit. If local
  review finds any of these ambiguous or teacher-dependent, move them to
  `classroom-only/` per section 11 step 5.
