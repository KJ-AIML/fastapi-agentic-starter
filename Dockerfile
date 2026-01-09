# Use a slim Python base image
FROM python:3.11-slim-bookworm AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies into a virtual environment
RUN uv sync --frozen --no-dev --no-install-project

# Final stage
FROM python:3.11-slim-bookworm

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /app/.venv /app/.venv

# Set environment path to use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Copy source code
COPY src ./src
COPY README.md .env.example ./

# Expose port
EXPOSE 3000

# Run the application
CMD ["python", "-m", "src.api.main"]
