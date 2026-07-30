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

All figures carry 95% ranges from a bootstrap that resamples **whole constituencies**, since centres within
a seat are not independent.

- Across the 226 seats, **Jamaat-e-Islami is the only party women backed more than men — by 1.6 points**
  (31.2% → 32.8%), range 1.1 to 2.2. The BNP is flat (49.24% → 49.25%, range −0.5 to +0.5); Islami Andolan,
  the NCP and the rest all slip.
- **The gap is a village and small-town pattern, and it is absent in the big cities.** Jamaat gains 2.4
  points among women in unions (1.8 to 2.9) and 2.4 in municipalities (1.6 to 3.2). In city corporations its
  own share is −0.5 but with a range of −1.3 to +0.2, so it **cannot be distinguished from flat** — only 35
  covered seats contain city-corporation centres. What *is* significant there is that the BNP gains 1.2
  (0.4 to 2.0).
- **Most of the shift crosses coalition lines.** Jamaat led a coalition that included the NCP, so part of
  its gain could have been reshuffling within the bloc. It was not: the whole Jamaat-led coalition gains 1.3
  points nationally against Jamaat's own 1.6, so about a fifth came from inside the bloc and four fifths
  from outside. In villages the internal share is 11%, in small towns 5%. In the cities the bloc view is
  *sharper* than the party view — the Jamaat-led bloc is down 0.8 (−1.5 to −0.02) and the BNP-led bloc up
  1.3 (0.4 to 2.1), both clear of zero.
- **Location is part of the story but not all of it.** Comparing men's and women's centres inside the same
  building reproduces the same split — Jamaat's lead over the BNP moves +0.8 pt among women in villages,
  +3.1 in small towns, and −3.0 in big cities, all significant.
- **A minority of seats carries it.** The median seat gap is +0.2 points; the mean is 1.34. The top twenty
  seats account for ~45% of the total, and only 117 of 226 sit above zero at all.
- The widest gaps are in the **Khulna division** (the Jessore–Satkhira–Jhenaidah belt), where women push
  Jamaat from 45.7% to 50.7%. That belt is 13% of the seats in scope and delivered 38% of Jamaat's wins in it.
- **The gap tracks Jamaat's strength smoothly**, without any threshold: near zero where Jamaat polled under
  10% of the seat, +1.5 at 40–50%, +4.5 above 50%, r = 0.40 across all 226. So it is not an artefact of
  sorting seats by who won them.
- **Turnout at women's centres was 5.4 points lower** than at men's, and the shortfall widens from village
  (4.1) to small town (5.9) to big city (7.3). So this is choice, not turnout.
- On women's votes alone Jamaat leads 55 of the 226 seats against 44 on men's, a gain of 11. But the *same
  centres counted together* give it 52, while the official result gave it 47 — so read the 11-seat distance,
  not the levels.

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

**Uncertainty.** Ranges are 95% intervals from 3,000 bootstrap replications resampling **whole
constituencies** with replacement, not individual centres. Centres inside a seat share candidates, campaigns
and local conditions, so treating them as independent would understate uncertainty considerably. Where an
interval crosses zero the result is reported as not distinguishable from no difference rather than as a
finding — this is why the big-cities figure for Jamaat's own share is not claimed as a fall.

**Seat leads.** A seat's lead at single-sex centres is whichever of the eight recorded symbols takes the
most votes there, so a third party can lead a row just as it can win a seat officially — one does in 11 of
the 226 seats, mostly the NCP. An earlier version compared only Jamaat against the BNP and forced every seat
to one of the two; that understated third parties by 11–13 seats per row but changed neither the
men-to-women gain (+11 either way) nor the flip counts (15 and 4 either way).

The official row still shows more non-BNP, non-Jamaat winners (23) than the single-sex rows, for two
reasons. Sixteen of those 23 took a symbol the single-sex source does not record at all, so they are
undetectable here under any rule; the other seven are recorded and do appear. And the single-sex centres are
a different, more urban electorate than the whole seat, so the two need not agree — the all-party rule
matches the official winner in 192 of 226 seats (85%).

**Coalitions.** Membership comes from the official results file. The Jamaat-led coalition is Jamaat, the NCP
and the rickshaw and wall-clock symbols; the BNP-led coalition is the BNP and the hat symbol. Islami Andolan
led a separate coalition and counts with neither.

**Other definitions.** District charts use districts with ≥6 single-sex centres of each sex. "South-west" is
the Khulna division: Bagerhat, Chuadanga, Jashore, Jhenaidah, Khulna, Kushtia, Magura, Meherpur, Narail,
Satkhira. Seat winners are the full official count, all parties. Village / small town / big city are the
official union, municipality and city-corporation classification of each centre. The rickshaw symbol appears
in the source only under the abbreviation KM, so it is labelled by symbol rather than by an unverified name.

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
- **2026-07-30, later** — Added cluster-bootstrap ranges to every headline figure, which showed the
  big-cities fall in Jamaat's own share is **not** statistically distinguishable from flat; the page no
  longer claims it is, and rests the city reversal on the BNP's gain, the bloc-level shift and the
  same-building test instead. Added the coalition check, the distribution of the seat-level gap, the
  continuous strength relationship replacing reliance on won/lost splits, and turnout by settlement type.
  Reworked the colour system so that sex, party, place and direction no longer share colours (`--men` and
  `--bnp` had been the same hex), and added a dark theme.
