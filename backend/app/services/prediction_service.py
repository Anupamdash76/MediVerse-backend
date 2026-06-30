from app.data.disease_repository import DiseaseRepository
from app.ml.predictor import DiseasePredictor
from app.nlp.parser import SymptomParser


class PredictionService:
    """
    Coordinates the complete AI prediction pipeline.
    """

    def __init__(self):
        self.parser = SymptomParser()
        self.predictor = DiseasePredictor()
        self.repository = DiseaseRepository()

    def predict(self, symptoms: str):

        parser_result = self.parser.parse(symptoms)

        prediction = self.predictor.predict(
            parser_result.feature_vector
        )

        enriched_predictions = []

        for item in prediction["predictions"]:

            disease = item["disease"]

            

            info = self.repository.get(disease)

            enriched_predictions.append(
                {
                    "disease": disease,
                    **info,
                }
            )

        return {
            "predictions": enriched_predictions,
            "matched_symptoms": parser_result.matches,
            "unknown_symptoms": prediction["unknown_symptoms"],
        }