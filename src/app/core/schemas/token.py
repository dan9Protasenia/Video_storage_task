from src.app.core.schemas.base import CommonBaseModel


class Token(CommonBaseModel):
    access_token: str
    token_type: str
