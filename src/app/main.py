from fastapi import FastAPI

from src.app.api.auth.router import router as auth_router
from src.app.api.user.router import router as video_router
from src.app.api.web import router as web_router
from src.app.core.handlers.errors import AuthError, ConflictError, InternalServerError, UserNotFoundError
from src.app.core.handlers.handlers import (
    auth_error_handler,
    conflict_error_handler,
    server_error,
    user_not_found_error_handler,
)

app = FastAPI()

app.include_router(video_router, prefix="/video", tags=["video"])
app.include_router(web_router, prefix="", tags=["web"])
app.include_router(auth_router, prefix="", tags=["auth"])

app.add_exception_handler(UserNotFoundError, user_not_found_error_handler)
app.add_exception_handler(ConflictError, conflict_error_handler)
app.add_exception_handler(AuthError, auth_error_handler)
app.add_exception_handler(InternalServerError, server_error)
