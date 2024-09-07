
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={"name": "Test Product", "price": 10.99, "description": "Test description"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"

def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"
    