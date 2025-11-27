# FastAPI-Agentic-Starter
> **The AI-First Backend for Scalable, Intelligent Applications.**

<p align="center">
  <img src="assets/images/asset_image_01.png" width="800" alt="FastAPI Agentic Starter Hero">
</p>

## Introduction
**FastAPI-Agentic-Starter** is a production-ready boilerplate designed for building robust, AI-powered backends. Built with a "AI-First" philosophy, it combines the performance of FastAPI with a modular architecture that treats LLM interactions as first-class citizens. Whatever you're building autonomous agents, RAG pipelines, or intelligent APIs, this starter kit provides the scalability and clean code structure you need to move fast.

## Key Features

- 🤖 **AI-Native Architecture**: Dedicated `src/agents` layer for managing LLM logic, tools, and complex agentic workflows, keeping your AI logic distinct from standard API routes.
- 🔌 **Provider Pattern**: Cleanly separate external services with `src/providers`. Easily swap or upgrade integrations for OpenAI, Supabase, Redis, or VectorDBs without tangling your business logic.
- 🧠 **Business Logic Separation**: Clear distinction between `usecases` and `actions` within `src/execution`, ensuring your core application logic remains testable and maintainable.
- 💾 **Database Abstraction**: Robust Repository pattern implementation in `src/database` for flexible data access and management.
- ⚡ **Async-Ready & High Performance**: Built on **FastAPI**, fully leveraging Python's async capabilities for high-throughput, low-latency applications.

## Folder Structure

A hybrid architecture combining Layered & Hexagonal concepts for maximum flexibility.

```text
src/
├── agents/       # LLM logic, prompts, tools, and agent definitions
├── api/          # FastAPI routes, dependencies, and request/response models
├── config/       # Configuration settings and environment variables
├── database/     # Database connection, migrations, and repository implementations
├── execution/    # Core business logic (usecases, actions)
├── providers/    # External service integrations (OpenAI, Supabase, Redis)
├── models/       # Domain models and Pydantic schemas
├── utils/        # Shared utility functions and helpers
└── ...
```

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **AI/LLM Orchestration**: [LangChain](https://www.langchain.com/)
- **Database**: [Supabase](https://supabase.com/) / PostgreSQL
- **Caching & Queues**: [Redis](https://redis.io/)
- **Validation**: [Pydantic](https://docs.pydantic.dev/)

## Getting Started

Follow these steps to get your AI backend up and running.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/KJ-AIML/fastapi-agentic-starter.git
    cd fastapi-agentic-starter
    ```

2.  **Configure Environment**
    Copy the example environment file and configure your secrets.
    ```bash
    cp .env.example .env
    ```

3.  **Install Dependencies**
    Using `uv` (recommended) or `pip`:
    ```bash
    uv sync
    ```

4.  **Run the Application**
    Start the development server with hot-reloading.
    ```bash
    uv run -m src.api.main
    ```
    
    Access the API documentation at `http://localhost:3000/docs`.

---
*Built for the next generation of AI applications.*
