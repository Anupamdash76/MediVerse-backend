from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from app.auth.dependencies import get_current_user

from app.profile.schema import (
    ProfileRequest,
    ProfileResponse,
)

from app.profile.service import (
    profile_service,
)

router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
)


@router.post(
    "",
    response_model=ProfileResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_profile(
    request: ProfileRequest,
    current_user: dict = Depends(get_current_user),
):

    try:

        profile = await profile_service.create_profile(
            user_id=str(current_user["_id"]),
            profile_data=request.model_dump(),
        )

        return ProfileResponse(**{
            key: value
            for key, value in profile.items()
            if key in ProfileResponse.model_fields
        })

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "",
    response_model=ProfileResponse,
)
async def get_profile(
    current_user: dict = Depends(get_current_user),
):

    profile = await profile_service.get_profile(
        str(current_user["_id"]),
    )

    if not profile:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found.",
        )

    return ProfileResponse(**{
        key: value
        for key, value in profile.items()
        if key in ProfileResponse.model_fields
    })


@router.put(
    "",
    response_model=ProfileResponse,
)
async def update_profile(
    request: ProfileRequest,
    current_user: dict = Depends(get_current_user),
):

    try:

        profile = await profile_service.update_profile(
            user_id=str(current_user["_id"]),
            profile_data=request.model_dump(),
        )

        return ProfileResponse(**{
            key: value
            for key, value in profile.items()
            if key in ProfileResponse.model_fields
        })

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )