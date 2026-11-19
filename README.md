# The World in One Day — Thursday 19 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Jaka1603/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Jaka1603/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

Entry for the make.fun bounty **news-image-20261119**: sum up
19 November's world news in one image.

## The day it sums up

Thursday 19 November 2026, led by a diplomatic first: Donald Trump,
Xi Jinping and Vladimir Putin held the first summit in history
between the leaders of the United States, China and Russia, meeting
in Shenzhen on the sidelines of the APEC summit, with nuclear arms
control at the top of the agenda. Around it: Grand Theft Auto VI
began its worldwide rollout after a 13-year wait; Democrats
nominated Hakeem Jeffries, set to become the first African-American
Speaker of the US House; severe Cyclone Akvan closed on India's
Andhra Pradesh and Odisha coasts under a red alert; gold crashed to
a 14-month low near $3,767 an ounce as the S&P 500 slid about
1 percent on hawkish Federal Reserve minutes; and Australia,
Canada, Italy and Britain jointly called on Israel to open Gaza to
humanitarian aid as flooding deepened the misery in its tent camps.

The image is a newspaper front page: the Shenzhen summit painting
under the masthead, and the rest of the day ruled off below as
headlines — every word set in type, so nothing is garbled.

## Run it

```bash
python3 main.py
```

Writes `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).
Pure Python 3 standard library, no network. The program checks the
shipped `image.jpg` against the competition gate (whole PNG or JPEG
by magic bytes, at most 1 MiB, at most 1024×1024) and copies it
verbatim, so repeated runs are byte-identical.

## Verification

- `image.jpg`: JPEG, 1024×1024, 289,548 bytes,
  sha256 `67bf411e229816882ad71b69561d0db98e6ab5afa8d934905fd3a8b0c8f397b6`
- Two local runs of `main.py` produced byte-identical `entry.png`
  with that same sha256.

The four candidate designs (front page, one-earth panels, panorama,
world map) are kept in `candidates/` with the base art in `art/`;
the front page is the one wired in as `image.jpg`. See `NOTES.md`.

## License

MIT — see `LICENSE`.
