# Jamaat, women and the city line

A concise, chart-led presentation of how men and women voted differently at Bangladesh's sex-segregated polling centres in the 2026 national election.

**[Open the presentation](index.html)** — serve this folder over HTTP; instructions are below.

## The seven findings

1. **Jamaat's share was 1.6 points higher among women.** It was 31.2% at men-only centres and 32.8% at women-only centres (95% range: +1.1 to +2.2). BNP was effectively flat.
2. **The edge belongs to villages and small towns.** Jamaat's share was 2.4 points higher at women-only centres in each. Its big-city gap was not clearly different from zero, while BNP's share was 1.2 points higher there.
3. **The same-premises check reproduces the divide.** The women–men difference in Jamaat's lead over BNP is +0.8 points in villages, +3.1 in towns and −3.0 in big cities when men-only and women-only records are matched at the same named polling premises.
4. **The pattern remains at coalition level.** The Jamaat-led bloc's share was +2.1 points higher at women-only village centres and +2.3 higher in towns, but −0.8 lower in big cities.
5. **The south-west is the hotspot.** Across the 29 covered Khulna-division seats, Jamaat had 45.7% at men-only centres and 50.7% at women-only centres; the gap was 1.0 point across covered seats elsewhere.
6. **The gap is larger where Jamaat's 2026 vote share is higher.** It is near zero where Jamaat polled below 10% and +4.5 points where Jamaat polled above 50% (r = 0.40 across seats).
7. **Jamaat leads 11 more seats at women-only centres.** It leads 44 seats using men-only centres and 55 using women-only centres. This is a within-sample comparison, not a projection.

## Scope and limits

The analysis covers the 226 of 297 constituencies where single-sex centres hold at least 10% of the electorate. It uses 10,468 men-only or women-only centres, covering about 30% of the electorate in those seats.

The subset is urban-skewed. Across all 297 constituencies, single-sex centres account for 77% of city-corporation centres, 42% of municipality centres and 18% of union centres. The presentation therefore reports villages, towns and big cities separately and does not treat the combined number as a national estimate.

The page's methodology is a native Q&A accordion covering scope, definitions, the same-premises match, uncertainty, threshold sensitivity, coalitions, seat leads and sources.

## Run locally

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000/index.html>. The page fetches local JSON/GeoJSON files, so opening it directly with a `file://` URL will not work.

## Files

| File | Purpose |
|---|---|
| `index.html` | Seven-finding web presentation with seven inline SVG visuals and methodology Q&A |
| `deck.json` | Headline, place, coalition, uncertainty and seat-lead data |
| `seats_map.geojson` | 300 constituency boundaries, with the 226 in-scope seats joined to presentation metrics |
| `build_map.py` | Rebuilds `seats_map.geojson` from the project boundary file and `seats_in_scope.csv` |
| `seats_in_scope.csv` | Per-seat coverage and gender-split vote shares for the 226 covered seats |
| `chart_data.json` | District aggregates retained for analysis and backup charts |
| `winner_data.json` | Legacy seat/flip detail retained for reference; the presentation uses the all-party lead data in `deck.json` |

All data files are aggregate and contain no personal information.
