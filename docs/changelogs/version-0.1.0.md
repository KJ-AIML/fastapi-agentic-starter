# ALMS Changelog - Version 0.1.0

**Release Date:** March 20, 2026  
**Version:** 0.1.0  
**Codename:** "Foundation"

---

## Overview

Initial release of ALMS (Agentic Layer for Microservices) - a production-ready FastAPI boilerplate designed specifically for AI-powered backends. This release establishes the foundational architecture and core features.

---

## Major Features

### ALMS Architecture

A pragmatic layered architecture optimized for AI applications:

- **API Layer** (`src/api/`) - HTTP handling, routing, middleware
- **Execution Layer** (`src/execution/`) - Business logic, use cases
- **Agent Layer** (`src/agents/`) - AI logic, prompts, tools
- **Infrastructure** (`src/providers/`, `src/database/`) - External services

Key benefits:
- Simpler than Hexagonal (no complex ports/adapters)
- AI-First design (dedicated agent layer)
- Production-ready patterns
- Microservice-ready (each layer can be extracted)

### FastAPI Integration

High-performance API framework with:
- Async/await support throughout
- Pydantic v2 for validation
- Scalar documentation UI
- CORS and security middleware
- Standardized response format

### AI Agent Support

Built-in LangChain + LangGraph integration:
- OpenAI model support
- Agent management layer
- Prompt templates
- Tool and workflow support (extensible)

### Database Infrastructure

Production-ready database setup:
- PostgreSQL with SQLAlchemy 2.0
- Async operations via asyncpg
- Alembic migrations
- Repository pattern
- Connection pooling

### Development Tools

Complete development environment:
- UV package manager (10-100x faster than pip)
- Ruff for linting and formatting
- pytest for testing
- Docker Compose for local development
- Type hints throughout

---

## File Structure

### New Files Created

#### Core Application
- `src/api/main.py` - FastAPI application factory
- `src/api/router/routers.py` - Router aggregation
- `src/api/middlewares/error_handler.py` - Exception handling
- `src/api/middlewares/logging.py` - Request logging
- `src/api/middlewares/security.py` - Security headers
- `src/api/endpoints/v1/health.py` - Health check endpoint
- `src/api/endpoints/v1/sample_agent.py` - Sample agent endpoint
- `src/api/endpoints/v1/sample_di.py` - DI example endpoint
- `src/api/endpoints/v1/schemas/base.py` - AppResponse wrapper
- `src/api/endpoints/v1/schemas/sample.py` - Sample schemas
- `src/api/endpoints/v1/dependencies.py` - DI container
- `src/api/endpoints/v1/routers.py` - v1 router

#### Execution Layer
- `src/execution/usecases/sample_usecase.py` - Sample use case
- `src/execution/actions/sample_action.py` - Sample action

#### Agent Layer
- `src/agents/agent_manager/agent.py` - Sample agent
- `src/agents/prompts/sample_agent_prompt.py` - Sample prompts

#### Infrastructure
- `src/providers/ai/langchain_model_loader.py` - LLM loader
- `src/database/connection.py` - Database connection
- `src/database/repositories/base.py` - BaseRepository
- `src/core/exceptions.py` - Custom exceptions
- `src/config/settings.py` - Pydantic Settings
- `src/config/logs_config.py` - Logging configuration

#### Testing
- `src/tests/conftest.py` - pytest configuration
- `src/tests/v1/test_health.py` - Health tests
- `src/tests/v1/test_agent.py` - Agent tests

#### Database
- `alembic/env.py` - Alembic environment
- `alembic/script.py.mako` - Migration template
- `alembic.ini` - Alembic configuration

#### Docker
- `Dockerfile` - Container build
- `docker-compose.yml` - Service orchestration

#### Configuration
- `.env.example` - Environment template
- `.python-version` - Python version specification
- `pyproject.toml` - UV dependencies
- `uv.lock` - Locked dependencies

#### Documentation
- `docs/01-System-Design.md` - Architecture overview
- `docs/02-Design-Patterns.md` - Design patterns
- `docs/03-Database-Design.md` - Database documentation
- `docs/04-Tech-Stack.md` - Technology inventory
- `docs/05-Project-Structure.md` - Project structure
- `docs/06-API-Documentation.md` - API reference
- `docs/07-Setup-Installation.md` - Setup guide
- `docs/08-Contribution-Guide.md` - Contribution guidelines
- `docs/UPDATE-SUMMARY.md` - Documentation updates
- `docs/changelogs/version-0.1.0.md` - This file

#### Project Rules
- `rules/project_rules.md` - ALMS guidelines

#### GitHub
- `.github/workflows/ci.yml` - CI/CD pipeline
- `.github/ISSUE_TEMPLATE/bug_report.yml` - Bug report template
- `.github/ISSUE_TEMPLATE/feature_request.yml` - Feature request template
- `.github/pull_request_template.md` - PR template
- `.github/dependabot.yml` - Dependency updates

### Files Updated

#### Documentation
- `README.md` - Complete rewrite with ALMS branding

---

## Technical Details

### Dependencies

```toml
[project]
name = "fastapi-agentic-starter"
version = "0.1.0"
requires-python = ">=3.13"

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
    "pydantic>=2.12.5",
    "pydantic-settings>=2.12.0",
    "redis>=7.1.0",
    "ruff>=0.14.11",
    "scalar-fastapi>=1.6.0",
    "sqlalchemy>=2.0.44",
    "uvicorn>=0.38.0",
]

[dependency-groups]
dev = [
    "httpx>=0.28.1",
    "pytest>=9.0.2",
]
```

### API Endpoints

#### Health Check
- `GET /api/v1/health` - Service health status

#### Agent
- `POST /api/v1/agent` - Execute AI agent

#### Sample
- `GET /api/v1/sample_di` - DI demonstration
- `GET /api/v1/sample_di/{message_id}` - DI with parameter

### Response Format

All responses use standardized `AppResponse`:

```json
{
  "success": true,
  "data": {...},
  "error": null,
  "request_id": "uuid-string"
}
```

### Exception Handling

Custom exceptions with HTTP status codes:
- `AppException` - Base (500)
- `DomainException` - Business logic (400)
- `NotFoundException` - Resource not found (404)
- `ValidationException` - Input validation (422)

---

## Testing

### Test Coverage

- Unit tests for core components
- Integration tests for API endpoints
- pytest fixtures for dependency injection

### Manual Testing Completed

- ✅ Application startup
- ✅ Health endpoint
- ✅ Agent endpoint
- ✅ DI example
- ✅ Database connection
- ✅ Docker Compose setup
- ✅ Documentation rendering

---

## Documentation

### Created Documentation

| Document | Lines | Status |
|----------|-------|--------|
| README.md | ~500 | ✅ Complete |
| 01-System-Design.md | ~300 | ✅ Complete |
| 02-Design-Patterns.md | ~500 | ✅ Complete |
| 03-Database-Design.md | ~400 | ✅ Complete |
| 04-Tech-Stack.md | ~300 | ✅ Complete |
| 05-Project-Structure.md | ~400 | ✅ Complete |
| 06-API-Documentation.md | ~350 | ✅ Complete |
| 07-Setup-Installation.md | ~450 | ✅ Complete |
| 08-Contribution-Guide.md | ~500 | ✅ Complete |
| project_rules.md | ~200 | ✅ Complete |

**Total:** ~3900 lines of documentation

---

## Known Issues

- VectorDB integration pending (v0.2.0)
- Advanced LangGraph workflows pending (v0.2.0)
- Authentication system pending (v0.3.0)
- Rate limiting pending (v0.3.0)

---

## Next Steps (v0.2.0)

### High Priority
1. Vector database integration (Pinecone/Weaviate)
2. Advanced LangGraph workflows
3. Agent memory/conversation persistence
4. More comprehensive test coverage

### Medium Priority
1. Redis caching implementation
2. Background task processing (Celery)
3. Metrics collection (Prometheus)
4. Error tracking (Sentry)

---

## Breaking Changes

None - this is the initial release.

---

## Migration Guide

Not applicable - initial release.

---

## Contributors

- Project Creator: [Your Name]

---

**Full Changelog:** https://github.com/KJ-AIML/alms/commits/v0.1.0

---

*Built for the next generation of AI applications.*
