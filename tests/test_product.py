import pytest
from src.product import Product


@pytest.fixture
def product_banan():
    return Product('Banan', "вкусный и полезный овощь", 50, 140)


def test_init(product_banan):
    assert product_banan.name == 'Banan'
    assert product_banan.description == 'вкусный и полезный овощь'
    assert product_banan.get_price == 50
    assert product_banan.quantity == 140
