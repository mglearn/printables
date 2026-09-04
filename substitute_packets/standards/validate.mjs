// Validate standards-lock.json against standard.schema.json (no deps: hand-rolled checks).
// Also cross-checks that every packet manifest's cited display_code exists in the lock.
// Usage: node standards/validate.mjs   (run from substitute_packets/)
import { readFileSync, readdirSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = join(HERE, "..");
const schema = JSON.parse(readFileSync(join(HERE, "schemas", "standard.schema.json"), "utf8"));
const lock = JSON.parse(readFileSync(join(HERE, "standards-lock.json"), "utf8"));

let errors = 0;
const fail = (m) => { console.error("  ✗ " + m); errors++; };
const req = schema.required;
const enums = { subject: schema.properties.subject.enum, status: schema.properties.status.enum };

const records = lock.standards || [];
const byCode = new Map();
for (const r of records) {
  const id = r.display_code || r.code || "(unknown)";
  for (const k of req) if (r[k] === undefined || r[k] === null || r[k] === "") fail(`${id}: missing required "${k}"`);
  if (r.subject && !enums.subject.includes(r.subject)) fail(`${id}: bad subject "${r.subject}"`);
  if (r.status && !enums.status.includes(r.status)) fail(`${id}: bad status "${r.status}"`);
  if (r.verified_on && !/^\d{4}-\d{2}-\d{2}$/.test(r.verified_on)) fail(`${id}: bad verified_on "${r.verified_on}"`);
  if (r.source_url && !/^https?:\/\//.test(r.source_url)) fail(`${id}: source_url not a URL`);
  if (r.status === "verified" && !r.student_expectation) fail(`${id}: status "verified" requires exact student_expectation wording`);
  if (r.display_code) byCode.set(r.display_code, r);
}

// Cross-check manifests
let manifestChecks = 0;
for (const d of readdirSync(ROOT, { withFileTypes: true })) {
  if (!d.isDirectory() || !/^G\d{2}_/.test(d.name)) continue;
  const mf = join(ROOT, d.name, "manifest.json");
  if (!existsSync(mf)) continue;
  let m; try { m = JSON.parse(readFileSync(mf, "utf8")); } catch { fail(`${d.name}: manifest not valid JSON`); continue; }
  for (const s of (m.standards?.primary || [])) {
    manifestChecks++;
    if (s.code && /^\d/.test(s.code) && !byCode.has(s.code))
      fail(`${d.name}: cites ${s.code} which is not in the standards lock`);
  }
}

const counts = records.reduce((a, r) => { a[r.status] = (a[r.status] || 0) + 1; return a; }, {});
console.log(`standards-lock: ${records.length} records — ${JSON.stringify(counts)}; ${manifestChecks} manifest citations checked`);
if (errors) { console.error(`\n${errors} problem(s).`); process.exit(1); }
console.log("OK — lock and manifests are consistent.");
