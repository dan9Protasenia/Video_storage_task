from fastapi import Request
from fastapi.responses import JSONResponse

from src.app.core.handlers.errors import AuthError, ConflictError, InternalServerError, RegError, UserNotFoundError


async def conflict_error_handler(request: Request, exc: Exception):
    exc = ConflictError(str(exc))
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )


async def auth_error_handler(request: Request, exc: Exception):
    exc = AuthError(str(exc))
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )


async def user_not_found_error_handler(request: Request, exc: Exception):
    exc = UserNotFoundError(str(exc))
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )


async def reg_error_handler(request: Request, exc: Exception):
    exc = RegError(str(exc))
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )


async def server_error(request: Request, exc: Exception):
    exc = InternalServerError(str(exc))
    return JSONResponse(
        content={"message": exc.message},
    )
