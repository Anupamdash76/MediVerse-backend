from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from app.auth.dependencies import get_current_user

from app.history.service import (
    history_service,
)

from app.schema.api import (
    PredictRequest,
    PredictResponse,
    PredictionItemResponse,
    SymptomMatchResponse,
)

from app.services.prediction_service import PredictionService


router = APIRouter(
    prefix="/predict",
    tags=["Prediction"],
)

prediction_service = PredictionService()


@router.post(
    "",
    response_model=PredictResponse,
)
async def predict(
    request: PredictRequest,
    current_user: dict = Depends(get_current_user),
):

    try:

        result = prediction_service.predict(
            request.symptoms
        )

        predictions = [

            PredictionItemResponse(

                disease=item["disease"],

                summary=item["summary"],

                recommended_medicines=item["recommended_medicines"],

                precautions=item["precautions"],

                doctor_speciality=item["doctor_speciality"],

                severity=item["severity"],

                disclaimer=item["disclaimer"],

            )

            for item in result["predictions"]

        ]

        matches = [

            SymptomMatchResponse(

                input=match.input,

                matched=match.matched,

                score=match.score,

            )

            for match in result["matched_symptoms"]

        ]

        # ------------------------------------
        # Save Prediction History
        # ------------------------------------

        await history_service.save_prediction(

            user_id=str(current_user["_id"]),

            input_symptoms=request.symptoms,

            matched_symptoms=[
                {
                    "input": match.input,
                    "matched": match.matched,
                    "score": match.score,
                }
                for match in result["matched_symptoms"]
            ],

            predictions=result["predictions"],

        )

        return PredictResponse(

            predictions=predictions,

            matched_symptoms=matches,

            unknown_symptoms=result["unknown_symptoms"],

        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )