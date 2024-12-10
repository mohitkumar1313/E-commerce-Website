# tests/test_api.py
import pytest
from app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to provide a test client."""
    with app.test_client() as client:
        yield client

def test_create_product(client):
    """Test POST /api/product endpoint."""
    response = client.post('/api/add_product', json={
        "name": "Camera",
        "description": "An HD Camera",
        "price": 1200,
        "stock": 10
    })
    assert response.status_code == 201
    assert b"Product created successfully" in response.data

def test_get_all_products(client):
    """Test GET /api/products endpoint."""
    response = client.get('/api/products')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Ensure it's a list of products

def test_get_product_by_name(client):
    """Test GET /api/product/<product_name> endpoint."""
    response = client.get('/api/product/Camera')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # It should return a list of products

def test_get_user_by_username(client):
    """Test GET /api/user/<username> endpoint."""
    response = client.get('/api/user/john_doe')
    assert response.status_code == 200
    assert response.json['username'] == 'john_doe'

def test_delete_product(client):
    """Test DELETE /api/product/<product_name> endpoint."""
    response = client.delete('/api/product/Camera')
    assert response.status_code == 200
    assert b"Product deleted successfully" in response.data
