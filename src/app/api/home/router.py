from fastapi import APIRouter
from starlette import status

from src.app.api.home.views import health, home

router = APIRouter()

router.add_api_route(
    path="/home/",
    endpoint=home,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    description="Home page",
)

router.add_api_route(
    path="/health/",
    endpoint=health,
    methods=["GET"],
    description="Home page",
)
