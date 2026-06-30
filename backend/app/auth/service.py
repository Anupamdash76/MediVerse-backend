from datetime import datetime, timezone

from app.auth.repository import auth_repository
from app.auth.security import (
    hash_password,
    verify_password,
    create_access_token,
)


class AuthService:

    async def register(
        self,
        name: str,
        email: str,
        password: str,
    ):

        # Check if email already exists
        existing_user = await auth_repository.get_user_by_email(
            email
        )

        if existing_user:

            raise ValueError(
                "Email already registered."
            )

        now = datetime.now(timezone.utc)

        user = {
            "name": name,
            "email": email,
            "password": hash_password(password),
            "created_at": now,
            "updated_at": now,
        }

        created_user = await auth_repository.create_user(
            user
        )

        token = create_access_token(
            {
                "sub": str(created_user["_id"]),
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "id": str(created_user["_id"]),
                "name": created_user["name"],
                "email": created_user["email"],
            },
        }

    async def login(
        self,
        email: str,
        password: str,
    ):

        user = await auth_repository.get_user_by_email(
            email
        )

        if not user:

            raise ValueError(
                "Invalid email or password."
            )

        if not verify_password(
            password,
            user["password"],
        ):

            raise ValueError(
                "Invalid email or password."
            )

        token = create_access_token(
            {
                "sub": str(user["_id"]),
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "id": str(user["_id"]),
                "name": user["name"],
                "email": user["email"],
            },
        }


auth_service = AuthService()