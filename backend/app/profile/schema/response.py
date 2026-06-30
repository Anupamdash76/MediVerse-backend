from pydantic import BaseModel
from typing import List


class ProfileResponse(BaseModel):
    age: int

    gender: str

    height_cm: float

    weight_kg: float

    blood_group: str

    allergies: List[str]

    chronic_diseases: List[str]

    current_medications: List[str]