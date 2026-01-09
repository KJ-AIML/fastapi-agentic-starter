import logging
from pathlib import Path
from typing import List

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    # OpenAI settings
    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL_BASIC: str | None = None
    OPENAI_MODEL_REASONING: str | None = None

    # Google settings
    GOOGLE_API_KEY: str | None = None
    GOOGLE_MODEL_BASIC: str | None = None
    GOOGLE_MODEL_REASONING: str | None = None

    # Environment settings
    DEBUG: bool = False
    SECRET_KEY: str = "your-default-secret-key"

    # Database settings
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "db"
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "postgres"

    # API settings
    API_PREFIX: str = "/api"

    # Redis settings
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str | None = None
    REDIS_DB: int = 0

    # Cache settings
    CACHE_TTL: int = 900

    # Logging settings
    LOG_LEVEL: str = "info"
    LOG_SAVE_TO_FILE: bool = False
    LOG_FILE: str = "src/logs/app.log"
    LOG_AUTO_SETUP: bool = True

    # Server Configuration
    SERVER_PORT: int = 3000
    SERVER_HOST: str = "0.0.0.0"

    # Allowed hosts
    ALLOWED_HOSTS: List[str] = ["*"]

    # Security settings
    X_API_KEY: str | None = "your-api-key-here"

    @property
    def is_production(self) -> bool:
        return not self.DEBUG

    class Config:
        env_file = BASE_DIR / ".env"
        case_sensitive = True


settings = Settings()

# Post-initialization validation
if not settings.DEBUG and not settings.OPENAI_API_KEY:
    logger = logging.getLogger(__name__)
    logger.warning("OPENAI_API_KEY is not set in production mode!")
