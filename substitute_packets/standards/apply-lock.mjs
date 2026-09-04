// Rewrite each packet manifest's standards.primary from standards-lock.json.
// Matches by subject + display_code (display codes like "6.6C" collide across
// subjects, so subject disambiguates). Sets verification_status from the lock,
// flipping manifests off the authors' "pending" placeholders. Idempotent.
// Usage: node standards/apply-lock.mjs   (run from substitute_packets/)
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = join(HERE, "..");
const lock = JSON.parse(readFileSync(join(HERE, "standards-lock.json"), "utf8"));

const SUBJ = { RLA: "rla", MATH: "math", SCI: "science", SOC: "social" };
const bySubjCode = new Map();          // "science|6.6C" -> record
const byCode = new Map();              // "6.6C" -> record (fallback)
for (const r of lock.standards) {
  bySubjCode.set(r.subject + "|" + r.display_code, r);
  if (!byCode.has(r.display_code)) byCode.set(r.display_code, r);
}

let changed = 0;
for (const [pid, codes] of Object.entries(lock.packet_map || {})) {
  const mf = join(ROOT, pid, "manifest.json");
  if (!existsSync(mf)) { console.warn(`  ! ${pid}: no manifest`); continue; }
  const m = JSON.parse(readFileSync(mf, "utf8"));
  const subj = SUBJ[(pid.split("_")[1] || "").toUpperCase()] || m.subject;   // HS_* folders: use manifest subject

  const primary = codes.map((dc) => {
    const rec = bySubjCode.get(subj + "|" + dc) || byCode.get(dc);
    if (!rec) { console.warn(`  ! ${pid}: ${dc} not in lock`); return { code: dc, verification_status: "pending" }; }
    return {
      code: rec.display_code,
      canonical_code: rec.code,
      section: rec.section,
      strand: rec.strand || null,
      focus: rec.focus,
      verification_status: rec.status,      // verified | code-verified
      source_url: rec.source_url,
    };
  });

  m.standards = m.standards || {};
  delete m.standards.alignment_note;   // stale free-text note superseded by verified per-SE records
  delete m.alignment_note;
  m.standards.primary = primary;
  if (!Array.isArray(m.standards.supporting)) m.standards.supporting = [];
  m.standards.lock = "standards/standards-lock.json";
  m.standards.verified_on = lock.verified_on || null;

  writeFileSync(mf, JSON.stringify(m, null, 2) + "\n");
  const st = primary.map((p) => p.code + ":" + p.verification_status).join(", ");
  console.log(`  ${pid.padEnd(30)} ${st}`);
  changed++;
}
console.log(`\nupdated ${changed} manifests from the lock.`);
