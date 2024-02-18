from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.app.infrastructure.database.database import get_db
from src.app.infrastructure.database.models.user_model import UserModel

from src.app.security import auth
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


async def get_current_user(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    username = auth.verify_token(token, credentials_exception)
    result = await db.execute(select(UserModel).filter(UserModel.username == username))
    user = result.scalars().first()
    if user is None:
        raise credentials_exception
    return user
