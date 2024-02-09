from fastapi import HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from src.app.infrastructure.minio.minio_client import get_minio_client


async def upload_video_logic(video: UploadFile, bucket_name: str):
    s3_client = get_minio_client()
    content = await video.read()
    file_name = video.filename
    s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=content)
    return {"message": "Video uploaded successfully", "file_name": file_name}


async def get_video_logic(file_name: str, bucket_name: str):
    s3_client = get_minio_client()
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        return StreamingResponse(response['Body'], media_type="video/mp4")
    except s3_client.exceptions.NoSuchKey:
        raise HTTPException(status_code=404, detail="Video not found")


async def update_video_logic(old_file_name: str, video: UploadFile, bucket_name: str):
    s3_client = get_minio_client()
    content = await video.read()
    new_file_name = video.filename

    try:
        s3_client.delete_object(Bucket=bucket_name, Key=old_file_name)
        s3_client.put_object(Bucket=bucket_name, Key=new_file_name, Body=content)
        return {"message": "Video updated successfully", "new_file_name": new_file_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def delete_video_logic(file_name: str, bucket_name: str):
    s3_client = get_minio_client()
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        return {"message": "Video deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def list_videos_logic(bucket_name: str):
    s3_client = get_minio_client()
    try:
        response = s3_client.list_objects(Bucket=bucket_name)
        videos = [obj['Key'] for obj in response.get('Contents', [])]
        return {"videos": videos}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
