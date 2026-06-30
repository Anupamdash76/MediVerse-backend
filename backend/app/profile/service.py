from datetime import datetime, timezone

from app.profile.repository import (
    profile_repository,
)


class ProfileService:

    async def get_profile(
        self,
        user_id: str,
    ):

        return await profile_repository.get_profile(
            user_id,
        )

    async def create_profile(
        self,
        user_id: str,
        profile_data: dict,
    ):

        existing_profile = await profile_repository.get_profile(
            user_id,
        )

        if existing_profile:

            raise ValueError(
                "Profile already exists."
            )

        now = datetime.now(
            timezone.utc,
        )

        profile = {
            "user_id": user_id,
            **profile_data,
            "created_at": now,
            "updated_at": now,
        }

        return await profile_repository.create_profile(
            profile,
        )

    async def update_profile(
        self,
        user_id: str,
        profile_data: dict,
    ):

        existing_profile = await profile_repository.get_profile(
            user_id,
        )

        if not existing_profile:

            raise ValueError(
                "Profile not found."
            )

        profile_data["updated_at"] = datetime.now(
            timezone.utc,
        )

        return await profile_repository.update_profile(
            user_id,
            profile_data,
        )


profile_service = ProfileService()