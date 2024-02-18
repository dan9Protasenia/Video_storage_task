from pydantic import BaseModel


class Video(BaseModel):
    id: int
    title: str
    description: str
    file_path: str

    class Config:
        orm_mode = True
        from_attributes = True


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
