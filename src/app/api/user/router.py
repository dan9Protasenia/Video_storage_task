from fastapi import APIRouter, Depends

from src.app.api.user.views import (
    delete_video_view,
    get_video_content_view,
    get_video_info_view,
    list_videos_view,
    update_video_view,
    upload_video_view,
)
from src.app.core.modules.security import get_current_user
from src.app.core.schemas.schemas import Video

router = APIRouter()

router.add_api_route(
    path="/upload-video/",
    endpoint=upload_video_view,
    methods=["POST"],
    response_model=Video,
    status_code=200,
    dependencies=[Depends(get_current_user)],
    description="Upload a new video",
)

router.add_api_route(
    path="/video-info/{file_path}",
    endpoint=get_video_info_view,
    methods=["GET"],
    response_model=Video,
    status_code=200,
    dependencies=[Depends(get_current_user)],
    description="Get a video info",
)

router.add_api_route(
    path="/{file_path}",
    endpoint=get_video_content_view,
    methods=["GET"],
    response_model=None,
    status_code=200,
    dependencies=[Depends(get_current_user)],
    description="Get a specific video",
)

router.add_api_route(
    path="/{old_file_name}",
    endpoint=update_video_view,
    methods=["PUT"],
    status_code=200,
    dependencies=[Depends(get_current_user)],
    description="Update an existing video",
)

router.add_api_route(
    path="/{file_name}",
    endpoint=delete_video_view,
    methods=["DELETE"],
    status_code=200,
    dependencies=[Depends(get_current_user)],
    description="Delete a video",
)

router.add_api_route(
    path="/videos/",
    endpoint=list_videos_view,
    methods=["GET"],
    response_model=list[Video],
    status_code=200,
    dependencies=[Depends(get_current_user)],
    description="List all videos",
)
