from sqlalchemy import Boolean, Column, Integer, String

from .base import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}', is_active='{self.is_active}')>"
