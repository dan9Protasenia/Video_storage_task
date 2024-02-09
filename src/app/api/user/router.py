from fastapi import APIRouter, File, UploadFile

from src.app.infrastructure.minio.minio_client import get_minio_client

router = APIRouter()


@router.post("/upload-video/")
async def upload_video(video: UploadFile = File(...)):
    s3_client = get_minio_client()
    content = await video.read()
    bucket_name = "video"
    file_name = video.filename
    response = s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=content)
    return {"message": "Video uploaded successfully", "response": response}
