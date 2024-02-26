import os
from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt

from src.app.core.handlers.errors import AuthError

SECRET_KEY = os.getenv("APP_SECRET_KEY")
ALGORITHM = os.getenv("APP_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("APP_ACCESS_TOKEN_EXPIRE_MINUTES", 15)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise AuthError(message="User not found.")
        return username
    except JWTError:
        raise AuthError(message="User not found.")
