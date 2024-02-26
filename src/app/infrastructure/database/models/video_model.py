from sqlalchemy import Column, Integer, String

from .base import Base


class VideoModel(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    file_path = Column(String, index=True)
