from app.services.prediction_service import PredictionService


def main():

    service = PredictionService()

    symptoms = input("Enter symptoms: ")

    result = service.predict(symptoms)

    print("\n" + "=" * 60)
    print("Disease Prediction")
    print("=" * 60)

    print(f"Disease    : {result.disease}")
    print(f"Confidence : {result.confidence:.2f}%")

    print("\n" + "=" * 60)
    print("Matched Symptoms")
    print("=" * 60)

    if not result.matched_symptoms:
        print("No semantic matches found.")
    else:
        for match in result.matched_symptoms:
            print(
                f"Input: '{match.input}' "
                f"-> '{match.matched}' "
                f"(Score: {match.score:.4f})"
            )


if __name__ == "__main__":
    main()