import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from src.config.logs_config import get_logger, request_id_ctx

logger = get_logger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Generate or retrieve request_id
        request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        request.state.request_id = request_id

        # Set request_id in context for logging
        request_id_ctx.set(request_id)

        start_time = time.time()

        logger.info(
            f"Request started: {request.method} {request.url.path} [id={request_id}]"
        )

        response = await call_next(request)

        process_time = time.time() - start_time
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = str(process_time)

        logger.info(
            f"Request finished: {request.method} {request.url.path} - {response.status_code} [id={request_id}, time={process_time:.4f}s]"
        )

        return response
