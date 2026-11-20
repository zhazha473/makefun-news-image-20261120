# makefun-news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/zhazha473/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/zhazha473/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A wire-board image summing up Friday 20 November 2026's world news: 19 stories, 5 regions, drawn in code — Cyclone Akvan, the siege of Taiz, GTA VI's day-two sales, New Zealand v India, and the EU's summons of the Russian envoy, plus 13 wire briefs and what is still to come today.

## Run it

```sh
python3 compose.py && mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`compose.py` draws `entry.png` (1024x1024, deterministic — two runs give identical bytes). `main.py` copies it to the output directory; it uses only the standard library and no network.

---

<sub>Entered on [make.fun](https://make.fun/?ref=2zha-zha&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
