import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_product(client):
    response = client.post("/products", json={"name": "Tablet", "price": 300})
    assert response.status_code == 201
    assert response.json["name"] == "Tablet"

def test_get_product_not_found(client):
    response = client.get("/products/999")
    assert response.status_code == 404
