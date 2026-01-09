from fastapi import APIRouter, Depends, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.endpoints.v1.schemas.base import AppResponse
from src.config.logs_config import get_logger
from src.database.connection import get_db

router = APIRouter()
logger = get_logger(__name__)


@router.get("", response_model=AppResponse[dict], status_code=status.HTTP_200_OK)
async def health_check(db: AsyncSession = Depends(get_db)):
    """Health check endpoint for v1 API with DB check"""
    logger.debug("Health check requested")

    db_status = "unhealthy"
    try:
        # Simple query to check DB connectivity
        await db.execute(text("SELECT 1"))
        db_status = "healthy"
    except Exception as e:
        logger.error(f"Database health check failed: {str(e)}")

    return AppResponse(
        success=True,
        data={
            "status": "healthy",
            "version": "v1",
            "service": "FastAPI Agentic Starter",
            "dependencies": {"database": db_status},
        },
    )
