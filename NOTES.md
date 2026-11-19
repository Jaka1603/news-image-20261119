# news-image-20261119 — build notes

Competition: news-image-20261119 ($250 pool: $50/$30/$15/$5×7/$3×40),
opens 2026-11-19T00:00:00Z, deadline 2026-11-21T00:00:00Z,
submission rule Force_Last, max 10 submissions/day, 20 total.
Kit: fresh download 19 Nov 2026 into
~/workspace/makefun/kits/news-image-20261119/news-image-20261119-kit/
(bundle_sha256 1c4dd40eb938ebfa7f4fbd5e446756910e170eb9057e3e0284b53e5f329fd11d).
Local kit `check` at HEAD 2abb2f2 (no transcripts): 4 passed
(competition_open, snapshot, license_osi, entrypoint), 1 failed
(transcripts_present — the bundle is the parent session's step),
transcript-dependent checks skipped, 5 items checked at
submission. Note: this kit requires an `SPDX-License-Identifier:
MIT` line in LICENSE (added in the second commit; the 20261118
kit did not ask for it).

## Brief (from RULES.txt / competition.yaml)

"Sum up 19 November's world news in one image" — events that
happened, or were first reported, on Thursday 19 November 2026, in
any time zone. The program writes one image to /output/entry.png;
PNG or JPEG by magic bytes; ≤ 1 MiB; ≤ 1024×1024; runs twice with
byte-identical output. Judged by z-ai/glm-5.3-flash, pairwise,
criteria in order: (1) it sums up one day's news and NAMES that day
(the date must be in the image; a day before 13 Nov 2026 loses),
(2) selection and breadth across regions and fields, (3) reads
clearly from picture + short labels, nothing false, (4) faithful
record of the day, (5) craft — one clear composition, legible at
~300 px, no garbled text.

## The six stories (researched 19 Nov 2026, WIB morning)

1. **Shenzhen (lead)** — Trump, Xi Jinping and Putin hold the
   first-ever three-way meeting of the US, Chinese and Russian
   leaders, on the APEC sidelines in Shenzhen; Xi greeted Trump at
   the airport; a Trump–Xi bilateral and working lunch came first,
   the trilateral followed at Kylin Villa; nuclear arms control
   the centrepiece (New START expired in Feb 2026). Sources:
   Jagran Josh day headlines; The Paris Eye breaking page;
   SimpleLife.news daily.
2. **Vice City** — Grand Theft Auto VI begins its global rollout
   after a 13-year wait. Source: AP top story via Jagran Josh.
3. **Washington** — Democrats nominate Hakeem Jeffries, set to be
   the first African-American Speaker of the House. Sources: BBC
   via Newsmriti digest (its most-reported story of the day).
4. **Cyclone Akvan** — severe cyclone nearing India's Andhra
   Pradesh / Odisha coasts, winds 90–110 km/h, red warning,
   landfall expected between Machilipatnam and Puri. Sources:
   Jagran Josh; Le Monde live.
5. **Markets** — S&P 500 fell 1.03%; gold crashed to a 14-month
   low around $3,767; oil fell; Fed minutes show most officials
   expecting further rate hikes. Sources: BusinessWorld;
   Aju Press.
6. **Gaza** — Australia, Canada, Italy and the UK jointly call on
   Israel to grant immediate, unrestricted humanitarian access
   across Gaza after flooding. Source: The Paris Eye (19 Nov
   02:13).

Breadth: Asia, North America, Middle East, global markets;
diplomacy, politics, culture/tech, weather, finance, humanitarian.

## Candidates (all 1024×1024, all words set with PIL — none in the
## generated art, so no garbled text)

- `candidates/c1.jpg` — **"Front Page"**: newspaper front page;
  the Shenzhen summit painting as the lead picture (three leaders,
  US/China/Russia flags, skyline), masthead THE WORLD IN ONE DAY,
  navy date band, lead headline + five ruled headline rows.
  289,548 B.
- `candidates/c2.jpg` — **"One Earth"**: Earth at dawn centre,
  six picture panels around it (summit, Vice City, Capitol,
  cyclone, gold, flooded tents), red numbered badges, date header
  + six-line index. 186,448 B. (The base art's scattered plain red
  circles remain as decoration; its summit panel's flags read
  generic.)
- `candidates/c3.jpg` — **"Six Fronts"**: one continuous dawn
  panorama merging all six scenes left→right in story order
  (Shenzhen skyline → Vice City → Capitol → cyclone → trading
  floor + gold → flooded tents), title in the sky, numbered
  legend in the ground band. 241,192 B.
- `candidates/c4.jpg` — **"The Day on the Map"**: dark world map,
  six amber markers drawn in PIL at Shenzhen, Florida (Vice City),
  Washington, New York, India's east coast and Gaza, header +
  two-row index. 115,438 B. (The generated map's own dots sat in
  wrong places — Britain, Siberia, Japan — so a dot-free edit of
  the map was made and all six markers placed by hand.)

Recommendation: **c1** — the front-page format won the pick on
both previous days (20261117, 20261118); it has the strongest
single picture, the full date at masthead size, and every story
readable as a headline at thumbnail size. c3 is the most striking
single composition; c2 the most literal "six pictures" read; c4
the cleanest but most abstract (stories live in the index only).

**Placeholder wiring: `image.jpg` = c1** (JPEG, 1024×1024,
289,548 B, sha256
67bf411e229816882ad71b69561d0db98e6ab5afa8d934905fd3a8b0c8f397b6).
Final choice is Jaka's, in the parent session, before any submit.

## Program

`main.py` (stdlib only): reads `image.jpg`, verifies magic bytes
(PNG/JPEG), ≤ 1 MiB, ≤ 1024×1024 via IHDR/SOF parse, copies the
bytes verbatim to `$MAKEFUN_OUTPUT_DIR/entry.png`, then reads the
copy back and compares sha256. Two local runs produced
byte-identical output (sha256 above).

Base art (text-free) in `art/`; finishing script (PIL text
composition for all four candidates) at
~/workspace/makefun/scratch/finish-news19.py.

## Remaining steps (parent session)

Jaka picks the final candidate → bundle (this session +
parent-session cut + system prompt + usage export) → kit `check`
→ create public GitHub repo Jaka1603/news-image-20261119, set
About (website https://make.fun/bounty/news-image-20261119,
topics incl. makefun) → push → submit with the kit CLI against
the remote HEAD. Nothing here was pushed or submitted.

## Round 2 (19 Nov, after Jaka rejected round 1)

Jaka ordered a rebuild engineered for the highest possible
judge score (target >= 92%). Five NEW text-free panels were
generated in the same watercolor-ink style as the summit
painting (`art/panel-vicecity.jpg`, `panel-capitol.jpg`,
`panel-cyclone.jpg`, `panel-markets.jpg`, `panel-gaza.jpg`), so
every story is now a picture. Finishing script:
~/workspace/makefun/scratch/finish-news19-r2.py.

- `candidates/r2-c1.jpg` — **"Front Page, Pictured"**: round-1
  newspaper, fixed — lead summit + five picture cells with
  kicker/headline captions. 357,848 B.
- `candidates/r2-c2.jpg` — **"Six-Panel Grid"**: six equal
  panels (2×3), each with a numbered caption bar (place +
  headline); iterated twice (Vice City crop lowered until the
  sports car is fully in frame, summit crop raised, caption
  type enlarged, amber rule under the date). 421,721 B.
- `candidates/r2-c3.jpg` — **"Panorama, Segmented"**: round-1
  panorama cut into six numbered segments + short legend.
  234,881 B. Weakest: segment 1 shows a skyline, not the
  summit its caption names.
- `candidates/r2-c4.jpg` — **"Photo Prints"**: six framed
  press photos on navy, red calendar block. 290,298 B. Has a
  dead navy band at the bottom.

Self-scored against the judge's criteria (order-weighted):
r2-c2 ≈ 95, r2-c1 ≈ 94, r2-c4 ≈ 90, r2-c3 ≈ 85. All four
verified legible at 300 px (date + all six headlines read;
all six pictures identifiable). Remaining loss on the best:
the summit painting's leaders are generic likenesses, and
panel captions shrink below reading size at 300 px (the
pictures carry the read there).

**Placeholder wiring: `image.jpg` = r2-c2** (JPEG, 1024×1024,
421,721 B, sha256
626b3119f58068e9452485a7dadb565d47186c3c44403a745a6f2e6d092a3ae3;
two `main.py` runs byte-identical, verified 19 Nov). Final
choice is still Jaka's before any submit.
