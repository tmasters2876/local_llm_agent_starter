import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_normal_prompt():
    payload = {
        "prompt": "Tell me a fun fact about space",
        "temperature": 0.7,
        "num_predict": 100,
        "model": "mistral"
    }
    response = client.post("/api/ask", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert isinstance(data["result"], str)
    assert len(data["result"]) > 10

def test_empty_prompt():
    payload = {
        "prompt": "",
        "temperature": 0.7,
        "num_predict": 100,
        "model": "mistral"
    }
    response = client.post("/api/ask", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert isinstance(data["result"], str)
    assert len(data["result"]) > 0  # Should fallback

def test_bad_model_name():
    payload = {
        "prompt": "What is AI?",
        "temperature": 0.7,
        "num_predict": 100,
        "model": "nonexistent-model"
    }
    response = client.post("/api/ask", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert isinstance(data["result"], str)
