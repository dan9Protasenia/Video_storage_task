class BaseError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class RegError(BaseError):
    def __init__(self, message: str):
        super().__init__(message)


class AuthError(BaseError):
    def __init__(self, message: str):
        super().__init__(message)


class UserNotFoundError(BaseError):
    def __init__(self, message: str):
        super().__init__(message)


class ConflictError(BaseError):
    def __init__(self, message: str):
        super().__init__(message)


class InternalServerError(BaseError):
    def __init__(self, message: str):
        super().__init__(message)
