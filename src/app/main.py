from fastapi import FastAPI

from src.app.api.user.router import router as video_router
from src.app.api.web import router as home_router

app = FastAPI()

app.include_router(video_router, prefix="/video", tags=["video"])
app.include_router(home_router, prefix="", tags=["home"])
