from typing import Any, Dict, Optional


class AppException(Exception):
    """Base exception for the application"""

    def __init__(
        self,
        message: str,
        status_code: int = 500,
        error_code: str = "INTERNAL_SERVER_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details


class DomainException(AppException):
    """Exception related to business logic/domain constraints"""

    def __init__(
        self,
        message: str,
        error_code: str = "DOMAIN_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message, status_code=400, error_code=error_code, details=details
        )


class NotFoundException(AppException):
    """Exception raised when a resource is not found"""

    def __init__(
        self,
        message: str,
        error_code: str = "NOT_FOUND",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message, status_code=404, error_code=error_code, details=details
        )


class ValidationException(AppException):
    """Exception raised for input validation errors"""

    def __init__(
        self,
        message: str,
        error_code: str = "VALIDATION_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message, status_code=422, error_code=error_code, details=details
        )
