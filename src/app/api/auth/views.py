from sqlalchemy.orm import Session

from src.app.infrastructure.database.models.user_model import UserModel
from src.app.security.auth import get_password_hash


async def create_user(username: str, email: str, password: str, db: Session):
    hashed_password = get_password_hash(password)
    user = UserModel(username=username, email=email, hashed_password=hashed_password, is_active=True)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
