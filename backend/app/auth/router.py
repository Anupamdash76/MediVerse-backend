from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from app.auth.dependencies import get_current_user
from app.auth.service import auth_service

from app.auth.schema import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
    UserResponse,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    request: RegisterRequest,
):

    try:

        return await auth_service.register(
            name=request.name,
            email=request.email,
            password=request.password,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login(
    request: LoginRequest,
):

    try:

        return await auth_service.login(
            email=request.email,
            password=request.password,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )


@router.get(
    "/me",
    response_model=UserResponse,
    summary="Current User",
)
async def get_current_user_profile(
    current_user=Depends(get_current_user),
):
    """
    Return the authenticated user's profile.
    """

    return UserResponse(
        id=str(current_user["_id"]),
        name=current_user["name"],
        email=current_user["email"],
    )