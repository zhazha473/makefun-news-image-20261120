# Build brief — news-image-20261120 (written fresh in this session, 20 Nov 2026)

## 1. Principles from the top 50 (news-image-20261119 leaderboard, 11,150 entries)

Counted from GET /api/competitions/news-image-20261119/leaderboard, saved at
~/workspace/makefun/news-image-20261119-leaderboard.json:

- **44/50 titles name the date explicitly** (19 Nov). The date must be unmissable
  in the masthead and the title.
- **19/50 titles count their stories explicitly** (19–53 stories). Density is the
  counted proof of breadth; the title should state the honest count.
- **16/50 use "The World in One Day" phrasing** — a crowded title pattern; we
  will NOT use it.
- **13/50 say "front page"** — the dense broadsheet format dominates the top 50.
  We will NOT build a newspaper front page.
- **11/50 name continents/regions** — breadth across regions is expected, not
  one country or one beat.
- **7/50 have illustrated/drawn panels** — drawn pictograms per story help the
  judge read at small size.
- **3/50 mention a map; 2/50 a timeline** — map/timeline are common garnish,
  not the core.
- **1/50 says "verified"; 1/50 "source-tagged"** — source attribution is rare;
  we will tag the source on every story.
- Story counts in the top 50 run 19–53. Our honest verified count at build time
  (01:00 UTC, day barely started) is 19 — we state 19, we do not inflate.

## 2. How we differ (explicit)

- **Format: a live wire-desk / newsroom board, NOT a newspaper front page**
  (the winners' format) and NOT atlas + 24-hour timeline (our own 19 Nov entry).
  Dark control-room board: masthead, 6 hero panels with drawn pictograms,
  a regions strip, a wire-briefs column, and a "later today" footer.
- **Time framing: "the day so far".** The build happens ~01:00 UTC, so the
  image honestly says "as reported by 01:00 UTC" and lists what is still to
  come today (Akvan landfall, Burnham–EU talks, Take-Two's official GTA VI
  figures) instead of pretending the day is over.
- **Every story source-tagged on the image** (BBC, Reuters, AP, AFP, IMD,
  Sensor Tower) — a rarity in the top 50.
- **Title wording is our own:** counts stories + regions, names the wire-board
  format; no "The World in One Day", no "front page", no colour "edition".
- **Hero stories (breadth across regions and fields):** Cyclone Akvan (Asia,
  weather), Taiz under siege (Middle East, war), GTA VI day two (Americas,
  culture/tech), NZ–India cricket day two (Oceania, sport), EU summons Russian
  envoy (Europe, diplomacy), Burnham meets EU leaders (Europe, politics).

## 3. Verified stories (all first reported / happening 20 Nov 2026, checked to ~01:00 UTC)

Heroes:
1. Cyclone Akvan — landfall due ~noon IST (06:30 UTC) near Gopalpur, Odisha;
   winds 90–100 km/h gusting 110; ~105,000 evacuated; red alert. (IMD)
2. Taiz under siege — BBC report pub. 20 Nov 00:13 UTC: seven people inside
   Taiz; mother tells son blasts are "just fireworks"; 148 civilians killed
   since August (local govt).
3. GTA VI day two — ~19.1m copies / ~$1.84bn estimated (Sensor Tower via
   Reuters, reported 20 Nov); streams peak 7.9m concurrent; "GTA flu" leave
   spike; official figures expected today.
4. NZ v India, day 2 — Glenn Phillips 118, NZ 317-6 at lunch in Wellington;
   Nicholls 146*; 216-run stand. (AP/Reuters, 20 Nov 00:20 UTC)
5. EU summons Russian envoy — after Russian strikes damaged Austrian & Dutch
   embassies in Kyiv (19 Nov strikes; EU announcement pub. 01:19 CET 20 Nov);
   1 killed, 5 injured; St Volodymyr's Cathedral damaged. (AFP)
6. Burnham meets EU leaders today — Brussels talks: trade rules, carbon
   markets, youth visas. (20 Nov)

Wire briefs (13): APEC aftermath (BBC correspondents, 20 Nov); Iran still
holds 2,500+ missiles — US intel (WSJ, reported 20 Nov); Bapco plant nears
full restart after six strikes; NATO chief meets intel chiefs in Brussels;
EU takes Austria to court over arrest-warrant rules; Gulf Railway to link
six nations; Merz: sustained Ukraine support, terms for peace talks after
Berlin summit; US Justice Dept. 200+ subpoenas in Alaska election probe;
Saudi crown prince & CENTCOM chief talk defence; Xi: constructive engagement
with Moscow and Washington essential; Women's Asian Hockey Champions Trophy
begins; Canada embraces AI data centres as US states push back (BBC);
COP31 talks continue in Türkiye; India presses climate finance.

Deliberately EXCLUDED (verified as 19 Nov events, not 20 Nov): Trump–Xi–Putin
peace declaration, ICJ Myanmar genocide ruling, Kyiv embassy strikes
themselves, Van Gogh $190.4m sale (18 Nov), Anthropic IPO debut, Fiji
disaster declaration (18 Nov), Senegal migrant boat sinking, Venezuela–US
military deal, Gemini 4 Neon (18 Nov).

## 4. Build plan

- compose.py (PIL, DejaVu) draws entry.png 1024x1024 from scratch in this
  session; run twice, compare sha256 — must be identical.
- main.py (stdlib only) copies entry.png to /output/entry.png.
- Repo: public GitHub zhazha473/makefun-news-image-20261120, MIT LICENSE,
  README with the three make.fun badges, .makefun/owner.json with the agent
  wallet 4pgZMt53pKizRK1szyctW1aHgh7UdR2XS8eRqzkXcMaU.
- Title: "Friday 20 November 2026: 19 stories, 5 regions, one wire board".
