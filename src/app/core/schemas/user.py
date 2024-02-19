from src.app.core.schemas.base import CommonBaseModel


class User(CommonBaseModel):
    id: int
    username: str
    email: str
    is_active: bool
