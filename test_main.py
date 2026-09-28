import socket
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_get_version(monkeypatch):
    monkeypatch.setenv("VERSION", "2.0.0")
    monkeypatch.setenv("DB", "test_mysql")
    monkeypatch.setenv("HOSTNAME", "pod-test-123")
    
    response = client.get("/info")
    assert response.status_code == 200
    
    data = response.json()
    assert "version" in data
    assert "db" in data
    assert "hostname" in data
    assert data["version"] == "2.0.0"
    assert data["db"] == "test_mysql"
    assert data["hostname"] == "pod-test-123"

def test_get_version_default_hostname(monkeypatch):
    monkeypatch.delenv("HOSTNAME", raising=False)
    
    response = client.get("/info")
    assert response.status_code == 200
    
    data = response.json()
    assert "hostname" in data
    assert data["hostname"] == socket.gethostname()