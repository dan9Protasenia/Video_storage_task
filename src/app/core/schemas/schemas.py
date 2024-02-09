from pydantic import BaseModel


class Video(BaseModel):
    id: int
    title: str
    description: str
    file_path: str


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
