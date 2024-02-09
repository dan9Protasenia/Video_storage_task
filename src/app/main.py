from fastapi import FastAPI

from src.app.api.user.router import router as video_router

app = FastAPI()

app.include_router(video_router, prefix="/video", tags=["video"])
