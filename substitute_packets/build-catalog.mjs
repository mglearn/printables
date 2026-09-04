// Build catalog.json + catalog.csv from every packet manifest.json.
// Run from substitute_packets/ (build.sh calls it). Reads Gxx_*/manifest.json,
// normalizes fields that vary between packets, and records which generated files
// exist so the catalog only advertises what actually built.
import { readdirSync, readFileSync, existsSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const ROOT = new URL(".", import.meta.url).pathname;
const dirs = readdirSync(ROOT, { withFileTypes: true })
  .filter((d) => d.isDirectory() && /^G\d{2}_/.test(d.name))
  .map((d) => d.name)
  .sort();

const SUBJECT_NAME = { rla: "Reading/ELA", math: "Mathematics", science: "Science", social: "Social Studies", sci: "Science", soc: "Social Studies" };
const val = (v) => (v == null ? "" : String(v));

const records = [];
for (const id of dirs) {
  const mfPath = join(ROOT, id, "manifest.json");
  if (!existsSync(mfPath)) { console.warn(`  ! ${id}: no manifest.json — skipped`); continue; }
  let m;
  try { m = JSON.parse(readFileSync(mfPath, "utf8")); }
  catch (e) { console.warn(`  ! ${id}: invalid manifest (${e.message}) — skipped`); continue; }

  const grade = m.grade ?? m.audience?.grade ?? Number((id.match(/^G(\d{2})/) || [])[1]) ?? null;
  const subjRaw = (typeof m.subject === "object" ? (m.subject.code || m.subject.name) : m.subject) || (id.split("_")[1] || "").toLowerCase();
  const subjKey = String(subjRaw).toLowerCase();
  const subject = SUBJECT_NAME[subjKey] || (typeof m.subject === "object" ? m.subject.name : subjRaw) || subjKey;

  const std = (m.standards?.primary || []).map((s) => ({
    code: val(s.code || s.display_code),
    section: val(s.section),
    status: val(s.verification_status || s.status || "pending"),
  }));

  // Which artifacts exist on disk?
  const has = (suffix) => existsSync(join(ROOT, id, id + suffix));
  const files = {
    html: existsSync(join(ROOT, id, "index.html")) ? `${id}/index.html` : null,
    student_pdf: has("_Student.pdf") ? `${id}/${id}_Student.pdf` : null,
    subguide_pdf: has("_SubGuide.pdf") ? `${id}/${id}_SubGuide.pdf` : null,
    answerkey_pdf: has("_AnswerKey.pdf") ? `${id}/${id}_AnswerKey.pdf` : null,
    teacher_master_pdf: has("_TeacherMaster.pdf") ? `${id}/${id}_TeacherMaster.pdf` : null,
    preview: has("_Preview.webp") ? `${id}/${id}_Preview.webp` : null,
  };

  const ss = std.map((s) => s.status);
  const standardsStatus = std.length === 0 ? "none"
    : ss.every((s) => s === "verified") ? "verified"
    : ss.every((s) => s === "pending") ? "pending"
    : ss.some((s) => s === "pending") ? "mixed"
    : "code-verified";
  records.push({
    id,
    title: val(m.title),
    grade,
    subject,
    subject_key: subjKey.replace("sci", "science").replace("soc", "social"),
    duration_minutes: m.duration?.core_minutes ?? null,
    extension_minutes: m.duration?.extension_minutes ?? null,
    materials: m.materials?.required || m.materials || [],
    calculator_allowed: m.calculator_allowed ?? m.accessibility?.calculator_allowed ?? false,
    color_required: m.color_required ?? m.accessibility?.color_required ?? false,
    standards: std,
    standards_status: standardsStatus,
    status: val(m.status || "draft"),
    version: val(m.version || "0.1.0"),
    href: `${id}/index.html`,
    files,
  });
}

writeFileSync(join(ROOT, "catalog.json"),
  JSON.stringify({ generated: null, count: records.length, packets: records }, null, 2) + "\n");

// CSV (flat, spreadsheet-friendly)
const cols = ["id", "title", "grade", "subject", "duration_minutes", "calculator_allowed", "standards", "standards_status", "status", "version", "href"];
const esc = (v) => { const s = Array.isArray(v) ? v.map((x) => x.code || x).join("; ") : String(v ?? ""); return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s; };
const csv = [cols.join(",")].concat(records.map((r) => cols.map((c) => esc(r[c])).join(","))).join("\n") + "\n";
writeFileSync(join(ROOT, "catalog.csv"), csv);

console.log(`catalog: ${records.length} packets → catalog.json + catalog.csv`);
for (const r of records) console.log(`  ${r.id.padEnd(30)} G${r.grade} ${r.subject.padEnd(14)} ${r.files.student_pdf ? "pdf" : "html-only"} · standards ${r.standards_status}`);
