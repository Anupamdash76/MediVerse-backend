from dataclasses import dataclass
from typing import List

from app.schema.internal.parser import SymptomMatch


@dataclass
class PredictionResult:
    """
    Final disease prediction returned by the prediction service.
    """

    disease: str

    matched_symptoms: List[SymptomMatch]