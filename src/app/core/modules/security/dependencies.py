from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.app.core.handlers.errors import AuthError, ConflictError, UserNotFoundError
from src.app.core.modules import auth
from src.app.infrastructure.database.models.user_model import UserModel
from src.app.infrastructure.database.postgres import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        username = auth.verify_token(token)
    except AuthError as e:
        raise ConflictError(detail=str(e))

    result = await db.execute(select(UserModel).filter(UserModel.username == username))
    user = result.scalars().first()
    if user is None:
        raise UserNotFoundError(detail="User not found.")
    return user
