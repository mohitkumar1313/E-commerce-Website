import pytest
from app import app 
from model import *
from unittest.mock import patch

@pytest.fixture
def client():
    """Fixture to provide a test client."""
    with app.test_client() as client:
        yield client

def test_add_product(client):
    response = client.post('/api/add_product', json={
        "name": "Camera",
        "description": "An HD Camera",
        "price": 1200,
        "stock": 10
    })
    assert response.status_code == 200
    assert b"Product created successfully" in response.data

def test_get_all_products(client):
    response = client.get('/api/products')
    assert response.status_code == 200
    assert isinstance(response.json, list) 

def test_get_product_by_name(client):
    response = client.get('/api/product/Camera')
    assert response.status_code == 200
    assert isinstance(response.json, list)  

def test_update_product_stock(client):
    response = client.put('/api/product/Camera/stock')
    assert response.status_code == 200
    assert b"Product stock updated successfully" in response.data

def test_delete_product(client):
    response = client.delete('/api/product/Camera')
    assert response.status_code == 200
    assert b"Product deleted successfully" in response.data

def test_add_user(client):
    response = client.post('/api/add_user', json={
        "name": "John",
        "email": "john@example.com", 
        "password": "password123"
    })
    assert response.status_code == 200
    assert b"User created successfully" in response.data


def test_list_all_users(client):
    mock_users = [
        User("john_doe", "john@example.com", "password123"),
        User("jane_doe", "jane@example.com", "password456"),
    ]

    with patch('api.get_all_users', return_value=mock_users):
        response = client.get('/api/users')

    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) == 2
    assert response.json[0]["username"] == "john_doe"
    assert response.json[0]["email"] == "john@example.com"
    assert response.json[1]["username"] == "jane_doe"
    assert response.json[1]["email"] == "jane@example.com"


def test_get_user_by_username(client):
    response = client.get('/api/user/john_doe')
    assert response.status_code == 200
    assert response.json['username'] == 'john_doe'


