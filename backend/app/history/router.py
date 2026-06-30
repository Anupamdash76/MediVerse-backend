from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from app.auth.dependencies import get_current_user

from app.history.service import (
    history_service,
)

from app.history.schema import (
    HistoryResponse,
)

router = APIRouter(
    prefix="/history",
    tags=["History"],
)


def serialize_history(document: dict) -> HistoryResponse:

    return HistoryResponse(
        id=str(document["_id"]),
        input_symptoms=document["input_symptoms"],
        matched_symptoms=document["matched_symptoms"],
        predictions=document["predictions"],
        created_at=document["created_at"],
    )


@router.get(
    "",
    response_model=list[HistoryResponse],
)
async def get_history(
    current_user: dict = Depends(get_current_user),
):

    history = await history_service.get_predictions(
        str(current_user["_id"]),
    )

    return [
        serialize_history(item)
        for item in history
    ]


@router.get(
    "/{prediction_id}",
    response_model=HistoryResponse,
)
async def get_prediction(
    prediction_id: str,
    current_user: dict = Depends(get_current_user),
):

    prediction = await history_service.get_prediction(
        prediction_id,
    )

    if (
        prediction is None
        or prediction["user_id"] != str(current_user["_id"])
    ):

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prediction not found.",
        )

    return serialize_history(
        prediction,
    )


@router.delete(
    "/{prediction_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_prediction(
    prediction_id: str,
    current_user: dict = Depends(get_current_user),
):

    try:

        await history_service.delete_prediction(
            prediction_id,
            str(current_user["_id"]),
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )