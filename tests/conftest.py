from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from defaultpython.api import app
from defaultpython.config import Settings, get_settings


@pytest.fixture
def settings() -> Settings:
    return get_settings()


@pytest.fixture
def client() -> Generator[TestClient]:
    with TestClient(app) as c:
        yield c
