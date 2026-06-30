from app.database.collections import (
    profiles_collection,
)


class ProfileRepository:

    async def get_profile(
        self,
        user_id: str,
    ):

        return await profiles_collection.find_one(
            {
                "user_id": user_id,
            }
        )

    async def create_profile(
        self,
        profile: dict,
    ):

        await profiles_collection.insert_one(
            profile,
        )

        return await self.get_profile(
            profile["user_id"],
        )

    async def update_profile(
        self,
        user_id: str,
        profile: dict,
    ):

        await profiles_collection.update_one(
            {
                "user_id": user_id,
            },
            {
                "$set": profile,
            },
        )

        return await self.get_profile(
            user_id,
        )


profile_repository = ProfileRepository()