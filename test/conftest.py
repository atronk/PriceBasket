import pytest

from main import load_products_prices


def pytest_configure():
    pytest.prices = load_products_prices("products.json")
