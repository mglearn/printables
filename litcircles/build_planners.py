#!/usr/bin/env python3
"""Generate per-title Literature Circle planners (worked + blank) for the kit.

Each title yields two US Letter pages in two versions:
  planners/<slug>.html        worked example (sample answers shown in tinted italic)
  planners/<slug>-blank.html  blank companion (teacher scaffolds kept; student fields empty)

Layout and CSS match packet.css. Render to PDF with headless Chrome:
  --print-to-pdf --no-pdf-header-footer  (US Letter, 100%).

Copyrighted titles: paraphrase-only worked prep, no quotations, disclaimer callout,
no Gutenberg link, mark uncertain plot points "verify against the text".
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "planners"
OUT.mkdir(exist_ok=True)

DISCLAIMER = {
 "giver": "Independent educational companion to <i>The Giver</i> by Lois Lowry. Students need lawful access to the novel; this planner does not reproduce or replace it and is not affiliated with the author or publisher. Verify all plot details against the book.",
 "kindred": "Independent educational companion to <i>Kindred</i> by Octavia E. Butler. Students need lawful access to the novel; this planner does not reproduce or replace it and is not affiliated with the author's estate or publisher. Verify all plot details against the book.",
 "bnw": "Independent educational companion to <i>Brave New World</i> by Aldous Huxley. Students need lawful access to the novel; this planner does not reproduce or replace it and is not affiliated with the author's estate or publisher. Verify all plot details against the book.",
}

# ---- Title data -----------------------------------------------------------
# Each entry: keys documented inline. q = 5 open questions (predict/question/
# clarify/summarize/interpret). lenses = jigsaw lens list. prep = worked 3-2-1.
TITLES = [
 {
  "slug":"magi","title":"The Gift of the Magi","author":"O. Henry","year":"1905",
  "band":"grades 7–10","genre":"public-domain short story","pace":"~1 week / two meetings",
  "room":"magi","rights":"Public domain",
  "teks":"Grade 8 · §110.24 — 7(A): theme through characters/events; 6(C,D): support inferences; 1(D): student-led discussion.",
  "li":"We are learning to explain how the characters’ choices reveal a theme about love and value.",
  "sc":"I bring one open question, cite two details with paragraph numbers, respond to a peer, and name how my thinking changed.",
  "chunks":[("1","Opening through Della selling her hair and buying the watch chain (≈ paragraphs 1–20).","Tue · Leader: Maya"),
            ("2","Jim arrives home through the closing “magi” paragraph — the double reveal (≈ paragraphs 21–end).","Thu · Leader: Devon")],
  "roles":[("Maya","Questioner","Summarizer"),("Devon","Summarizer","Clarifier"),("Priya","Clarifier","Evidence tracker"),("Luis","Predictor","Questioner")],
  "q":["After Della counts $1.87 the day before Christmas, what will she risk to give Jim a worthy gift? What clue supports your guess?",
       "Why might the narrator step in to compare Della and Jim to the magi? How does that change how we judge their choices?",
       "What does the narrator mean that they “most unwisely sacrificed the greatest treasures”? Is it really unwise?",
       "Each sold the one thing the other’s gift was meant for — restate that irony in order, without opinion.",
       "How do their choices reveal what the story says about love versus money? Use two details."],
  "lenses":[("Character","Della’s and Jim’s choices"),("Plot","the parallel sacrifices, twist ending"),("Language","the intruding narrator"),("Theme","value isn’t material"),("Point of view","the narrator’s direct address (5th reader)")],
  "prep":{"name":"Priya","lens":"Character choices","chunk":"Chunk 2",
    "ideas":["Jim sells his gold watch — his most prized possession — to buy Della combs.",
             "Della had already cut and sold her long hair to buy Jim a chain for that watch.",
             "Neither can use the gift they receive, yet both are moved, not angry."],
    "details":["When Jim sees Della’s short hair he goes still — shock, not anger (the reveal). → His love isn’t about her appearance.",
               "The combs Della had “coveted” are now useless without her hair (the reveal). → The gift’s worth is in the sacrifice."],
    "vocab":["coveted = wanted badly for a long time.","the magi = the wise gift-bringers of the Christmas story."],
    "summary":"Both Della and Jim secretly sold their most treasured thing to buy the other a Christmas gift. The gifts can’t even be used — but the love and sacrifice behind them is the real point.",
    "interp":"These details suggest the story measures love by what people give up, not by what they spend.",
    "synth":"The parallel sacrifices (plot) create the irony that proves the theme: value lives in the sacrifice, not the object. Text points: Della’s haircut in Chunk 1 and Jim’s sold watch in Chunk 2."}},

 {
  "slug":"necklace","title":"The Necklace","author":"Guy de Maupassant","year":"1884",
  "band":"grades 8–10","genre":"public-domain short story","pace":"~1 week / two meetings",
  "room":"necklace","rights":"Public domain",
  "teks":"Grade 8 · §110.24 — 7(A): theme through characters/events; 6(C,D): support inferences; 1(D): student-led discussion.",
  "li":"We are learning to explain how Mathilde’s choices and the story’s irony reveal a theme about vanity and honesty.",
  "sc":"I bring one open question, cite two details with locations, respond to a peer, and name how my thinking changed.",
  "chunks":[("1","Mathilde’s discontent through the ball and the lost necklace.","Tue · Leader: Aisha"),
            ("2","The ten years of debt through Madame Forestier’s final revelation.","Thu · Leader: Marcus")],
  "roles":[("Aisha","Questioner","Summarizer"),("Marcus","Summarizer","Clarifier"),("Lin","Clarifier","Evidence tracker"),("Sam","Predictor","Questioner")],
  "q":["After Mathilde borrows the necklace, what could go wrong — and what detail hints at it?",
       "Why might Maupassant end with Forestier’s revelation? How does it change our view of Mathilde’s suffering?",
       "What does the narrator mean that Mathilde “was made for” a life of luxury? Is that true?",
       "Retell the ten years of repayment in order, without opinion.",
       "How do Mathilde’s choices and the twist reveal a theme about vanity or honesty? Use two details."],
  "lenses":[("Character","Mathilde and her husband"),("Plot","the ironic twist"),("Language","the narrator’s judgments"),("Theme","pride vs. contentment"),("Point of view","whose viewpoint is missing — Forestier’s (5th reader)")],
  "prep":{"name":"Lin","lens":"Plot / irony","chunk":"Chunk 2",
    "ideas":["The Loisels replace the lost necklace with a real diamond one costing 36,000 francs.",
             "They spend ten years in poverty repaying the debt.",
             "At the end, Forestier reveals the borrowed necklace was only paste (fake)."],
    "details":["The narrator notes Mathilde grew “hard” and coarse from labor (later part). → The cost fell on her looks and life.",
               "Forestier says the necklace was worth at most 500 francs (ending). → The sacrifice rested on a false assumption."],
    "vocab":["paste = imitation gems.","discontent = restless unhappiness."],
    "summary":"Mathilde loses a borrowed necklace, and the family ruins itself for ten years to replace it — only to learn it was fake.",
    "interp":"The story suggests that pride and pretending cost far more than honesty would have.",
    "synth":"The ironic twist (plot) proves the theme: Mathilde’s refusal to admit the loss (character) turns one night’s vanity into a decade of ruin. Text points: the ball (Chunk 1) and Forestier’s revelation (Chunk 2)."}},

 {
  "slug":"tobuildafire","title":"To Build a Fire","author":"Jack London","year":"1908",
  "band":"grades 8–11","genre":"public-domain short story","pace":"~1 week / two meetings",
  "room":"tobuildafire","rights":"Public domain",
  "teks":"English I · §110.36 — 6(A): theme through characterization/plot; 5(C,D): commentary and summary; 1(D): student-led discussion.",
  "li":"We are learning to explain how the man’s choices and the setting reveal a theme about nature and human pride.",
  "sc":"I bring one open question, cite two details with locations, respond to a peer, and name how my thinking changed.",
  "chunks":[("1","The man sets out at 75-below despite the old-timer’s warning, and breaks through the ice.","Tue · Leader: Noah"),
            ("2","The failed fires, the growing panic, and the ending — the dog moves on.","Thu · Leader: Elena")],
  "roles":[("Noah","Questioner","Summarizer"),("Elena","Summarizer","Clarifier"),("Ravi","Clarifier","Evidence tracker"),("Grace","Predictor","Questioner")],
  "q":["After the man ignores the old-timer’s advice, what will the cold force him to face? What clue supports it?",
       "Why might London give the dog instincts the man lacks? What does that contrast argue?",
       "What does “the trouble with him was that he was without imagination” mean for his fate?",
       "Order the man’s attempts to survive after he gets wet, without opinion.",
       "How do the man’s choices and the setting reveal a theme about nature vs. pride? Use two details."],
  "lenses":[("Character","the man and the dog"),("Setting","the Yukon cold as antagonist"),("Plot","the chain of small errors"),("Theme","instinct vs. arrogance"),("Language","repetition of temperature and warnings")],
  "prep":{"name":"Ravi","lens":"Setting","chunk":"Chunk 2",
    "ideas":["The cold is an active force, not just a backdrop.",
             "Small mistakes — getting wet, a badly placed fire — turn fatal.",
             "The dog reads danger the man dismisses."],
    "details":["The man’s spittle crackles in the air (early). → Shows how extreme and deadly the cold is.",
               "Snow from the spruce buries his fire (middle). → Nature punishes his haste."],
    "vocab":["conjectural = based on guessing.","apprehension = uneasy awareness of danger."],
    "summary":"A man travels alone in deadly cold, ignores a warning, and dies after failing to keep a fire; the dog moves on.",
    "interp":"Nature is indifferent; survival needs humility and instinct, not confidence.",
    "synth":"The environment (setting) enacts the theme: pride without imagination cannot survive an indifferent nature. Text points: the crackling cold (Chunk 1) and the buried fire (Chunk 2)."}},

 {
  "slug":"telltale","title":"The Tell-Tale Heart","author":"Edgar Allan Poe","year":"1843",
  "band":"grades 8–11","genre":"public-domain short story","pace":"~1 week / two meetings",
  "room":"poe","rights":"Public domain",
  "teks":"Grade 8 · §110.24 — 7(A): theme through characters/events; 6(C,D): support inferences; 1(D): student-led discussion.",
  "li":"We are learning to explain how the narrator’s unreliable voice reveals a theme about guilt and the mind.",
  "sc":"I bring one open question, cite two details with locations, respond to a peer, and name how my thinking changed.",
  "chunks":[("1","The plan, the seven nights of watching, and the killing.","Tue · Leader: Omar"),
            ("2","The police visit and the confession.","Thu · Leader: Bea")],
  "roles":[("Omar","Questioner","Summarizer"),("Bea","Summarizer","Clarifier"),("Kai","Clarifier","Evidence tracker"),("Zoe","Predictor","Questioner")],
  "q":["The narrator insists he is sane — what will his behavior reveal instead? What clue hints at it?",
       "Why might Poe let the narrator tell his own story? How does that shape our trust?",
       "What is the “beating” the narrator hears at the end — literal or guilt?",
       "Order the events of the night of the murder, without opinion.",
       "How does the narrator’s voice reveal a theme about guilt or madness? Use two details."],
  "lenses":[("Character","the narrator"),("Point of view","unreliable first person"),("Language","repetition, dashes, exclamation"),("Plot","control unraveling"),("Theme","guilt and conscience")],
  "prep":{"name":"Kai","lens":"Point of view","chunk":"Chunk 2",
    "ideas":["The narrator claims sanity while describing obsession.",
             "He stalks the old man for seven nights before acting.",
             "He confesses under an imagined heartbeat."],
    "details":["His repeated “nervous — very, dreadfully nervous” (opening) undercuts the sanity claim.",
               "His shriek to the police (ending) shows guilt breaking through his control."],
    "vocab":["acute = sharp, heightened.","dissimulation = hiding true feelings."],
    "summary":"A narrator kills an old man over his “eye,” hides the body, then confesses when he thinks he hears the heart.",
    "interp":"The mind cannot escape its own guilt, no matter how it insists it is calm.",
    "synth":"The unreliable narrator (point of view) proves the theme: his own telling exposes the guilt he denies. Text points: the sanity claim (Chunk 1) and the confession (Chunk 2)."}},

 {
  "slug":"monkeyspaw","title":"The Monkey’s Paw","author":"W. W. Jacobs","year":"1902",
  "band":"grades 7–10","genre":"public-domain short story","pace":"~1 week / two meetings",
  "room":"monkeyspaw","rights":"Public domain",
  "teks":"Grade 7 · §110.23 — 7(A): theme through characters/events; 6(C,D): support inferences; 1(D): student-led discussion.",
  "li":"We are learning to explain how the family’s wishes and the story’s structure reveal a theme about fate and greed.",
  "sc":"I bring one open question, cite two details with locations, respond to a peer, and name how my thinking changed.",
  "chunks":[("1","The paw arrives, Morris’s warning, and the first wish.","Tue · Leader: Dev"),
            ("2","The consequence (Herbert’s death) and the final two wishes.","Thu · Leader: Nora")],
  "roles":[("Dev","Questioner","Summarizer"),("Nora","Summarizer","Clarifier"),("Theo","Clarifier","Evidence tracker"),("Ivy","Predictor","Questioner")],
  "q":["After Mr. White wishes for money, what will “fate rules people’s lives” cost him? What clue hints at it?",
       "Why might Jacobs keep the third wish’s result offstage?",
       "What does Morris mean that the paw grants wishes but with a price?",
       "Order the three wishes and their results, without opinion.",
       "How do the wishes reveal a theme about tempting fate or greed? Use two details."],
  "lenses":[("Character","Mr. and Mrs. White"),("Plot","the three-wish structure and foreshadowing"),("Mood","the storm and the quiet house"),("Theme","fate vs. desire"),("Language","warnings and the knock")],
  "prep":{"name":"Theo","lens":"Plot","chunk":"Chunk 2",
    "ideas":["The paw grants three wishes, but each carries a cost.",
             "The wished-for money arrives as compensation for Herbert’s death.",
             "The parents wish him back, then wish him gone again."],
    "details":["Morris throws the paw on the fire (early). → Warns that the wishes are dangerous.",
               "The knocking stops after the third wish (ending). → Shows the cost of undoing fate."],
    "vocab":["fakir = a holy man.","talisman = an object believed to hold power."],
    "summary":"A family gains a cursed wishing paw; their wishes bring money through their son’s death, and they undo the horror with the last wish.",
    "interp":"Meddling with fate for gain brings ruin, not reward.",
    "synth":"The three-wish structure (plot) enacts the theme: each wish shows that forcing fate exacts a price. Text points: the first wish (Chunk 1) and the last (Chunk 2)."}},

 {
  "slug":"gettysburg","title":"The Gettysburg Address","author":"Abraham Lincoln","year":"1863",
  "band":"grades 6–12","genre":"public-domain speech (nonfiction)","pace":"~2–3 class sessions",
  "room":"gettysburg","rights":"Public domain",
  "teks":"Grade 8 · §110.24 — 9(D): rhetorical devices; 8(D): argument/claim; 1(D): student-led discussion. (Nonfiction: replace the literary focus with your course’s informational/argumentative expectation.)",
  "li":"We are learning to explain how Lincoln’s structure and word choices advance his purpose.",
  "sc":"I bring one open question, cite two details with locations, respond to a peer, and name how my thinking changed.",
  "chunks":[("1","“Four score” — the founding and the present dedication of the cemetery.","Day 1 · Leader: Ana"),
            ("2","The living’s “unfinished work” and the “new birth of freedom.”","Day 2 · Leader: Jon")],
  "roles":[("Ana","Questioner","Summarizer"),("Jon","Summarizer","Clarifier"),("Mia","Clarifier","Evidence tracker"),("Cole","Predictor","Questioner")],
  "q":["A speech at a battlefield cemetery — what will Lincoln ask the living to do? What in the opening hints at it?",
       "Why might Lincoln spend so little time on the dead and more on the living?",
       "What is the “unfinished work” and the “great task remaining”?",
       "State Lincoln’s main claim in one sentence, without opinion.",
       "How do repetition and contrast (past / present / future) advance his purpose? Use two details."],
  "lenses":[("Purpose","why Lincoln speaks"),("Structure","past → present → future"),("Language","repetition: “dedicate,” “we cannot”"),("Rhetoric","appeals to shared ideals"),("Context","the Civil War, 1863")],
  "prep":{"name":"Mia","lens":"Structure","chunk":"whole speech",
    "ideas":["Lincoln opens with the nation’s founding in 1776.",
             "He turns to the present dedication of the cemetery.",
             "He ends by charging the living with the unfinished work."],
    "details":["“Four score and seven years ago” (opening) roots the nation in its founding ideals.",
               "“government of the people, by the people, for the people” (ending) names the goal to preserve."],
    "vocab":["consecrate = to make sacred.","proposition = a claim put forward."],
    "summary":"Lincoln honors the dead briefly, then calls the living to finish the work of preserving a government by the people.",
    "interp":"The speech reframes a burial as a call to continue the nation’s founding ideals.",
    "synth":"The past-present-future structure serves the purpose: by moving from 1776 to “unfinished work,” Lincoln turns mourning into commitment. Text points: the opening and the closing line."}},

 {
  "slug":"yellowwallpaper","title":"The Yellow Wallpaper","author":"Charlotte Perkins Gilman","year":"1892",
  "band":"grades 10–12","genre":"public-domain short story","pace":"~1 week / two meetings",
  "room":"yellowwallpaper","rights":"Public domain",
  "content":"Preview for mental illness and controlling medical/gender dynamics; plan support.",
  "teks":"English III · §110.38 — 6(A): relationships among literary elements; 5(C,D): analytic commentary and summary; 1(D): student-led discussion.",
  "li":"We are learning to explain how the setting and the “rest cure” reveal a theme about autonomy and gender.",
  "sc":"I bring one open question, cite two details with locations, respond to a peer, and name how my thinking changed.",
  "chunks":[("1","Arrival at the house, the wallpaper introduced, and John’s control.","Tue · Leader: Rosa"),
            ("2","The narrator’s growing fixation through the final “creeping.”","Thu · Leader: Will")],
  "roles":[("Rosa","Questioner","Summarizer"),("Will","Summarizer","Clarifier"),("Tara","Clarifier","Evidence tracker"),("Ben","Predictor","Questioner")],
  "q":["The narrator is told to rest and not write — what will forced idleness do to her? What clue hints at it?",
       "Why might Gilman make the wallpaper’s “woman” appear only to the narrator?",
       "What does the narrator mean when she “gets out at last”?",
       "Trace how her view of the wallpaper changes across the story, without opinion.",
       "How do the setting and John’s control reveal a theme about women’s autonomy? Use two details."],
  "lenses":[("Character","the narrator and John"),("Symbol","the wallpaper and its “woman”"),("Point of view","the journal, increasingly unreliable"),("Theme","autonomy and gender"),("Language","the fragmented entries")],
  "prep":{"name":"Tara","lens":"Symbol","chunk":"Chunk 2",
    "ideas":["The wallpaper repels the narrator, then fascinates her.",
             "She comes to see a trapped woman behind the pattern.",
             "She tears the paper to “free” that woman."],
    "details":["She describes the pattern’s “bars” (middle). → Suggests confinement.",
               "She creeps over the fainted John (ending). → A grim reversal of who controls whom."],
    "vocab":["atrocious = shockingly bad.","arabesque = an ornate, winding pattern."],
    "summary":"A woman confined for a “rest cure” fixates on the wallpaper, identifies with a trapped figure in it, and breaks down while claiming freedom.",
    "interp":"Denying a person voice and work can destroy the mind it claims to heal.",
    "synth":"The wallpaper (symbol) carries the theme: the trapped woman mirrors the narrator’s caged autonomy. Text points: the “bars” (Chunk 2) and the final creeping."}},

 {
  "slug":"secretgarden","title":"The Secret Garden","author":"Frances Hodgson Burnett","year":"1911",
  "band":"grades 5–7","genre":"public-domain novel (selected chapters or whole)","pace":"~2–3 weeks",
  "room":None,"rights":"Public domain",
  "content":"Preview colonial attitudes and racist language toward Indian servants, the disability portrayal of Colin, and deaths (cholera, parents); plan context and support.",
  "teks":"Grade 6 · §110.22 — 7(A): multiple themes within/across texts; 6(C,D): support inferences, summary; 1(D): student-led discussion.",
  "li":"We are learning to explain how Mary’s and Colin’s changes reveal a theme about renewal and belonging.",
  "sc":"I bring one open question, cite two details with chapter/page, respond to a peer, and name how my thinking changed.",
  "chunks":[("1","Ch. 1–8: Mary orphaned in India → Misselthwaite → finding the key and the garden.","Wk 1 · Leader: Priya"),
            ("2","Ch. 9–20: reviving the garden, meeting Dickon, discovering Colin.","Wk 2 · Leader: Sam"),
            ("3","Ch. 21–27: Colin’s recovery, the garden restored, Mr. Craven’s return.","Wk 3 · Leader: Aida")],
  "roles":[("Priya","Questioner","Summarizer"),("Sam","Summarizer","Clarifier"),("Aida","Clarifier","Evidence tracker"),("Ken","Predictor","Questioner")],
  "q":["A sour, lonely Mary arrives at a house of secrets — what might the locked garden change in her?",
       "Why might Burnett tie the garden’s revival to the children’s health?",
       "What does “Magic” mean to Colin — supernatural, or something else?",
       "Trace Mary’s change from the opening to the garden’s bloom, without opinion.",
       "How do the garden and the friendships reveal a theme about renewal or belonging? Use two details."],
  "lenses":[("Character","Mary and Colin"),("Symbol","the garden"),("Theme","renewal and nature"),("Plot","secrets revealed"),("Context","Edwardian England — preview colonial attitudes")],
  "prep":{"name":"Aida","lens":"Symbol","chunk":"Chunk 2",
    "ideas":["Mary finds a hidden, neglected garden and begins to tend it.",
             "Caring for it changes her mood and her health.",
             "Colin, believed a hopeless invalid, grows stronger outdoors."],
    "details":["The first green shoots appear (mid-novel). → Mirror Mary’s warming heart.",
               "Colin stands and walks in the garden (late). → Shows the garden’s healing effect."],
    "vocab":["contrary = stubbornly opposed.","moor = open, rolling upland."],
    "summary":"A neglected girl restores a locked garden and, with it, herself and a sickly boy.",
    "interp":"Care for living things heals the one who gives the care.",
    "synth":"The garden (symbol) embodies renewal (theme): as it revives, so do Mary and Colin. Text points: the first shoots (Chunk 2) and Colin walking (Chunk 3)."}},

 {
  "slug":"littlewomen","title":"Little Women","author":"Louisa May Alcott","year":"1868–69",
  "band":"grades 7–9","genre":"public-domain novel (Part 1 or whole)","pace":"~2–3 weeks",
  "room":None,"rights":"Public domain",
  "content":"Preview period gender expectations, religious references, and illness/death (Beth); plan support.",
  "teks":"Grade 8 · §110.24 — 7(A): theme through characters/events; 6(C,D): support inferences, summary; 1(D): student-led discussion.",
  "li":"We are learning to explain how the March sisters’ choices reveal a theme about ambition, family, and sacrifice.",
  "sc":"I bring one open question, cite two details with chapter/page, respond to a peer, and name how my thinking changed.",
  "chunks":[("1","Ch. 1–11: the sisters, “playing pilgrims,” Christmas, and meeting Laurie.","Wk 1 · Leader: Jo"),
            ("2","Ch. 12–23: Beth’s scarlet fever, Meg’s romance, and Father’s return.","Wk 2 · Leader: Meg")],
  "roles":[("Jo","Questioner","Summarizer"),("Meg","Summarizer","Clarifier"),("Beth","Clarifier","Evidence tracker"),("Amy","Predictor","Questioner")],
  "q":["Four sisters vow to bear their “burdens” — which sister’s ambition will cost or reward her most?",
       "Why might Alcott frame the sisters’ growth as a “pilgrim’s progress”?",
       "What does Jo mean by wanting to “do something splendid”?",
       "Trace one sister’s main change in Part 1, without opinion.",
       "How do the sisters’ choices reveal a theme about ambition versus duty? Use two details."],
  "lenses":[("Character","Jo and her sisters"),("Theme","ambition vs. duty"),("Structure","the Pilgrim’s Progress frame"),("Setting","the Civil War home front"),("Language","the narrator’s moral asides")],
  "prep":{"name":"Beth","lens":"Character (Jo)","chunk":"Chunk 1",
    "ideas":["Jo wants independence and to become a writer.",
             "She sacrifices for family — selling her hair to fund Marmee’s trip.",
             "Beth’s illness draws the sisters closer together."],
    "details":["Jo cuts and sells her hair (Part 1). → Shows sacrifice over vanity.",
               "The sisters give their Christmas breakfast to the Hummels (opening). → Duty over comfort."],
    "vocab":["genteel = respectably refined.","penitent = sorry for wrongdoing."],
    "summary":"Four sisters grow up in wartime poverty, each balancing personal ambition with love and duty to family.",
    "interp":"Growing up means balancing one’s own dreams with care for others.",
    "synth":"Jo’s choices (character) carry the theme: her ambition matters, but her sacrifices define her. Text points: the hair (Chunk 1) and the Hummel breakfast (Chunk 1)."}},

 {
  "slug":"douglass","title":"Narrative of the Life of Frederick Douglass","author":"Frederick Douglass","year":"1845",
  "band":"grades 9–12","genre":"public-domain memoir (selected chapters)","pace":"~2 weeks",
  "room":"douglass","rights":"Public domain",
  "content":"Plan context and support for accounts of enslavement, violence, and racist language.",
  "teks":"English III · §110.38 — author’s purpose and rhetoric (informational); 5(C,D): analytic commentary and summary; 1(D): student-led discussion.",
  "li":"We are learning to explain how Douglass connects literacy and freedom (author’s purpose).",
  "sc":"I bring one open question, cite two details with chapter, respond to a peer, and name how my thinking changed.",
  "chunks":[("1","Ch. 1–5: birth, separation, witnessing violence, and being sent to Baltimore.","Wk 1 · Leader: Marcus"),
            ("2","Ch. 6–8: learning to read — “the pathway from slavery to freedom.”","Wk 1 · Leader: Nia"),
            ("3","Ch. 9–11: Covey, the turning point, and escape (details withheld).","Wk 2 · Leader: Sol")],
  "roles":[("Marcus","Questioner","Summarizer"),("Nia","Summarizer","Clarifier"),("Sol","Clarifier","Evidence tracker"),("Dee","Predictor","Questioner")],
  "q":["Douglass says learning to read was forbidden — what will literacy open, or endanger, for him?",
       "Why might Douglass withhold the exact means of his escape?",
       "What does he mean that literacy showed him “the pathway from slavery to freedom” yet also discontent?",
       "Trace how Douglass learns to read despite obstacles, without opinion.",
       "How does Douglass connect literacy and freedom (his purpose)? Use two details."],
  "lenses":[("Purpose","the abolitionist argument"),("Structure","the chronological memoir"),("Rhetoric","appeals and irony"),("Theme","literacy as freedom"),("Context","American slavery, 1845")],
  "prep":{"name":"Sol","lens":"Purpose","chunk":"Chunk 2",
    "ideas":["Douglass is denied education by law and custom.",
             "He trades bread for reading lessons and studies in secret.",
             "Literacy lets him understand — and begin to resist — his condition."],
    "details":["Auld warns that reading would make Douglass “unmanageable” (Ch. 6–7). → Reveals literacy’s power.",
               "Douglass’s resolve after learning to read (Ch. 7). → Shows both its cost and its promise."],
    "vocab":["chattel = a person treated as property.","emancipation = the act of being set free."],
    "summary":"Douglass recounts how he learned to read against the law, and how that literacy drove his path toward freedom.",
    "interp":"Knowledge is the first step from bondage toward freedom.",
    "synth":"The memoir’s purpose (abolition) rests on the theme: literacy exposes and undoes the logic of slavery. Text points: Auld’s warning (Chunk 2) and Douglass’s resolve (Chunk 2)."}},

 {
  "slug":"giver","title":"The Giver","author":"Lois Lowry","year":"1993",
  "band":"grades 6–8","genre":"novel","pace":"~2–3 weeks","room":None,"rights":"Copyrighted",
  "content":"Copyrighted — use a previewed edition. Contains “release” (euthanasia) and mature ideas. Verify all plot details against the book.",
  "teks":"Grade 7 · §110.23 — 7(A): theme through characters/events; 6(C,D): support inferences, summary; 1(D): student-led discussion.",
  "li":"We are learning to explain how Jonas’s growing awareness reveals a theme about memory, choice, and individuality.",
  "sc":"I bring one open question, cite two details with chapter (paraphrased), respond to a peer, and name how my thinking changed.",
  "chunks":[("1","Ch. 1–7: the community, the Ceremony, and Jonas chosen as Receiver.","Wk 1 · Leader: Jonah"),
            ("2","Ch. 8–15: training with the Giver — memories of color, pain, and love.","Wk 2 · Leader: Ari"),
            ("3","Ch. 16–23: learning what “release” means, and the escape with Gabriel.","Wk 3 · Leader: Sana")],
  "roles":[("Jonah","Questioner","Summarizer"),("Ari","Summarizer","Clarifier"),("Sana","Clarifier","Evidence tracker"),("Cruz","Predictor","Questioner")],
  "q":["Jonas is chosen for a unique, “honored” role — what might the community be hiding behind Sameness?",
       "Why might the community trade memory and color for “Sameness”?",
       "What does “release” turn out to mean, and how does it change Jonas?",
       "Trace what Jonas gains and loses as he receives memories, without opinion.",
       "How does Jonas’s awakening reveal a theme about memory and choice? Use two details (paraphrase)."],
  "lenses":[("Character","Jonas and the Giver"),("Setting","the engineered community"),("Theme","memory/individuality vs. Sameness"),("Plot","the decision to leave"),("Symbol","color and the sled")],
  "prep":{"name":"Sana","lens":"Theme","chunk":"Chunk 2","paraphrase":True,
    "ideas":["The community removes pain by removing memory and choice.",
             "The Giver transfers memories that bring both joy and suffering.",
             "Jonas decides that freedom is worth the risk of pain."],
    "details":["Jonas first perceives color where others see none (early training). → Suppressed individuality. (Verify against the text.)",
               "Jonas learns that “release” means death (later). → The hidden cost of a painless society. (Verify against the text.)"],
    "vocab":["Sameness = the community’s erasure of difference.","Receiver = the one who holds the community’s memories."],
    "summary":"Jonas discovers that his community’s comfort depends on erasing memory and choice, and he leaves to restore them.",
    "interp":"A life without pain or memory is also a life without love or real choice.",
    "synth":"Jonas (character) enacts the theme: his awakening shows that memory and choice, though painful, are what make us human. Text points (paraphrased): first color (Chunk 2) and learning of “release” (Chunk 3)."}},

 {
  "slug":"kindred","title":"Kindred","author":"Octavia E. Butler","year":"1979",
  "band":"grades 11–12 (English III–IV)","genre":"novel","pace":"~3 weeks","room":"kindred","rights":"Copyrighted",
  "content":"Copyrighted, mature — use a previewed edition. Contains graphic violence, racism, and sexual violence; plan strong context and support. Verify all plot details against the book.",
  "teks":"English III · §110.38 — 6(A): relationships among literary elements; 5(C,D): analytic commentary and summary; 1(D): student-led discussion.",
  "li":"We are learning to explain how Dana’s time shifts reveal a theme about the legacy and power of slavery.",
  "sc":"I bring one open question, cite two details by section (paraphrased), respond to a peer, and name how my thinking changed.",
  "chunks":[("1","“The River” / “The Fire”: Dana is pulled from 1976 to antebellum Maryland to save Rufus.","Wk 1 · Leader: Dana"),
            ("2","“The Fall” / “The Fight”: longer stays, Kevin, plantation life, and survival.","Wk 2 · Leader: Kev"),
            ("3","“The Storm” / “The Rope” / Epilogue: escalating danger, the final break, and its cost.","Wk 3 · Leader: Tess")],
  "roles":[("Dana","Questioner","Summarizer"),("Kev","Summarizer","Clarifier"),("Tess","Clarifier","Evidence tracker"),("Marc","Predictor","Questioner")],
  "q":["Dana is yanked into the past whenever Rufus is in danger — what will saving him force her to become part of?",
       "Why might Butler make Dana’s survival depend on protecting a future slaveholder?",
       "What does Dana’s injury on returning to 1976 suggest about the past’s grip on the present?",
       "Trace how Dana’s relationship to Rufus changes across her trips, without opinion.",
       "How do the time shifts reveal a theme about slavery’s legacy and power? Use two details (paraphrase)."],
  "lenses":[("Character","Dana and Rufus"),("Structure","the time-travel frame"),("Theme","the power and legacy of slavery"),("Setting","1976 vs. antebellum Maryland"),("Point of view","Dana’s first-person witness")],
  "prep":{"name":"Tess","lens":"Structure","chunk":"Chunk 3","paraphrase":True,
    "ideas":["Dana travels to the past whenever Rufus’s life is threatened.",
             "Each trip is longer and more dangerous than the last.",
             "Her survival ties her to the plantation’s system of power."],
    "details":["Dana loses part of herself — literally — by the end (epilogue). → The past exacts a permanent cost. (Verify against the text.)",
               "The compromises she makes to survive (middle sections). → Complicity forced by power. (Verify against the text.)"],
    "vocab":["antebellum = before the Civil War.","patroller = one who enforced slavery by hunting the enslaved."],
    "summary":"A modern Black woman is repeatedly pulled into the antebellum South to keep her white ancestor alive, confronting slavery’s brutality and its hold on the present.",
    "interp":"The past is not past; its power still shapes and scars the present.",
    "synth":"The time-travel structure carries the theme: Dana’s forced returns dramatize how slavery’s power reaches into the present. Text points (paraphrased): the epilogue’s cost and her mid-novel compromises."}},

 {
  "slug":"bnw","title":"Brave New World","author":"Aldous Huxley","year":"1932",
  "band":"grades 11–12 (English III–IV)","genre":"novel","pace":"~3 weeks","room":"bnw","rights":"Copyrighted",
  "content":"Copyrighted, mature — use a previewed edition. Contains drug use, sexual content, and mature themes; plan context and support. Verify all plot details against the book.",
  "teks":"English IV · §110.39 — 6(A): relationships among literary elements; 5(C,D): evaluative commentary and summary; 1(D): student-led discussion.",
  "li":"We are learning to explain how the World State’s design reveals a theme about freedom, technology, and stability.",
  "sc":"I bring one open question, cite two details by chapter (paraphrased), respond to a peer, and name how my thinking changed.",
  "chunks":[("1","Ch. 1–6: the World State, conditioning, castes, soma; Bernard and Lenina.","Wk 1 · Leader: Bea"),
            ("2","Ch. 7–13: the Reservation, and John the Savage brought to London.","Wk 2 · Leader: Juan"),
            ("3","Ch. 14–18: John’s rebellion, the debate with Mond, and the tragic end.","Wk 3 · Leader: Val")],
  "roles":[("Bea","Questioner","Summarizer"),("Juan","Summarizer","Clarifier"),("Val","Clarifier","Evidence tracker"),("Rai","Predictor","Questioner")],
  "q":["A society engineered for happiness and stability — what will it have to give up to keep them?",
       "Why might Huxley make the “Savage” the one who defends suffering and freedom?",
       "What does Mustapha Mond mean that they sacrificed truth and beauty for comfort?",
       "Trace how John’s view of the “brave new world” changes, without opinion.",
       "How does the World State’s design reveal a theme about freedom vs. stability? Use two details (paraphrase)."],
  "lenses":[("Character","John, Bernard, and Mond"),("Setting","the World State"),("Theme","freedom vs. stability"),("Structure","London vs. the Reservation"),("Symbol","soma")],
  "prep":{"name":"Val","lens":"Theme","chunk":"Chunk 3","paraphrase":True,
    "ideas":["Citizens are engineered into castes and kept content with soma.",
             "John, raised outside, values freedom, art, and even pain.",
             "Mond explains that stability requires giving up truth and high art."],
    "details":["Soma erases any discontent (throughout). → Comfort replaces freedom. (Verify against the text.)",
               "John demands the “right to be unhappy” in the debate (Ch. 17). → The human cost of engineered happiness. (Verify against the text.)"],
    "vocab":["conditioning = engineered training of behavior.","soma = the state-issued pleasure drug."],
    "summary":"A stable, engineered society trades freedom, truth, and art for comfort; an outsider’s refusal exposes that bargain.",
    "interp":"A life engineered for comfort may cost the very freedom that makes it meaningful.",
    "synth":"John (character) voices the theme: his defense of suffering reveals what the World State sacrificed for stability. Text points (paraphrased): soma’s use and the Mond debate (Chunk 3)."}},
]

# ---- HTML helpers ---------------------------------------------------------
HEAD = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — Literature Circle Planner ({kind})</title><link rel="stylesheet" href="../packet.css?v=f2bc7384919b"><style>
.filled{{color:#1d5b70;font-style:italic;font-weight:bold}}
.samplebadge{{display:inline-block;background:#315562;color:#fff;font-size:8pt;font-weight:bold;letter-spacing:.6px;padding:2px 8px;border-radius:3px;vertical-align:middle;margin-left:8px}}
.blankbadge{{background:#6a7a1e}}
.legend{{font-size:8.5pt;color:#52646c;margin:6px 0 0}}
.rights{{font-size:8.5pt;color:#52646c}}
.disc{{border:1px solid #9a6a2e;border-left:5px solid #9a6a2e;background:#fbf6ee;font-size:8.5pt}}
@media print{{
 #mp1{{font-size:9pt;line-height:1.25}}#mp2{{font-size:9.5pt}}
 #mp1 h1,#mp2 h1{{font-size:16pt;margin:4px 0}}
 #mp1 .lead{{font-size:10.5pt;margin:2px 0}}
 #mp1 h2,#mp2 h2{{margin:6px 0 2px;font-size:11pt}}
 #mp1 p,#mp2 p{{margin:3px 0}}
 #mp1 td,#mp1 th,#mp2 td,#mp2 th{{padding:3px}}
 #mp1 .write td{{height:22px}}
 #mp1 ul{{margin:3px 0}}#mp1 li{{margin-bottom:2px}}
 #mp1 .callout,#mp2 .callout,.disc{{padding:5px;margin:4px 0}}
 #mp1 .legend,.disc{{font-size:8pt}}#mp1 .legend{{margin:1px 0}}
 #mp2 .notes-grid{{grid-template-rows:220px 195px}}
 #mp2 .lines.three{{height:44px}}#mp2 h2{{margin:5px 0 2px}}
}}
</style></head><body>'''

def esc(s): return s  # data already uses entities/HTML intentionally

def toolbar(t, kind, blank):
    tip = ('Blank companion — teacher scaffolds (target, questions, lenses) are kept; students fill the plan and prep.'
           if blank else 'Worked example — <span class="filled">tinted italic</span> shows how one group filled it in.')
    return (f'<nav class="toolbar" aria-label="Planner actions"><a href="index.html">Planners</a>'
            f'<a href="../packet.html">Blank kit &amp; organizers</a>'
            f'<button onclick="window.print()">Print this planner</button>'
            f'<p>US Letter · Print at 100% · {tip}</p></nav>')

def cell(value, blank):
    """A write-in table cell: sample value (worked) or empty (blank)."""
    return '<td></td>' if blank else f'<td class="filled">{value}</td>'

def page1(t, blank):
    badge = ('<span class="samplebadge blankbadge">BLANK</span>' if blank
             else '<span class="samplebadge">WORKED EXAMPLE</span>')
    # target/plan table
    rows = [
      ('Text / author / edition',
       f'“{t["title"]}” — {t["author"]} ({t["year"]}). {t["genre"].capitalize()}.' if not blank
       else f'“{t["title"]}” — {t["author"]} ({t["year"]}). ______________________ (edition)'),
      ('Group / period / dates', None),  # write-in
      ('Grade / TEKS target (p. 3)', t["teks"]),   # scaffold: always shown
      ('Learning intention', t["li"]),                 # scaffold: always shown
      ('Success criteria', t["sc"]),                   # scaffold: always shown
    ]
    trs = ''
    for i,(hd,val) in enumerate(rows):
        if hd.startswith('Group'):
            trs += f'<tr><th>{hd}</th>' + cell('', blank) + '</tr>' if False else \
                   f'<tr><th>{hd}</th>' + ('<td></td>' if blank else f'<td class="filled">{t["_group"]}</td>') + '</tr>'
        elif hd == 'Text / author / edition':
            trs += f'<tr><th>{hd}</th>' + (f'<td>{val}</td>' if blank else f'<td class="filled">{val}</td>') + '</tr>'
        else:
            trs += f'<tr><th>{hd}</th><td>{val}</td></tr>'
    # calendar
    cal = ''
    for label, reading, meet in t["chunks"]:
        cal += ('<tr>' + (f'<td>{label}</td>' if blank else f'<td class="filled">{label}</td>')
                + (f'<td>{reading}</td>' if blank else f'<td class="filled">{reading}</td>')
                + ('<td></td>' if blank else f'<td class="filled">{meet}</td>') + '</tr>')
    # roles
    rl = ''
    for name, j1, j2 in t["roles"]:
        rl += ('<tr>' + ('<td></td><td></td><td></td>' if blank else
               f'<td class="filled">{name}</td><td class="filled">{j1}</td><td class="filled">{j2}</td>') + '</tr>')
    # questions (scaffold, always shown)
    labels = ["Predict","Question","Clarify","Summarize","Interpret the theme"]
    ql = ''.join(f'<li><b>{labels[i]}:</b> {q}</li>' for i,q in enumerate(t["q"]))
    # jigsaw lenses (scaffold, always shown)
    lens = ' · '.join(f'<span class="filled">{n}</span> ({d})' for n,d in t["lenses"])
    disc = f'<div class="callout disc"><b>Copyright:</b> {DISCLAIMER[t["slug"]]}</div>' if t["slug"] in DISCLAIMER else ''
    content = t.get("content")
    cnote = f'<p class="legend"><b>Preview note:</b> {content}</p>' if content else ''
    legend = ('Kit section 5 (group agreement &amp; calendar), scaffolded for this text. Students fill the group, calendar, and roles.'
              if blank else
              'Kit section 5 (group agreement &amp; calendar) filled in for one text — a finished plan students see before writing their own. <span class="filled">Tinted italic</span> = sample answers.')
    grade = t["teks"].split(" · ")[0].replace("Grade ","GRADE ").upper()
    return f'''<section class="page" id="mp1"><div class="eyebrow">LITERATURE CIRCLES / PLANNER · {grade} {badge}</div>
<h1>Plan a circle: “{t["title"]}”</h1>
<p class="lead">{t["author"]} ({t["year"]}) · {t["genre"]} · {t["band"]} · {t["pace"]}. <span class="rights">Rights: {t["rights"]}.</span></p>
<p class="legend">{legend}</p>{cnote}{disc}
<h2>Text, group, and target</h2>
<table class="write">{trs}</table>
<h2>Reading map &amp; calendar</h2>
<table class="write"><tr><th>Chunk</th><th>Read through</th><th>Meeting date · leader</th></tr>{cal}</table>
<h2>Members &amp; first-meeting jobs (p. 7 roles)</h2>
<table class="write"><tr><th>Member</th><th>First job</th><th>Rotates to (next meeting)</th></tr>{rl}</table>
<h2>Text-specific discussion questions (open — more than one answer)</h2>
<ul>{ql}</ul>
<div class="callout"><b>Optional Jigsaw lenses (p. 4):</b> {lens}.</div>
<footer><span>mglearn · Teacher Printables · {"Blank planner" if blank else "Sample planner"}</span><span>{t["title"]} · 1 / 2</span></footer></section>'''

def page2(t, blank):
    p = t["prep"]
    badge = ('<span class="samplebadge blankbadge">BLANK</span>' if blank
             else '<span class="samplebadge">WORKED EXAMPLE</span>')
    para = p.get("paraphrase")
    if blank:
        q = '<p>What needs clarification?<br>What could the group explore?</p>'
        ideas = '<p>Character choices, conflicts, themes, or central ideas.</p><p>1.</p><div class="lines two"></div><p>2.</p><div class="lines two"></div><p>3.</p><div class="lines two"></div>'
        vocab = '<p>Word + location + meaning or clue.<br>Mark anything still uncertain.</p>'
        ev = '<p>Short quote or accurate paraphrase + page/paragraph + what it shows.</p><p>1.</p><div class="lines three"></div><p>2.</p><div class="lines two"></div>'
        summary = '<div class="lines three"></div>'
        bring = ('<b>My interpretation:</b> These details suggest __________________________________________<br>'
                 '<b>Synthesis (connect two lenses):</b> ____________________________________________________<br>'
                 '<b>After discussion:</b> My thinking changed / became clearer because ______________________')
        head = f'Reading notes: “{t["title"]}”'
        idline = (f'<span class="filled">Name:</span> _______________ · <span class="filled">Home group:</span> _______________ '
                  f'· <span class="filled">Section:</span> “{t["title"]},” ____________ · <span class="filled">Expert lens:</span> ____________')
        note = '<b>Everyone prepares.</b> Read the whole assigned section. Write or draw three important ideas, two supporting details with locations, and one summary in your own words. Keep interpretation separate from summary.'
    else:
        q = ''.join(f'<p class="filled">{x}</p>' for x in [p["_q1"], p["_q2"]])
        ideas = ''.join(f'<p class="filled">{i+1}. {x}</p>' for i,x in enumerate(p["ideas"]))
        vocab = ''.join(f'<p class="filled">{x}</p>' for x in p["vocab"])
        ev = ''.join(f'<p class="filled">{i+1}. {x}</p>' for i,x in enumerate(p["details"]))
        summary = f'<p class="filled">{p["summary"]}</p>'
        bring = (f'<b>My interpretation:</b> <span class="filled">{p["interp"]}</span><br>'
                 f'<b>Synthesis (two lenses):</b> <span class="filled">{p["synth"]}</span><br>'
                 f'<b>After discussion:</b> <span class="filled">My thinking became clearer once the group compared evidence.</span>')
        head = f'Sample 3–2–1 notes: {p["name"]}, {p["lens"].lower()} lens'
        idline = (f'<span class="filled">Name: {p["name"]}</span> · <span class="filled">Home group: {t["_group"]}</span> '
                  f'· <span class="filled">Section: “{t["title"]},” {p["chunk"]}</span> · <span class="filled">Expert lens: {p["lens"]}</span>')
        note = ('<b>What a finished prep looks like.</b> Kit section 6 / Organizer A completed for one reader, so students can compare their notes to a strong model.'
                + (' Paraphrase and short references only — no long copying.' if para else ''))
    disc = ('<span class="rights"> Paraphrase only — no quotations; verify details against the book.</span>' if para else '')
    tag = f' · <span class="rights">Pair with the PlotPoint “{t["title"]}” room.</span>' if t.get("room") else ''
    return f'''<section class="page organizer" id="mp2"><div class="eyebrow">LITERATURE CIRCLES / STUDENT PREP {badge}</div>
<h1>{head}</h1>
<p>{idline}</p>
<div class="callout">{note}{disc}</div>
<div class="notes-grid">
<div class="questions-box"><h2>Questions</h2>{q}</div>
<div class="ideas-box"><h2>3 · Important ideas</h2>{ideas}</div>
<div class="vocab-box"><h2>Vocabulary</h2>{vocab}</div>
<div class="evidence-box"><h2>2 · Supporting details</h2>{ev}</div></div>
<h2>1 · Summary in my own words</h2>{summary}
<h2>Bring to the circle</h2><p>{bring}</p>
<p class="small">TEKS evidence: 6(C,D) supported inference; 7(A) theme through characters/events; 1(D) response to a peer.{tag}</p>
<footer><span>Miguel Guhlin · mguhlin.org · mguhlin@tcea.org · blog.tcea.org</span><span>{t["title"]} · 2 / 2</span></footer></section>'''

def render(t, blank):
    kind = "Blank" if blank else "Worked example"
    doc = HEAD.format(title=t["title"], kind=kind) + toolbar(t, kind, blank) + page1(t, blank) + page2(t, blank) + "</body></html>"
    slug = t["slug"] + ("-blank" if blank else "")
    (OUT / f"{slug}.html").write_text(doc, encoding="utf-8")
    return f"{slug}.html"

# derive helpers: group name + the two worked questions from the prep
def prep_questions(t):
    # two short student questions for the worked prep, drawn from the text
    base = {
     "magi":["Is a gift that can’t be used still the best gift?","Why call them the “wisest” right after calling the trade unwise?"],
     "necklace":["Would honesty have saved the Loisels ten years?","Whose fault is the ruin — Mathilde’s, or chance?"],
     "tobuildafire":["Could the man have survived with the dog’s instincts?","Is the ending fate, or his own doing?"],
     "telltale":["Is the narrator mad, or only guilty?","Why confess when he had gotten away with it?"],
     "monkeyspaw":["Was the third wish the right choice?","Could any wish have ended well?"],
     "gettysburg":["Why say the world will “little note” the speech?","What is the “new birth of freedom”?"],
     "yellowwallpaper":["Is her “freedom” at the end real or tragic?","How much does John cause her breakdown?"],
     "secretgarden":["Is the “Magic” nature, effort, or belief?","Who is healed more — Mary or Colin?"],
     "littlewomen":["Which matters more to Jo — ambition or family?","Is sacrifice rewarded in Part 1?"],
     "douglass":["Why is literacy dangerous to enslavers?","Why withhold the escape’s details?"],
     "giver":["Is a painless life worth the loss of choice?","Why must Jonas leave to change anything?"],
     "kindred":["Why must Dana keep a slaveholder alive?","What does her final injury mean?"],
     "bnw":["Is stability worth losing freedom?","Why does John demand the “right to be unhappy”?"],
    }
    return base.get(t["slug"], ["What still needs clarifying?","What should the group explore?"])

if __name__ == "__main__":
    written = []
    for t in TITLES:
        t["_group"] = t["roles"][0][0] + "’s group · Period __ · Meetings ___ & ___"
        qz = prep_questions(t); t["prep"]["_q1"], t["prep"]["_q2"] = qz[0], qz[1]
        written.append(render(t, blank=False))
        written.append(render(t, blank=True))
    # simple index of the planners
    lis = "".join(
      f'<li><b>{t["title"]}</b> — {t["author"]} · <span class="r">{t["rights"]}</span> · {t["band"]}<br>'
      f'<a href="{t["slug"]}.pdf">Worked PDF</a> · <a href="{t["slug"]}-blank.pdf">Blank PDF</a> · '
      f'<a href="{t["slug"]}.html">worked</a> / <a href="{t["slug"]}-blank.html">blank</a> (online)</li>'
      for t in TITLES)
    (OUT / "index.html").write_text(
      '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
      '<title>Literature Circle Planners by Title | Teacher Printables</title>'
      '<style>body{margin:0;background:#eef2f3;color:#17232b;font:17px/1.55 system-ui,sans-serif}'
      'main{max-width:820px;margin:36px auto;padding:28px;background:#fff;border-top:8px solid #315562}'
      'a{color:#234957}li{margin:12px 0}.r{color:#52646c;font-size:.85em}h1{line-height:1.15}</style></head><body><main>'
      '<a href="../litcircles/index.html">← Literature Circles Launch Kit</a>'
      '<h1>Sample planners by title</h1>'
      '<p>Each title has a <b>worked example</b> (a finished plan plus a completed student 3–2–1) and a <b>blank companion</b> '
      'that keeps the teacher scaffolds — TEKS target, text-specific questions, and Jigsaw lenses — while leaving the plan and prep for students to fill in. '
      'Two US Letter pages each; print at 100%. Copyrighted titles are paraphrase-only companions — students need a lawful copy of the book.</p>'
      f'<ol>{lis}</ol>'
      '<p class="r">© 2026 TCEA, created by Miguel Guhlin · Content CC BY-NC 4.0. Public-domain texts retain that status; copyrighted titles remain © their owners.</p>'
      '</main></body></html>', encoding="utf-8")
    print(f"Wrote {len(written)} planner files + index to {OUT}")
    for w in written: print(" ", w)
