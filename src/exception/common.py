from typing import Any

from fastapi import HTTPException


class CustomException(HTTPException):
    def __init__(
            self,
            status_code: int,
            detail: str,
            error_code: str | None = None,
            extra: dict[str, Any] | None = None
    ):
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code
        self.extra = extra or {}


class BadRequestException(CustomException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=400,
            detail=detail,
            error_code="BAD_REQUEST"
        )
