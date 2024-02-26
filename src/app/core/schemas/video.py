from typing import Optional

from src.app.core.schemas.base import CommonBaseModel


class Video(CommonBaseModel):
    id: Optional[int] = None
    title: str
    description: str
    file_path: str
