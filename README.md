# How Women Voted: Evidence from Bangladesh’s 2026 Polling-Centre Results

An interactive analysis built from the official Election Commission results.

**Live:** https://news-netra.github.io/election-2026-graphics/

[`women-vote/`](women-vote/) — how men and women voted differently,
using 11,096 single-sex polling centres, plus a same-building control to rule out geography.

## The finding, in short

Jamaat-e-Islami was the only major party to draw more support from women than men
(**33.0% vs 31.3%, +1.7 points**). The BNP's share was effectively identical across sexes.

To rule out geography, each men's centre was matched to the women's centre **in the same building**
(2,453 pairs). The gap held — **+1.02 points on average, 95% CI [0.83, 1.22], p < 0.001** — while the
same test on the BNP returned **zero (+0.01, p = 0.95)**.

The advantage is **concentrated, not universal**: negligible in the median seat, but **+5.3 points** in
the south-western Khulna belt, which is also where Jamaat won 20 of 30 seats. The effect survives outside
that region too — the gap is four times larger in seats Jamaat won than lost (+2.1 vs +0.5).

## Running locally

The page fetches its data, so it needs to be served over HTTP (not opened as `file://`):

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000/>.

## Data notes

- Single-sex centres are ~26% of all 42,382 polling centres (~25% of voters). Mixed centres cannot be
  split by sex and are excluded from the gender analysis.
- Seat winners and national vote shares come from the full official count.
- Symbols: ধানের শীষ = BNP · দাঁড়িপাল্লা = Jamaat-e-Islami · হাতপাখা = Islami Andolan · শাপলা কলি = NCP.
- Geometry is stored as TopoJSON so neighbouring areas share borders exactly (no gaps after simplification).

All data files here are aggregate. They contain no personal information.
