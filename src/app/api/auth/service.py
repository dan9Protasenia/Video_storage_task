from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.app.core.handlers.errors import AuthError, RegError
from src.app.core.modules.auth.jwt_handler import create_access_token
from src.app.core.modules.auth.password_handler import get_password_hash, verify_password
from src.app.core.schemas.token import Token
from src.app.core.schemas.user import User
from src.app.infrastructure.database.models.user_model import UserModel


class AuthService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def register(self, username: str, email: str, password: str) -> User:
        existing_user = await self.db.execute(select(UserModel).filter(UserModel.username == username))
        if existing_user.scalars().first() is not None:
            raise RegError("Username already registered.")

        existing_email = await self.db.execute(select(UserModel).filter(UserModel.email == email))
        if existing_email.scalars().first() is not None:
            raise RegError("Mail is already registered")

        hashed_password = get_password_hash(password)
        new_user = UserModel(username=username, email=email, hashed_password=hashed_password, is_active=True)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return User.from_orm(new_user)

    async def login(self, username: str, password: str) -> Token:
        result = await self.db.execute(select(UserModel).where(UserModel.username == username))
        user = result.scalars().first()

        if not user or not verify_password(password, user.hashed_password):
            raise AuthError("Incorrect username or password")

        access_token = create_access_token(data={"sub": user.username})
        return Token(access_token=access_token, token_type="bearer")
