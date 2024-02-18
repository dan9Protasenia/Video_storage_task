from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.future import select

from src.app.api.user.views import (
    delete_video_logic,
    get_video_logic,
    list_videos_logic,
    update_video_logic,
    upload_video_logic,
)
from src.app.infrastructure.database.database import AsyncSession, get_db
from src.app.infrastructure.database.models.postgres import VideoModel

router = APIRouter()


@router.post("/upload-video/")
async def upload_video(
        title: str = Form(...),
        description: str = Form(...),
        video: UploadFile = File(...),
        db: AsyncSession = Depends(get_db),
):
    return await upload_video_logic(title, description, video, bucket_name="video", db=db)


@router.get("/{file_path}")
async def get_video(file_path: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(VideoModel).where(VideoModel.file_path == file_path))
    video = result.scalars().first()
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return video


@router.put("/{old_file_name}")
async def update_video(old_file_name: str, video: UploadFile = File(...)):
    return await update_video_logic(old_file_name, video, bucket_name="video")


@router.delete("/{file_name}")
async def delete_video(file_name: str):
    return await delete_video_logic(file_name, bucket_name="video")


@router.get("/")
async def list_videos():
    return await list_videos_logic(bucket_name="video")
