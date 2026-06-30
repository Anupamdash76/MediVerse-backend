from datetime import datetime, timezone

from app.history.repository import (
    history_repository,
)


class HistoryService:

    async def save_prediction(
        self,
        user_id: str,
        input_symptoms: str,
        matched_symptoms: list,
        predictions: list,
    ):

        history = {
            "user_id": user_id,
            "input_symptoms": input_symptoms,
            "matched_symptoms": matched_symptoms,
            "predictions": predictions,
            "created_at": datetime.now(
                timezone.utc,
            ),
        }

        return await history_repository.save_prediction(
            history,
        )

    async def get_prediction(
        self,
        prediction_id: str,
    ):

        return await history_repository.get_prediction(
            prediction_id,
        )

    async def get_predictions(
        self,
        user_id: str,
    ):

        return await history_repository.get_predictions(
            user_id,
        )

    async def delete_prediction(
        self,
        prediction_id: str,
        user_id: str,
    ):

        deleted = await history_repository.delete_prediction(
            prediction_id,
            user_id,
        )

        if not deleted:

            raise ValueError(
                "Prediction not found."
            )


history_service = HistoryService()