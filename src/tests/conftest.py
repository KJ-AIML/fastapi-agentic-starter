from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient

from src.api.main import app
from src.config.settings import settings
from src.database.connection import get_db


@pytest.fixture
def client():
    headers = {"X-API-KEY": settings.X_API_KEY} if settings.X_API_KEY else {}

    async def override_get_db():
        mock_session = AsyncMock()
        yield mock_session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app, headers=headers) as c:
        yield c

    app.dependency_overrides.clear()
