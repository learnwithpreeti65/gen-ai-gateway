"""Test configuration and fixtures."""

import pytest
from fastapi.testclient import TestClient
from gen_ai_gateway.apps.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)
