"""
Metrics endpoint for Prometheus scraping.

This module provides endpoints for exposing application metrics
in Prometheus format for monitoring and alerting.
"""

from fastapi import APIRouter, Response

from src.observability.metrics import get_metrics, get_metrics_content_type

router = APIRouter(tags=["monitoring"])


@router.get("/metrics")
async def metrics():
    """
    Prometheus metrics endpoint.

    Returns metrics in Prometheus exposition format including:
    - HTTP request counts and durations
    - Database query metrics
    - AI/LLM operation metrics
    - Cache hit/miss ratios
    - Agent execution metrics

    Configure Prometheus to scrape this endpoint:
    ```yaml
    scrape_configs:
      - job_name: 'fastapi-agentic'
        static_configs:
          - targets: ['localhost:3000']
        metrics_path: '/api/v1/metrics'
    ```
    """
    return Response(content=get_metrics(), media_type=get_metrics_content_type())
