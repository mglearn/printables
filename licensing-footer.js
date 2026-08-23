/* ============================================================
   Teachers Give Teachers (TGT) — licensing footer (unobtrusive)
   Appends a quiet one-line licensing notice to the end of the
   page, linking to /tgt/licensing.html. Injects its own scoped
   styles so it cannot clash with a page's existing CSS.

   Include on a page with:
     <script src="/tgt/licensing-footer.js" defer></script>

   The path is absolute, so the same tag works at any folder
   depth (the hub root and the collection sub-folders). To change
   the license shown site-wide, edit LICENSE_TEXT / HOLDER below —
   the pages themselves need no changes.
   ============================================================ */
(function () {
  "use strict";

  var HOLDER       = "© 2026 TCEA";
  var LICENSE_TEXT = "Content CC BY-NC 4.0 · Code MIT";
  var HREF         = "/tgt/licensing.html";

  // Never inject inside an embedded iframe — the host page carries it.
  try { if (window.top !== window.self) return; } catch (e) { return; }

  // Never inject on the licensing page itself.
  if (/\/licensing\.html$/.test(location.pathname)) return;

  function build() {
    if (document.getElementById("tgt-lic-footer")) return;

    var css = ""
      + "#tgt-lic-footer{all:initial;display:block;box-sizing:border-box;width:100%;"
      + "margin:0;padding:.9rem 1rem calc(.9rem + env(safe-area-inset-bottom,0px));"
      + "border-top:1px solid rgba(15,118,110,.18);background:#eef5f2;text-align:center;"
      + "font-family:'Segoe UI',system-ui,-apple-system,Roboto,'Helvetica Neue',Arial,sans-serif;"
      + "font-size:.76rem;line-height:1.6;color:#4b5b60;}"
      + "#tgt-lic-footer .tgt-lic-in{max-width:820px;margin:0 auto;}"
      + "#tgt-lic-footer a{color:#0a4f4a;font-weight:700;text-decoration:underline;text-underline-offset:2px;}"
      + "#tgt-lic-footer a:hover,#tgt-lic-footer a:focus-visible{color:#0f766e;}"
      + "@media print{#tgt-lic-footer{border-top:1px solid #ccc;background:transparent;color:#333;}}";

    var style = document.createElement("style");
    style.id = "tgt-lic-footer-css";
    style.appendChild(document.createTextNode(css));
    document.head.appendChild(style);

    var bar = document.createElement("footer");
    bar.id = "tgt-lic-footer";

    var inner = document.createElement("div");
    inner.className = "tgt-lic-in";
    inner.appendChild(document.createTextNode(HOLDER + " · " + LICENSE_TEXT + " · "));

    var link = document.createElement("a");
    link.href = HREF;
    link.textContent = "Licensing & provenance";
    inner.appendChild(link);

    bar.appendChild(inner);
    document.body.appendChild(bar);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", build);
  } else {
    build();
  }
})();
