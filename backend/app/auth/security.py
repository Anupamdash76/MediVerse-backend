from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from app.config.settings import (
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    """
    Hash a plain-text password.
    """
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    Verify a password against its hash.
    """
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(
    data: dict,
) -> str:
    """
    Generate a JWT access token.
    """

    payload = data.copy()

    expire = datetime.now(
        timezone.utc
    ) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )