from fastapi import APIRouter

# Import v1 endpoints
from src.api.endpoints.v1 import health, sample_agent, sample_di

# Create v1 router
v1_router = APIRouter()

# Include v1 endpoints
v1_router.include_router(health.router, prefix="/health")
v1_router.include_router(sample_agent.router, prefix="/agent")
v1_router.include_router(sample_di.router, prefix="/sample_di")
