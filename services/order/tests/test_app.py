import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_and_get_orders(client):
    response = client.post("/orders", json={
        "user_id": 1,
        "products": [1, 2],
        "total": 1500
    })
    assert response.status_code == 201
    assert response.json["user_id"] == 1

    response = client.get("/orders")
    assert response.status_code == 200
    assert len(response.json) >= 1
