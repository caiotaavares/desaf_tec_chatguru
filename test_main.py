import socket
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_health():
    # Como as variáveis globais são lidas na importação/inicialização, 
    # podemos testar a rota diretamente chamando o cliente.
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_get_version(monkeypatch):
    # Define valores simulados para o teste usando monkeypatch
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
    # Testa fallback para socket.gethostname() quando a variável HOSTNAME não estiver definida
    monkeypatch.delenv("HOSTNAME", raising=False)
    
    response = client.get("/info")
    assert response.status_code == 200
    
    data = response.json()
    assert "hostname" in data
    assert data["hostname"] == socket.gethostname()