import json

from app.config.paths import APP_DIR


class DiseaseRepository:
    """
    Loads disease information once and serves it
    throughout the application's lifetime.
    """

    def __init__(self):

        path = APP_DIR / "data" / "diseases.json"

       

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:

            self.data = json.load(file)

        

    def get(self, disease: str):
        """
        Returns disease information from the knowledge base.
        """

        key = disease.strip().lower()

       

        return self.data.get(
            key,
            {
                "summary": "Information unavailable.",

                "recommended_medicines": [],

                "precautions": [],

                "doctor_speciality": "General Physician",

                "severity": "Unknown",

                "disclaimer": (
                    "This AI prediction is informational only "
                    "and should not replace professional medical advice."
                ),
            },
        )