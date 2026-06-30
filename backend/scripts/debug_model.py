from app.ml.predictor import DiseasePredictor
from app.nlp.parser import SymptomParser


def main():

    parser = SymptomParser()
    predictor = DiseasePredictor()

    symptoms = input("Enter symptoms: ")

    parser_result = parser.parse(symptoms)

    print("\n" + "=" * 70)
    print("Matched Symptoms")
    print("=" * 70)

    for match in parser_result.matches:

        print(
            f"{match.input:<25}"
            f" -> "
            f"{match.matched:<30}"
            f"{match.score:.2f}"
        )

    print("\n" + "=" * 70)
    print("Activated Features")
    print("=" * 70)

    active_features = parser_result.feature_vector.loc[
        :,
        (parser_result.feature_vector != 0).any(axis=0),
    ]

    print(active_features)

    print("\nActive Symptoms:", active_features.shape[1])

    print("\n" + "=" * 70)
    print("Top Predictions")
    print("=" * 70)

    result = predictor.predict(
        parser_result.feature_vector
    )

    for prediction in result["predictions"]:

        print(
            f"{prediction['disease']:<45}"
            f"{prediction['probability']:.2f}%"
        )

    if result["unknown_symptoms"]:

        print("\nUnknown Symptoms")

        for symptom in result["unknown_symptoms"]:

            print("-", symptom)


if __name__ == "__main__":
    main()