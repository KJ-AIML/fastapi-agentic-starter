# 04 - Tech Stack

> **Last Updated:** March 20, 2026  
> **Version:** 0.2.0  
> **Status:** ✅ Active

## Core Framework

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.13+ | Programming language |
| **FastAPI** | 0.122.0+ | High-performance web framework |
| **Uvicorn** | 0.38.0+ | ASGI server |
| **Pydantic** | 2.12.5+ | Data validation and settings management |
| **Pydantic-Settings** | 2.12.0+ | Environment-based configuration |

## AI & LLM

| Technology | Version | Purpose |
|------------|---------|---------|
| **LangChain** | 1.1.0+ | LLM orchestration framework |
| **LangGraph** | 1.0.4+ | Agent workflow graphs |
| **LangChain-OpenAI** | 1.1.0+ | OpenAI integration |
| **LangChain-Community** | 0.4.1+ | Community integrations |
| **LangChain-MCP-Adapters** | 0.1.14+ | Model Context Protocol adapters |
| **OpenAI** | 2.8.1+ | OpenAI API client |

## Database

| Technology | Version | Purpose |
|------------|---------|---------|
| **PostgreSQL** | 15+ | Primary database |
| **SQLAlchemy** | 2.0.44+ | ORM and query builder |
| **asyncpg** | 0.31.0+ | Async PostgreSQL driver |
| **Alembic** | 1.17.2+ | Database migrations |
| **Redis** | 7.1.0+ | Caching and message broker |

## Observability

| Technology | Version | Purpose |
|------------|---------|---------|
| **OpenTelemetry API** | 1.25.0+ | Distributed tracing API |
| **OpenTelemetry SDK** | 1.25.0+ | Tracing implementation |
| **OpenTelemetry FastAPI** | 0.46b0+ | FastAPI auto-instrumentation |
| **OpenTelemetry SQLAlchemy** | 0.46b0+ | Database query tracing |
| **OpenTelemetry Redis** | 0.46b0+ | Cache operation tracing |
| **OpenTelemetry OTLP** | 1.25.0+ | Trace export protocol |
| **Prometheus Client** | 0.20.0+ | Metrics collection |

## Documentation

| Technology | Version | Purpose |
|------------|---------|---------|
| **Scalar** | 1.6.0+ | Modern API documentation UI |
| **FastAPI Standard** | 0.122.0+ | Built-in OpenAPI/Swagger |

## Development Tools

| Technology | Version | Purpose |
|------------|---------|---------|
| **pytest** | 9.0.2+ | Testing framework |
| **httpx** | 0.28.1+ | HTTP client for testing |
| **Ruff** | 0.14.11+ | Python linter and formatter |

## Package Management

| Tool | Purpose |
|------|---------|
| **uv** | Modern Python package manager (replacing pip) |

## Docker & Deployment

| Technology | Version | Purpose |
|------------|---------|---------|
| **Docker** | Latest | Containerization |
| **Docker Compose** | Latest | Multi-container orchestration |

## External Services

| Service | Purpose | Integration |
|---------|---------|-------------|
| **OpenAI API** | LLM inference | Via LangChain OpenAI adapter |
| **Google AI (optional)** | Alternative LLM | Via LangChain Community |
| **PostgreSQL** | Primary database | Via SQLAlchemy + asyncpg |
| **Redis** | Caching & queues | Via redis-py |

## Python Version Requirements

- **Minimum:** Python 3.13
- **Recommended:** Python 3.13 or newer
- **Type Hints:** Full type annotation support
- **Async/Await:** Native async support throughout

## Dependencies Overview

### Production Dependencies

```toml
[project]
dependencies = [
    "alembic>=1.17.2",
    "asyncpg>=0.31.0",
    "fastapi[standard]>=0.122.0",
    "langchain>=1.1.0",
    "langchain-community>=0.4.1",
    "langchain-mcp-adapters>=0.1.14",
    "langchain-openai>=1.1.0",
    "langgraph>=1.0.4",
    "openai>=2.8.1",
    "opentelemetry-api>=1.25.0",
    "opentelemetry-sdk>=1.25.0",
    "opentelemetry-instrumentation-fastapi>=0.46b0",
    "opentelemetry-instrumentation-sqlalchemy>=0.46b0",
    "opentelemetry-instrumentation-redis>=0.46b0",
    "opentelemetry-exporter-otlp>=1.25.0",
    "prometheus-client>=0.20.0",
    "pydantic>=2.12.5",
    "pydantic-settings>=2.12.0",
    "redis>=7.1.0",
    "ruff>=0.14.11",
    "scalar-fastapi>=1.6.0",
    "sqlalchemy>=2.0.44",
    "uvicorn>=0.38.0",
]
```

### Development Dependencies

```toml
[dependency-groups]
dev = [
    "httpx>=0.28.1",
    "pytest>=9.0.2",
]
```

## Key Technology Decisions

### Why FastAPI?

- **Performance:** Built on Starlette and Pydantic for high performance
- **Type Safety:** Native Pydantic integration for request/response validation
- **Async Support:** First-class async/await support
- **Auto Documentation:** Automatic OpenAPI/Swagger generation
- **Modern Python:** Uses modern Python features (type hints, dataclasses)

### Why SQLAlchemy 2.0?

- **Unified API:** Same syntax for sync and async operations
- **Type Safety:** Improved type hints and IDE support
- **Performance:** Optimized query compilation and execution
- **Flexibility:** Supports multiple database backends
- **Future-Proof:** Latest version with long-term support

### Why LangChain + LangGraph?

- **Agent Orchestration:** Built-in tools for building AI agents
- **Workflow Management:** LangGraph for complex agent workflows
- **Provider Agnostic:** Easy to swap between OpenAI, Anthropic, etc.
- **Production Ready:** Battle-tested in production environments
- **Community:** Large ecosystem of integrations

### Why Alembic?

- **SQLAlchemy Native:** Designed specifically for SQLAlchemy
- **Version Control:** Database migrations tracked like code
- **Autogeneration:** Can auto-generate migrations from model changes
- **Team Collaboration:** Consistent database state across environments

### Why Redis?

- **Speed:** In-memory storage for ultra-fast caching
- **Versatility:** Supports caching, sessions, message queues
- **Simplicity:** Simple API, easy to integrate
- **Production Ready:** Battle-tested at scale

### Why OpenTelemetry?

- **Vendor Neutral:** Avoid vendor lock-in, works with any backend
- **Standards Based:** CNCF project with broad industry adoption
- **Auto-Instrumentation:** Minimal code changes required
- **Distributed Tracing:** Follow requests across services
- **AI Monitoring:** Track LLM calls with token usage and costs

### Why Prometheus?

- **Industry Standard:** De facto standard for metrics in cloud-native
- **Pull Model:** Simple HTTP endpoint for metric collection
- **Rich Ecosystem:** Grafana, Alertmanager integration
- **Performance:** Minimal overhead on application

### Why Ruff?

- **Speed:** Written in Rust, extremely fast
- **All-in-One:** Replaces flake8, black, isort, pydocstyle
- **Compatibility:** Drop-in replacement for existing tools
- **Active Development:** Rapidly evolving with new features

### Why uv?

- **Speed:** 10-100x faster than pip
- **Modern:** Built for modern Python packaging (PEP 621)
- **Lock Files:** Built-in lock file support for reproducible builds
- **Workspace Support:** Excellent for monorepos
- **Cache Efficient:** Aggressive caching for faster installs

## Technology Constraints

### Python Version
- Must use Python 3.13 or newer
- Full type hint support required
- Async/await patterns throughout

### Database
- PostgreSQL 15+ recommended
- Async operations required (no sync DB calls)
- Migration files must be committed

### AI Models
- OpenAI API key required for agent features
- Google AI optional (alternative provider)
- Model selection configurable via environment

### Development
- Ruff for linting and formatting
- pytest for testing
- Type hints required on all functions

## Upgrade Policy

### Major Versions
- Review changelogs before upgrading
- Test in staging environment
- Update documentation

### Minor/Patch Versions
- Automatic updates via Dependabot
- Weekly review of security updates
- Pin versions in production

## Future Considerations

### Potential Additions

| Technology | Purpose | Status |
|------------|---------|--------|
| **Celery** | Distributed task queue | ⏳ Planned |
| **Prometheus** | Metrics collection | ✅ Active |
| **Grafana** | Metrics visualization | ⏳ Planned |
| **Sentry** | Error tracking | ⏳ Planned |
| **MinIO** | Object storage | ❌ Under Review |
| **Elasticsearch** | Search engine | ❌ Under Review |

**Updated:** v0.2.0 - Added OpenTelemetry and Prometheus observability stack
