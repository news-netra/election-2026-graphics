#!/usr/bin/env python3
"""Build the presentation's constituency map from the project boundary file."""

import csv
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
BOUNDARIES = HERE.parent / "delimitation_tool" / "constituencies_story.geojson"
SEATS = HERE / "seats_in_scope.csv"
OUTPUT = HERE / "seats_map.geojson"


def main() -> None:
    with BOUNDARIES.open(encoding="utf-8") as handle:
        geojson = json.load(handle)

    with SEATS.open(encoding="utf-8", newline="") as handle:
        seats = {row["index"]: row for row in csv.DictReader(handle)}

    for feature in geojson["features"]:
        constituency_id = str(feature["properties"]["constituency_id"])
        row = seats.get(constituency_id)
        properties = {
            "id": constituency_id,
            "name": feature["properties"].get("constituency_name_en", constituency_id),
            "in_scope": row is not None,
        }
        if row:
            jamaat_men = float(row["jM"])
            jamaat_women = float(row["jF"])
            properties.update(
                {
                    "gap": round(float(row["adv"]), 3),
                    "coverage": round(float(row["cov"]), 1),
                    "belt": row["belt"] == "True",
                    "contested": jamaat_men > 0 or jamaat_women > 0,
                    "jamaat_men": round(jamaat_men, 2),
                    "jamaat_women": round(jamaat_women, 2),
                }
            )
        feature["properties"] = properties

    OUTPUT.write_text(
        json.dumps(geojson, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    in_scope = sum(f["properties"]["in_scope"] for f in geojson["features"])
    if in_scope != len(seats):
        raise SystemExit(f"Map joined {in_scope} seats; expected {len(seats)}")
    print(f"Wrote {OUTPUT.name}: {in_scope} seats in scope, {len(geojson['features'])} boundaries")


if __name__ == "__main__":
    main()
