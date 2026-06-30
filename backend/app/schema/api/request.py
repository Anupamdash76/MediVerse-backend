from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    """
    Request body for disease prediction.
    """

    symptoms: str = Field(
        ...,
        min_length=1,
        examples=[
            "headache, vomiting, fever",
            "I have severe headache with nausea and vomiting"
        ],
        description="Comma-separated symptoms or free-text symptom description."
    )