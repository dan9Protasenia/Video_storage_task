from fastapi import APIRouter
from starlette import status

from src.app.api.auth.views import login_user, register_user
from src.app.core.schemas.schemas import Token, User

router = APIRouter()

router.add_api_route(
    path="/register/",
    endpoint=register_user,
    methods=["POST"],
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    description="Create a new user",
)

router.add_api_route(
    path="/login/",
    endpoint=login_user,
    methods=["POST"],
    response_model=Token,
    status_code=status.HTTP_200_OK,
    description="Authenticate user and retrieve token",
)
