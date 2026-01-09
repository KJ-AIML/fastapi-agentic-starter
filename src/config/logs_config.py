import logging
import logging.handlers
import sys
from contextvars import ContextVar
from typing import Any, Dict, Optional

from src.config.settings import BASE_DIR, settings

request_id_ctx: ContextVar[str] = ContextVar("request_id", default="system")


# Custom formatter with UTF-8 support and better formatting
class UTF8Formatter(logging.Formatter):
    """Custom formatter that ensures UTF-8 encoding for log messages and includes request_id"""

    def __init__(self, fmt: Optional[str] = None, datefmt: Optional[str] = None):
        if fmt is None:
            # Added [id=%(request_id)s] to the format
            fmt = "%(asctime)s - %(name)s - %(levelname)s - [id=%(request_id)s] - %(funcName)s:%(lineno)d - %(message)s"
        if datefmt is None:
            datefmt = "%Y-%m-%d %H:%M:%S"
        super().__init__(fmt, datefmt)

    def format(self, record: logging.LogRecord) -> str:
        # Ensure the message is properly encoded as UTF-8
        try:
            return super().format(record)
        except UnicodeEncodeError:
            # Fallback for encoding issues
            record.msg = (
                str(record.msg).encode("utf-8", errors="replace").decode("utf-8")
            )
            return super().format(record)


class RequestIDFilter(logging.Filter):
    """Filter that injects request_id from contextvars into the log record"""

    def filter(self, record):
        record.request_id = request_id_ctx.get()
        return True


def setup_logging(
    log_level: Optional[str] = None,
    save_to_file: Optional[bool] = None,
    log_file: Optional[str] = None,
    max_file_size: Optional[int] = None,
    backup_count: Optional[int] = None,
) -> None:
    """
    Setup comprehensive logging configuration with UTF-8 support and rotation

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        save_to_file: Whether to save logs to file
        log_file: Path to log file (if save_to_file is True)
        max_file_size: Maximum file size in bytes before rotation (default: 10MB)
        backup_count: Number of backup files to keep (default: 5)
    """
    # Get settings from environment or use defaults
    if log_level is None:
        log_level = getattr(settings, "LOG_LEVEL", "INFO")

    if save_to_file is None:
        save_to_file = getattr(settings, "LOG_SAVE_TO_FILE", False)

    if log_file is None:
        log_file = getattr(settings, "LOG_FILE", "src/logs/app.log")

    if max_file_size is None:
        max_file_size = getattr(settings, "LOG_MAX_FILE_SIZE", 10 * 1024 * 1024)  # 10MB

    if backup_count is None:
        backup_count = getattr(settings, "LOG_BACKUP_COUNT", 5)

    # Convert log level string to logging constant
    level = getattr(logging, log_level.upper(), logging.INFO)

    # Create logs directory if it doesn't exist
    if save_to_file:
        # Convert to absolute path relative to project root
        log_path = BASE_DIR / log_file
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_file = str(log_path)  # Update log_file to absolute path

    # Configure logging
    handlers = []

    # Console handler with UTF-8 encoding
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(UTF8Formatter())
    handlers.append(console_handler)

    # File handler with rotation and UTF-8 encoding (if enabled)
    if save_to_file:
        # Use RotatingFileHandler for log rotation
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=max_file_size,
            backupCount=backup_count,
            encoding="utf-8",  # Explicitly set UTF-8 encoding
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(UTF8Formatter())
        handlers.append(file_handler)

    # Configure root logger with UTF-8 support
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Clear existing handlers
    root_logger.handlers = []

    id_filter = RequestIDFilter()

    for handler in handlers:
        handler.addFilter(id_filter)
        root_logger.addHandler(handler)

    # Set specific log levels for noisy libraries
    noisy_libs = {
        "urllib3": logging.WARNING,
        "httpx": logging.WARNING,
        "httpcore": logging.WARNING,
        "asyncio": logging.WARNING,
        "langchain": logging.INFO,
        "openai": logging.INFO,
    }

    for lib_name, lib_level in noisy_libs.items():
        logging.getLogger(lib_name).setLevel(lib_level)

    logger = logging.getLogger(__name__)
    logger.info(f"Logging configured. Level: {log_level}, Save to file: {save_to_file}")
    if save_to_file:
        logger.info(
            f"Log file: {log_file}, Max size: {max_file_size / 1024 / 1024:.1f}MB, Backups: {backup_count}"
        )


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger with the specified name

    Args:
        name: Logger name (usually __name__)

    Returns:
        Configured logger instance with UTF-8 support
    """
    return logging.getLogger(name)


def configure_third_party_loggers(config: Optional[Dict[str, Any]] = None) -> None:
    """
    Configure third-party library loggers with custom settings

    Args:
        config: Dictionary of logger names and their desired levels
    """
    if config is None:
        config = {
            "urllib3": logging.WARNING,
            "httpx": logging.WARNING,
            "httpcore": logging.WARNING,
            "asyncio": logging.WARNING,
            "langchain": logging.INFO,
            "openai": logging.INFO,
        }

    for logger_name, level in config.items():
        logging.getLogger(logger_name).setLevel(level)


def unify_system_loggers() -> None:
    """
    Force all system loggers (Uvicorn, FastAPI, etc.) to use our custom formatter and filter.
    This ensures that even startup and internal logs follow the [id=...] format.
    """
    loggers = (
        logging.getLogger("uvicorn"),
        logging.getLogger("uvicorn.error"),
        logging.getLogger("uvicorn.access"),
        logging.getLogger("fastapi"),
    )

    id_filter = RequestIDFilter()
    formatter = UTF8Formatter()

    for logger in loggers:
        # Clear existing handlers to prevent duplicate logs
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

        # Add a new stream handler with our config
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        handler.addFilter(id_filter)
        logger.addHandler(handler)
        logger.propagate = False  # Prevent double logging through root


# Auto-setup logging on import if enabled
auto_setup = getattr(settings, "LOG_AUTO_SETUP", True)
if auto_setup:
    setup_logging()
    unify_system_loggers()
