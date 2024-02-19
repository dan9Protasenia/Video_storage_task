from fastapi import Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.api.user.service import VideoService
from src.app.core.schemas.schemas import Video
from src.app.infrastructure.database.database import get_db


async def upload_video_view(
    title: str, description: str, video: UploadFile, db: AsyncSession = Depends(get_db)
) -> Video:
    video_service = VideoService(db)
    return await video_service.upload_video(video, title, description, "video")


async def get_video_info_view(file_path: str, db: AsyncSession = Depends(get_db)):
    video_service = VideoService(db)
    return await video_service.get_video_info(file_path)


async def get_video_content_view(file_path: str, db: AsyncSession = Depends(get_db)):
    video_service = VideoService(db)
    return await video_service.get_video_content(file_path, "video")


async def update_video_view(old_file_name: str, video: UploadFile, db: AsyncSession = Depends(get_db)) -> list:
    video_service = VideoService(db)
    return await video_service.update_video(old_file_name, video, "video")


async def delete_video_view(file_name: str, db: AsyncSession = Depends(get_db)) -> list:
    video_service = VideoService(db)
    return await video_service.delete_video(file_name, "video")


async def list_videos_view(db: AsyncSession = Depends(get_db)) -> list:
    video_service = VideoService(db)
    return await video_service.list_videos("video")
