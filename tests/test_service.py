from service import add_product, get_all_products
from unittest.mock import patch
import pytest

@pytest.fixture
def mock_db():
    """Fixture to mock the database for unit tests."""
    with patch('service.get_db') as mock:
        yield mock

def test_add_product(mock_db):
    mock_collection = mock_db.return_value['products']
    mock_collection.insert_one.return_value = None  
    product_data = {
        "name": "Test Product",
        "description": "A test product",
        "price": 500,
        "stock": 20
    }
    add_product(product_data)
    mock_collection.insert_one.assert_called_once_with(product_data)

def test_get_all_products(mock_db):
    """Test the get_all_products function."""
    mock_collection = mock_db.return_value['products']
    mock_collection.find.return_value = [
        {"name": "Camera", "description": "An HD Camera", "price": 1200, "stock": 10}
    ]

    products = get_all_products()
    assert len(products) == 1
    assert products[0].name == "Camera"
    assert products[0].description == "An HD Camera"
    assert products[0].price == 1200
    assert products[0].stock == 10

