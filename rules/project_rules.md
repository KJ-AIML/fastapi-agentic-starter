#Repository Guidelines

## Project Structure & Module Organization
- The project should follow the [FastAPI Hexagonal Agentic Structure] That I created and modify
- The project should have a `src` directory at the root level
- The `src` directory should have the following subdirectories:
  - `api`: Contains the FastAPI application code
    - `endpoints`: Contains the API endpoint definitions (grouped by version)
      - Each version (v1, v2, etc.) has its own `dependencies.py` for version-specific DI
    - `router`: Contains router aggregation and version prefix management
  - `execution`: Contains the business logic and execution code (equivalent to services layer)
    - `usecases`: Contains the usecases code for executing actions 
    - `actions`: Contains the actions code implementations
  - `agents`: Contains AI agent management
    - `agent_manager`: Contains agent definitions
    - `prompts`: Contains agent prompts
    - `tools`: Contains agent tools
    - `workflows`: Contains agent workflows
  - `providers`: Contains infrastructure providers
    - `ai`: Contains AI model providers
    - `cache`: Contains cache providers
    - `vectordb`: Contains vector database providers
  - `database`: Contains database layer
    - `migrations`: Contains database migrations
    - `repositories`: Contains data repositories
  - `config`: Contains configuration files
  - `utils`: Contains utility functions and helpers

## Build, Test, and Development Commands
- `uv run -m src.api.main` to run the FastAPI application
- `uv run -m tests.test_main` to run the tests
- `uv run -m src.utils.helpers` to run the utility functions
- `uv add xxx` to add a new module or package to the project
- `uv sync` to sync the project with the `uv.lock` file

## Coding Style & Naming Conventions
- Language: Python
- Code Style: [PEP 8]
- Naming Conventions:
  - Variables: `snake_case`
  - Functions: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_CASE`
