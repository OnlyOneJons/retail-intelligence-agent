import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "OPERATIONAL"

def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "HEALTHY"
    assert "services" in data

def test_metrics_endpoint():
    response = client.get("/api/v1/metrics")
    assert response.status_code == 200

def test_chat_endpoint():
    payload = {
        "message": "Inspect store #201 fleet status",
        "thread_id": "test-session-123",
        "domain": "edgepulse"
    }
    response = client.post("/api/v1/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "response" in data
