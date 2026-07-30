# How Women Voted: Evidence from Bangladesh’s 2026 Polling-Centre Results

An interactive analysis built from the official Election Commission results.

**Live:** https://news-netra.github.io/election-2026-graphics/

[`women-vote/`](women-vote/) — how men and women voted differently, using 10,468 single-sex polling
centres across the 226 constituencies where enough of the electorate votes that way to measure it.

## The finding, in short

Across those 226 seats, Jamaat-e-Islami was the only party to draw more support from women than men
(**32.8% vs 31.2%, +1.6 points**). The BNP's share was effectively identical across sexes
(49.25% vs 49.24%), and Islami Andolan — the other Islamic party — did *worse* among women.

**The gap is a village and small-town pattern, and it reverses in the big cities.** Jamaat gains about
2.4 points among women in unions and in municipalities, and loses 0.5 in city corporations, where the
BNP gains 1.2 instead. Matching men's and women's centres **in the same building** reproduces that same
split — Jamaat's lead over the BNP moves **+0.8 pt** among women in villages, **+3.1** in small towns and
**−3.0** in big cities, all significant. The test is never pooled across those three: pooled it returns
the opposite sign, because the matched sample is 41% big-city buildings against 31% of the scope.

The advantage is **concentrated, not universal**: negligible in the median seat, but **+5.0 points** in
the south-western Khulna division, which is also where Jamaat won 18 of the 29 seats in scope. It
survives outside that region — the gap is about five times larger in seats Jamaat won than lost
(+2.5 vs +0.5).

## Scope and known bias

This is **not a national result.** Only sex-segregated centres can be split by sex, and they are ~26% of
all 42,382 centres and very unevenly spread — seven constituencies have none at all. The analysis
therefore covers only the **226 of 297 constituencies where single-sex centres hold at least 10% of the
constituency's electorate**; 71 seats are dropped.

Sex-segregated polling is largely an urban practice — **77% of city-corporation centres are single-sex
against 18% of village (union) centres** — so the sample over-represents cities. Measured across all 297
seats, counting only single-sex centres understates the BNP by 1.7 points, overstates the NCP by 2.2, and
picks a different winner from the full official result in 23 of the 290 covered seats. Seat counts in the
analysis are therefore shown against the same centres counted together, never as a projection.

## Running locally

The page fetches its data, so it needs to be served over HTTP (not opened as `file://`):

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000/>.

## Data notes

- Mixed centres cannot be split by sex and are excluded from the gender analysis.
- Seat winners and national vote shares come from the full official count, all parties.
- Village / small town / big city are the official union, municipality and city-corporation
  classification of each polling centre.
- Symbols: ধানের শীষ = BNP · দাঁড়িপাল্লা = Jamaat-e-Islami · হাতপাখা = Islami Andolan · শাপলা কলি = NCP.

Full method, definitions and per-seat coverage: [`women-vote/README.md`](women-vote/README.md) and
[`women-vote/seats_in_scope.csv`](women-vote/seats_in_scope.csv).

All data files here are aggregate. They contain no personal information.
