"""
Observability module for tracing, metrics, and logging.

Provides:
- OpenTelemetry tracing
- Prometheus metrics
- Automatic instrumentation middleware
"""

from src.observability.tracing import (
    setup_tracing,
    instrument_fastapi,
    tracer,
    trace_span,
    trace_function,
    get_tracer,
)

from src.observability.metrics import (
    setup_metrics,
    get_metrics,
    get_metrics_content_type,
    timed_metric,
    measure_duration,
    MetricsCollector,
    # Pre-defined metrics
    http_requests_total,
    http_request_duration_seconds,
    db_queries_total,
    db_query_duration_seconds,
    ai_requests_total,
    ai_request_duration_seconds,
    ai_tokens_total,
    usecase_executions_total,
    usecase_duration_seconds,
    cache_hits_total,
    cache_misses_total,
    agent_executions_total,
    agent_execution_duration_seconds,
)

__all__ = [
    "setup_tracing",
    "instrument_fastapi",
    "tracer",
    "trace_span",
    "trace_function",
    "get_tracer",
    "setup_metrics",
    "get_metrics",
    "get_metrics_content_type",
    "timed_metric",
    "measure_duration",
    "MetricsCollector",
    "http_requests_total",
    "http_request_duration_seconds",
    "db_queries_total",
    "db_query_duration_seconds",
    "ai_requests_total",
    "ai_request_duration_seconds",
    "ai_tokens_total",
    "usecase_executions_total",
    "usecase_duration_seconds",
    "cache_hits_total",
    "cache_misses_total",
    "agent_executions_total",
    "agent_execution_duration_seconds",
]
