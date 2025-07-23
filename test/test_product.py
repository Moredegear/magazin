import pytest
from src.product import Product


@pytest.fixture
def product_banan():
    return Product('Banan', "вкусный и полезный овощь", 50, 140)
@pytest.fixture
def product_banan2():
    return Product('Banan', "вкусный и полезный овощь", 50, 140)

def test_init(product_banan, product_banan2,capsys):
    assert product_banan.name == 'Banan'
    assert product_banan.description == 'вкусный и полезный овощь'
    assert product_banan.get_price == 50
    assert product_banan.quantity == 140
    assert product_banan2.name == 'Banan'
    assert (product_banan2 + product_banan) == 14000
    print(product_banan2)
    captured = capsys.readouterr()
    assert captured.out == 'Banan, 50 руб. Остаток: 140 шт.\n'
