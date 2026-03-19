from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_ready_check():
    # Note: This might fail if the DB isn't connected in the test env
    response = client.get("/ready")
    assert response.status_code == 200