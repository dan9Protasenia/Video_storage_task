from fastapi import APIRouter

from src.app.api.health import router as health_router
from src.app.api.home import router as home_router

router = APIRouter()

router.include_router(home_router)
router.include_router(health_router)
