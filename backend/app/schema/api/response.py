from typing import List

from pydantic import BaseModel


class SymptomMatchResponse(BaseModel):
    input: str
    matched: str
    score: float


class PredictionItemResponse(BaseModel):
    disease: str

    summary: str

    recommended_medicines: List[str]

    precautions: List[str]

    doctor_speciality: str

    severity: str

    disclaimer: str


class PredictResponse(BaseModel):

    predictions: List[PredictionItemResponse]

    matched_symptoms: List[SymptomMatchResponse]

    unknown_symptoms: List[str]