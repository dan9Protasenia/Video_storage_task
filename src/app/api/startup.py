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


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url="/documentation",
        openapi_url="/openapi.json",
        title="FastAPI Monolithic Web Application",
        description="API for video management and secure user authentication.",
        version="1.0.0",
    )

    init_routers(app)
    init_middlewares(app)

    return app


def init_routers(app: FastAPI) -> None:
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(video_router, prefix="/video", tags=["video"])
    app.include_router(web_router, tags=["web"])

    app.add_exception_handler(UserNotFoundError, user_not_found_error_handler)
    app.add_exception_handler(ConflictError, conflict_error_handler)
    app.add_exception_handler(AuthError, auth_error_handler)
    app.add_exception_handler(InternalServerError, server_error)


def init_middlewares(app: FastAPI) -> None:
    pass


app = create_app()
