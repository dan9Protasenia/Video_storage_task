from fastapi import APIRouter, File, UploadFile

from .views import delete_video_logic, get_video_logic, list_videos_logic, update_video_logic, upload_video_logic

router = APIRouter()


@router.post("/upload-video/")
async def upload_video(video: UploadFile = File(...)):
    return await upload_video_logic(video, bucket_name="video")


@router.get("/{file_name}")
async def get_video(file_name: str):
    return await get_video_logic(file_name, bucket_name="video")


@router.put("/{old_file_name}")
async def update_video(old_file_name: str, video: UploadFile = File(...)):
    return await update_video_logic(old_file_name, video, bucket_name="video")


@router.delete("/{file_name}")
async def delete_video(file_name: str):
    return await delete_video_logic(file_name, bucket_name="video")


@router.get("/")
async def list_videos():
    return await list_videos_logic(bucket_name="video")
