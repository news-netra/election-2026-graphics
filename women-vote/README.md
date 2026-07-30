# How women voted: Jamaat's advantage outside the cities

An interactive data-journalism analysis of how men and women voted differently in Bangladesh's 2026
national election, built from sex-segregated polling centres.

**[▶ Open the presentation](index.html)** — serve the folder over any static HTTP server, see below.

## Scope — read this first

Bangladesh runs many polling stations segregated by sex, so their results can be split by sex. But those
centres are only ~26% of all 42,382 centres, and they are **not spread evenly**: some constituencies have
almost none, and seven have none at all. A gender gap measured off two or three centres is noise.

This analysis therefore covers **only the 226 of 297 constituencies where single-sex centres hold at least
10% of the constituency's electorate.** 71 seats are dropped. Inside the 226, coverage runs from 10% to 98%
(median 22%), and the centres used hold about 30% of those seats' electorate.

**Known bias.** Sex-segregated polling is largely an urban practice — 77% of city-corporation centres are
single-sex against 18% of village (union) centres — so the sample over-represents cities. Measured across all
297 seats, counting only single-sex centres understates the BNP by 1.7 points, overstates the NCP by 2.2, and
picks a different winner from the full official result in 23 of the 290 covered seats. Nothing here is a
national result or a projection.

## The finding

- Across the 226 seats, **Jamaat-e-Islami is the only party women backed more than men — by 1.6 points**
  (31.2% → 32.8%). The BNP is flat (49.24% → 49.25%); Islami Andolan, the NCP and the rest all slip.
- **The gap is a village and small-town pattern, and it reverses in the big cities.** Jamaat gains ~2.4
  points among women in unions and in municipalities, and *loses* 0.5 in city corporations, where the BNP
  gains 1.2 instead.
- **Location is part of the story but not all of it.** Comparing men's and women's centres inside the same
  building reproduces the same split — Jamaat's lead over the BNP moves +0.8 pt among women in villages,
  +3.1 in small towns, and −3.0 in big cities, all significant.
- The widest gaps are in the **Khulna division** (the Jessore–Satkhira–Jhenaidah belt), where women push
  Jamaat from 45.7% to 50.7%. That belt is 13% of the seats in scope and delivered 38% of Jamaat's wins in it.
- **Turnout at women's centres was 5.4 points lower** than at men's, so this is choice, not turnout.
- On women's votes alone Jamaat leads 57 of the 226 seats against 46 on men's. But the *same centres counted
  together* give it 54, while the official result gave it 47 — so read the men-to-women gap, not the levels.

## Methodology

**Shares** are of valid votes at single-sex centres. Party columns available in the source are the eight
symbols listed below (~91% of the national vote).

**Same-building test.** Buildings are matched on the exact centre name within a constituency, normalised to
Bengali letters and digits only. Parenthetical qualifiers such as `(বালক শাখা)` / `(বালিকা শাখা)` are
**kept**, because those denote separate premises: dropping them roughly doubles the matched sample but merges
different sites and reverses the result. 1,204 buildings / 2,813 centres qualify. Confidence intervals are
95% on the mean of per-building differences.

The test is reported **by settlement type and never pooled.** Pooled across all types it returns −0.5 pt,
the opposite sign to every stratum, because the matched sample is 41% big-city buildings against 31% of the
scope's centres — textbook Simpson's paradox.

**Other definitions.** District charts use districts with ≥6 single-sex centres of each sex. "South-west" is
the Khulna division: Bagerhat, Chuadanga, Jashore, Jhenaidah, Khulna, Kushtia, Magura, Meherpur, Narail,
Satkhira. Seat winners are the full official count, all parties. Village / small town / big city are the
official union, municipality and city-corporation classification of each centre.

Party symbols: ধানের শীষ = BNP · দাঁড়িপাল্লা = Jamaat-e-Islami · হাতপাখা = Islami Andolan ·
শাপলা কলি = NCP.

## Run it locally

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000/index.html>. Any static server works; the charts fetch the `*.json` files
from this folder, so it must be served over HTTP, not opened as a `file://`.

## Contents

| File | What it is |
|------|------------|
| `index.html` | The scrollable presentation (11 charts, inline SVG) |
| `deck.json` | Every headline metric the page renders |
| `chart_data.json` | Per-district gaps |
| `winner_data.json` | Seat outcomes, gender-split leads, flip seats |
| `seats_in_scope.csv` | The 226 seats: coverage, men's/women's shares, leads, official winner |

All data files are aggregate and contain no personal information.

## Changelog

- **2026-07-30** — Narrowed scope to the 226 seats with ≥10% single-sex coverage; added the settlement-type
  split as a headline finding; corrected the same-building test (it was previously pooled across settlement
  types under a looser building match, which reversed its sign); documented the urban bias of the sample;
  removed the constituency map, which no longer matched the scope.
