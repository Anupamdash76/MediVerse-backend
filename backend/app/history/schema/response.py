from datetime import datetime

from pydantic import BaseModel

from typing import List


class MatchedSymptomResponse(BaseModel):

    input: str

    matched: str

    score: float


class DiseaseResponse(BaseModel):

    disease: str

    summary: str

    recommended_medicines: List[str]

    precautions: List[str]

    doctor_speciality: str

    severity: str

    disclaimer: str


class HistoryResponse(BaseModel):

    id: str

    input_symptoms: str

    matched_symptoms: List[
        MatchedSymptomResponse
    ]

    predictions: List[
        DiseaseResponse
    ]

    created_at: datetime