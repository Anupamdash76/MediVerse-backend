from bson import ObjectId

from app.database.collections import (
    predictions_collection,
)


class HistoryRepository:

    async def save_prediction(
        self,
        history: dict,
    ):

        result = await predictions_collection.insert_one(
            history,
        )

        return await self.get_prediction(
            str(result.inserted_id),
        )

    async def get_prediction(
        self,
        prediction_id: str,
    ):

        return await predictions_collection.find_one(
            {
                "_id": ObjectId(
                    prediction_id,
                )
            }
        )

    async def get_predictions(
        self,
        user_id: str,
    ):

        cursor = predictions_collection.find(
            {
                "user_id": user_id,
            }
        ).sort(
            "created_at",
            -1,
        )

        return await cursor.to_list(
            length=None,
        )

    async def delete_prediction(
        self,
        prediction_id: str,
        user_id: str,
    ):

        result = await predictions_collection.delete_one(
            {
                "_id": ObjectId(
                    prediction_id,
                ),
                "user_id": user_id,
            }
        )

        return result.deleted_count


history_repository = HistoryRepository()