from fastapi import FastAPI

from ..core.handlers.errors import AuthError, ConflictError, InternalServerError, UserNotFoundError
from ..core.handlers.handlers import (
    auth_error_handler,
    conflict_error_handler,
    server_error,
    user_not_found_error_handler,
)
from .auth.router import router as auth_router
from .home.router import router as home_router
from .user.router import router as video_router


def init_routers(app: FastAPI) -> None:
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(video_router, prefix="/video", tags=["video"])
    app.include_router(home_router, prefix="/web", tags=["web"])

    app.add_exception_handler(UserNotFoundError, user_not_found_error_handler)
    app.add_exception_handler(ConflictError, conflict_error_handler)
    app.add_exception_handler(AuthError, auth_error_handler)
    app.add_exception_handler(InternalServerError, server_error)
