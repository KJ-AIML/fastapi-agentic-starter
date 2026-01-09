from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.api.endpoints.v1.schemas.base import AppResponse, ErrorDetail
from src.config.logs_config import get_logger
from src.core.exceptions import AppException

logger = get_logger(__name__)


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = getattr(request.state, "request_id", "unknown")

        try:
            response = await call_next(request)
            return response
        except AppException as exc:
            logger.error(
                f"AppException: {exc.message} [request_id={request_id}]", exc_info=True
            )
            return JSONResponse(
                status_code=exc.status_code,
                content=AppResponse(
                    success=False,
                    error=ErrorDetail(
                        code=exc.error_code, message=exc.message, details=exc.details
                    ),
                    request_id=request_id,
                ).model_dump(),
            )
        except Exception as exc:
            logger.error(
                f"Unhandled Exception: {str(exc)} [request_id={request_id}]",
                exc_info=True,
            )
            return JSONResponse(
                status_code=500,
                content=AppResponse(
                    success=False,
                    error=ErrorDetail(
                        code="INTERNAL_SERVER_ERROR",
                        message="An unexpected error occurred",
                    ),
                    request_id=request_id,
                ).model_dump(),
            )
