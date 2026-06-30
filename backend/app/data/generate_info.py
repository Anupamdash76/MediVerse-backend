import json
import argparse
import pandas as pd
from pathlib import Path


DEFAULT_DISCLAIMER = (
    "This AI prediction is informational only and "
    "should not replace professional medical advice."
)


def generate(dataset_path: Path, output_path: Path):

    df = pd.read_csv(dataset_path)

    diseases = (
        df["diseases"]
        .dropna()
        .str.strip()
        .str.lower()
        .unique()
    )

    diseases = sorted(diseases)

    data = {}

    for disease in diseases:

        data[disease] = {

            "summary": "",

            "recommended_medicines": [],

            "precautions": [],

            "doctor_speciality": "",

            "severity": "",

            "disclaimer": DEFAULT_DISCLAIMER,
        }

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        output_path,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False,
        )

    print(f"Generated {len(data)} diseases.")
    print(f"Saved to: {output_path}")


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--dataset",
        required=True,
        help="Path to curated_dataset.csv",
    )

    parser.add_argument(
        "--output",
        default="app/data/diseases.json",
        help="Output JSON file",
    )

    args = parser.parse_args()

    generate(
        Path(args.dataset),
        Path(args.output),
    )


if __name__ == "__main__":
    main()