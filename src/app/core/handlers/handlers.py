from fastapi import Request
from fastapi.responses import JSONResponse

from src.app.core.handlers.errors import AuthError, ConflictError, InternalServerError, RegError, UserNotFoundError


async def conflict_error_handler(request: Request, exc: ConflictError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


async def auth_error_handler(request: Request, exc: AuthError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


async def user_not_found_error_handler(request: Request, exc: UserNotFoundError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


async def reg_error_handler(request: Request, exc: RegError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


async def server_error(request: Request, exc: InternalServerError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
