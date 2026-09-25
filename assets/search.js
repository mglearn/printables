/* Home-page search across every printable.
   Reads the supplemental-aids manifests (already loaded on the home page) for
   sheet-level results that deep-link to the exact card (#sheet-<base>), plus a
   short static list of the other collections. Pure client-side, no dependencies. */
(function () {
  'use strict';

  // Sheet-level sources — { manifest global, collection path, display label }.
  var SRC = [
    { g: 'SA_MANIFEST', path: 'supplemental_aids/',              label: 'Science Visual Cue Cards (6–8)' },
    { g: 'MA_MANIFEST', path: 'supplemental_aids_math/',         label: 'Math Visual Cue Cards (6–8)' },
    { g: 'ES_MANIFEST', path: 'supplemental_aids_elem_science/', label: 'Elementary Science Visual Cue Cards (3–5)' },
    { g: 'EM_MANIFEST', path: 'supplemental_aids_elem_math/',    label: 'Elementary Math Visual Cue Cards (3–5)' }
  ];

  // Collections without a sheet-level manifest — searchable at the collection level.
  var COLLS = [
    { title: 'Literature Circles Launch Kit', label: 'Reading & Language Arts', url: 'litcircles/index.html',
      blurb: 'grades 5-12 literature circle organization teacher setup TEKS approved texts Aesop reciprocal teaching jigsaw reading schedule student handouts discussion' },
    { title: 'Phase Change Station Lab', label: 'Science', url: 'phase_change_stations/index.html',
      blurb: 'seven hands-on middle school science stations melting condensation evaporation deposition freezing sublimation particle model' },
    { title: 'CER & ACE Case Files', label: 'Science', url: 'https://mglearn.github.io/activities/science/case-files/',
      blurb: 'claim evidence reasoning articulate connect extend hands-on cases grades 5-8' },
    { title: 'ELE Activity Packets', label: 'Digital Citizenship, AI & Media Literacy', url: 'ele-packets/index.html',
      blurb: 'print-ready handout packets gen ai literacy artificial intelligence chatbot digital citizenship privacy scams phishing passwords cyberbullying media literacy misinformation deepfakes lateral reading screen time card sort grades k-2 3-5 6-8 9-12 higher ed college professional learning teachers coaches leaders spanish vietnamese' },
    { title: 'ELE Activity Bank', label: 'Digital Citizenship, AI & Media Literacy', url: 'https://mglearn.github.io/eles/',
      blurb: 'tcea essential learning expectations eles professional learning k-16 activities facilitator guides teks elps udl student success tool sst ai literacy digital citizenship media literacy coaching' },
    { title: 'Texas Grab-and-Go Substitute Packets', label: 'Substitute Plans', url: 'substitute_packets/index.html',
      blurb: 'print and go substitute lessons reading math science social studies grades 3-12 emergency sub plans' },
    { title: 'Student Refusal Forms', label: 'Classroom Management', url: 'srf/index.html',
      blurb: 'meme gaming content-area reflection sheets refusal i am not doing this' },
    { title: 'Get To Know You (GTKY)', label: 'Classroom Management', url: 'https://mglearn.github.io/gtky/',
      blurb: 'icebreakers back to school getting to know you' }
  ];

  function base(file) { return String(file).replace(/\.[a-z0-9]+$/i, ''); }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  var items = [];
  SRC.forEach(function (s) {
    (window[s.g] || []).forEach(function (w) {
      items.push({
        title: w.title, coll: s.label, strand: w.strand || '', blurb: w.blurb || '',
        url: s.path + 'index.html#sheet-' + base(w.file)
      });
    });
  });
  COLLS.forEach(function (c) {
    items.push({ title: c.title, coll: c.label, strand: 'Collection', blurb: c.blurb, url: c.url });
  });

  var input = document.getElementById('site-search-input');
  var out = document.getElementById('site-search-results');
  var section = document.getElementById('collections');
  if (!input || !out) return;

  function render(raw) {
    var q = raw.trim().toLowerCase();
    if (q.length < 2) {
      out.hidden = true; out.innerHTML = '';
      if (section) section.classList.remove('searching');
      return;
    }
    if (section) section.classList.add('searching');
    var terms = q.split(/\s+/);
    var hits = items.filter(function (it) {
      var hay = (it.title + ' ' + it.coll + ' ' + it.strand + ' ' + it.blurb).toLowerCase();
      return terms.every(function (t) { return hay.indexOf(t) !== -1; });
    });
    // Title-prefix matches first.
    hits.sort(function (a, b) {
      var ap = a.title.toLowerCase().indexOf(terms[0]) === 0 ? 0 : 1;
      var bp = b.title.toLowerCase().indexOf(terms[0]) === 0 ? 0 : 1;
      return ap - bp;
    });
    if (!hits.length) {
      out.innerHTML = '<p class="search-empty">No printables match “' + esc(raw.trim()) + '”.</p>';
      out.hidden = false; return;
    }
    var shown = hits.slice(0, 40);
    var html = '<p class="search-count">' + hits.length + ' result' + (hits.length === 1 ? '' : 's') +
      (hits.length > 40 ? ' (showing 40)' : '') + '</p>';
    shown.forEach(function (it) {
      var meta = esc(it.coll) + (it.strand && it.strand !== 'Collection' ? ' · ' + esc(it.strand) : '');
      html += '<a class="search-hit" href="' + esc(it.url) + '">' +
        '<span class="h-title">' + esc(it.title) + '</span>' +
        '<span class="h-meta">' + meta + '</span></a>';
    });
    out.innerHTML = html; out.hidden = false;
  }

  input.addEventListener('input', function () { render(input.value); });
  // If the page was opened with ?q=… (e.g., a shared search), prefill and run.
  var m = /[?&]q=([^&]+)/.exec(location.search);
  if (m) { input.value = decodeURIComponent(m[1].replace(/\+/g, ' ')); render(input.value); }
})();
