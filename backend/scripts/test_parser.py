from app.nlp.parser import SymptomParser


def main():

    parser = SymptomParser()

    result = parser.parse(
        "headache, vomiting"
    )

    print("\n" + "=" * 60)
    print("Detected Semantic Matches")
    print("=" * 60)

    if not result.matches:
        print("No matches found.")
    else:
        for match in result.matches:
            print(
                f"Input: '{match.input}' "
                f"-> Matched: '{match.matched}' "
                f"(Score: {match.score:.4f})"
            )

    print("\n" + "=" * 60)
    print("Activated Features")
    print("=" * 60)

    active_features = result.feature_vector.loc[
        :,
        (result.feature_vector != 0).any(axis=0),
    ]

    print(active_features)


if __name__ == "__main__":
    main()