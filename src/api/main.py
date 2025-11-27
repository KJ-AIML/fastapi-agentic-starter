from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.config.settings import settings
from src.config.logs_config import get_logger

from src.api.endpoints.router.routers import api_router

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan events for the FastAPI application"""
    # Startup
    logger.info("Starting FastAPI Agentic Starter")
    yield
    # Shutdown
    logger.info("Shutting down FastAPI Agentic Starter")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application"""

    app = FastAPI(
        title="FastAPI Agentic Starter",
        description="Backend API for FastAPI Agentic Starter",
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/docs",
    )

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API router
    app.include_router(api_router, prefix=settings.API_PREFIX)

    # Health check endpoint
    @app.get("/")
    async def check():
        return {
            "status": "healthy",
            "service": "FastAPI Agentic Starter",
        }

    logger.info("FastAPI application configured successfully")
    return app


# Create the application instance
app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.api.main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        log_level=settings.LOG_LEVEL,
        reload=settings.DEBUG,
    )
