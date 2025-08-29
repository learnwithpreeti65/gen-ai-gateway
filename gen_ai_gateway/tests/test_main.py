"""Tests for the main FastAPI application."""

import pytest
from fastapi.testclient import TestClient


def test_health_check(client: TestClient):
    """Test the health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["message"] == "Gen AI Gateway is running"
    assert data["version"] == "1.0.0"


def test_get_presentations(client: TestClient):
    """Test getting all presentations."""
    response = client.get("/presentations")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 3  # We have 3 mock presentations


def test_get_presentation_by_id(client: TestClient):
    """Test getting a specific presentation by ID."""
    response = client.get("/presentations/ppt_001")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "ppt_001"
    assert data["title"] == "AI in Healthcare"


def test_get_nonexistent_presentation(client: TestClient):
    """Test getting a presentation that doesn't exist."""
    response = client.get("/presentations/nonexistent")
    assert response.status_code == 404


def test_create_presentation(client: TestClient):
    """Test creating a new presentation."""
    payload = {
        "title": "Test Presentation",
        "author": "Test Author",
        "template_id": "template_001"
    }
    response = client.post("/presentations", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Presentation"
    assert data["author"] == "Test Author"
    assert data["status"] == "draft"


def test_generate_content(client: TestClient):
    """Test generating AI content."""
    payload = {
        "topic": "Machine Learning",
        "slide_type": "content"
    }
    response = client.post("/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["topic"] == "Machine Learning"
    assert data["slide_type"] == "content"
    assert "title" in data
    assert "content" in data


def test_get_templates(client: TestClient):
    """Test getting all templates."""
    response = client.get("/templates")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 3  # We have 3 mock templates


def test_get_stats(client: TestClient):
    """Test getting presentation statistics."""
    response = client.get("/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_presentations" in data
    assert "completed_presentations" in data
    assert "total_slides" in data
    assert "available_templates" in data
