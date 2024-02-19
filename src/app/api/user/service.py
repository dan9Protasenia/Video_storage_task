from fastapi import UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import StreamingResponse

from src.app.core.handlers.errors import InternalServerError, UserNotFoundError
from src.app.core.modules.minio.minio_client import get_minio_client
from src.app.core.schemas.video import Video
from src.app.infrastructure.database.models.video_model import VideoModel


class VideoService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.s3_client = get_minio_client()

    async def upload_video(self, video: UploadFile, title: str, description: str, bucket_name: str) -> Video:
        content = await video.read()
        file_name = video.filename
        self.s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=content)

        new_video = VideoModel(title=title, description=description, file_path=file_name)
        self.db.add(new_video)
        await self.db.commit()
        await self.db.refresh(new_video)

        return Video.from_orm(new_video)

    async def get_video_info(self, file_name: str) -> Video:
        try:
            result = await self.db.execute(select(VideoModel).where(VideoModel.file_path == file_name))
            video_info = result.scalars().first()

            if not video_info:
                raise UserNotFoundError(detail="Video not found")

            return Video(
                id=video_info.id,
                title=video_info.title,
                description=video_info.description,
                file_path=video_info.file_path,
            )
        except self.s3_client.exceptions.NoSuchKey:
            raise UserNotFoundError(detail="Video file not found in S3")

    async def get_video_content(self, file_path: str, bucket_name: str):
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=file_path)
            return StreamingResponse(response["Body"], media_type="video/mp4")
        except self.s3_client.exceptions.NoSuchKey:
            raise UserNotFoundError(detail="Video file not found in S3")

    async def update_video(self, old_file_name: str, video: UploadFile, bucket_name: str) -> dict:
        new_file_name = video.filename
        try:
            self.s3_client.delete_object(Bucket=bucket_name, Key=old_file_name)
            content = await video.read()
            self.s3_client.put_object(Bucket=bucket_name, Key=new_file_name, Body=content)
            return {"message": "Video updated successfully", "new_file_name": new_file_name}
        except Exception as e:
            raise InternalServerError(detail=str(e))

    async def delete_video(self, file_name: str, bucket_name: str) -> dict:
        try:
            self.s3_client.delete_object(Bucket=bucket_name, Key=file_name)
            return {"message": "Video deleted successfully"}
        except Exception as e:
            raise InternalServerError(detail=str(e))

    async def list_videos(self, bucket_name: str) -> list[Video]:
        try:
            response = self.s3_client.list_objects(Bucket=bucket_name)
            video_models = [
                Video(title=obj["Key"], description="", file_path=obj["Key"]) for obj in response.get("Contents", [])
            ]

            return video_models
        except Exception as e:

            raise InternalServerError(detail=str(e))
