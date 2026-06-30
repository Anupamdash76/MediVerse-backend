from bson import ObjectId

from app.database.collections import users_collection


class AuthRepository:

    async def get_user_by_email(
        self,
        email: str,
    ):

        return await users_collection.find_one(
            {
                "email": email,
            }
        )

    async def get_user_by_id(
        self,
        user_id: str,
    ):

        return await users_collection.find_one(
            {
                "_id": ObjectId(user_id),
            }
        )

    async def create_user(
        self,
        user: dict,
    ):

        result = await users_collection.insert_one(
            user
        )

        return await self.get_user_by_id(
            str(result.inserted_id)
        )


auth_repository = AuthRepository()