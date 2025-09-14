import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_and_get_cart(client):
    user_id = 1
    response = client.post(f"/cart/{user_id}", json={"product_id": 101})
    assert response.status_code == 201
    assert 101 in response.json["products"]

    response = client.get(f"/cart/{user_id}")
    assert response.status_code == 200
    assert 101 in response.json["products"]
