from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.app.api.auth import views as auth_views
from src.app.infrastructure.database.database import get_db
from src.app.infrastructure.database.models.user_model import UserModel
from src.app.security import auth

router = APIRouter()


@router.post("/register")
async def register_user(username: str, email: str, password: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserModel).filter(UserModel.username == username))
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = await auth_views.create_user(username, email, password, db)
    return {"message": "User created successfully", "user": user}


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserModel).where(UserModel.username == form_data.username))
    user = result.scalars().first()

    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
