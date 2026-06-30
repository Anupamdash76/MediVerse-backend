import joblib
import numpy as np

from pathlib import Path
from xgboost import XGBClassifier


BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "models" / "xgboost.json"
FEATURE_PATH = BASE_DIR / "artifacts" / "feature_names.pkl"
ENCODER_PATH = BASE_DIR / "artifacts" / "label_encoder.pkl"


class DiseasePredictor:
    """
    Performs disease prediction from an already prepared feature vector.
    """

    def __init__(self):

        self.model = XGBClassifier()
        self.model.load_model(str(MODEL_PATH))

        self.feature_names = joblib.load(FEATURE_PATH)
        self.encoder = joblib.load(ENCODER_PATH)

    def predict(self, feature_vector, top_k=3):

        probabilities = self.model.predict_proba(feature_vector)[0]

        top_indices = np.argsort(probabilities)[::-1][:top_k]

        predictions = []

        for idx in top_indices:

            predictions.append(
                {
                    "disease": self.encoder.inverse_transform([idx])[0],
                    "probability": round(float(probabilities[idx] * 100), 2),
                }
            )

        return {
            "predictions": predictions,
            "unknown_symptoms": []
        }