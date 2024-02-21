from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.api.auth.service import AuthService
from src.app.core.schemas.token import Token
from src.app.core.schemas.user import User
from src.app.infrastructure.database.postgres import get_db


async def register_user(username: str, email: str, password: str, db: AsyncSession = Depends(get_db)) -> User:
    auth_service = AuthService(db)
    return await auth_service.register(username, email, password)


async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)) -> Token:
    auth_service = AuthService(db)
    return await auth_service.login(form_data.username, form_data.password)
