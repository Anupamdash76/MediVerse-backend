from pydantic import BaseModel, Field
from typing import List, Literal


class ProfileRequest(BaseModel):
    age: int = Field(..., ge=0, le=120)

    gender: Literal[
        "Male",
        "Female",
        "Other",
    ]

    height_cm: float = Field(..., gt=0)

    weight_kg: float = Field(..., gt=0)

    blood_group: str

    allergies: List[str] = []

    chronic_diseases: List[str] = []

    current_medications: List[str] = []