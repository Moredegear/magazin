import pytest
from src.product import Product
from src.product import Smartphone
from src.product import LawnGrass


@pytest.fixture
def product_banan():
    return Product('Banan', "вкусный и полезный овощь", 50, 140)


@pytest.fixture
def product_banan2():
    return Product('Banan', "вкусный и полезный овощь", 50, 140)


@pytest.fixture
def product_smartphone():
    return Smartphone("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                      5, 3360, "Galaxy", 256, "Серый")


@pytest.fixture
def product_lawngrass():
    return LawnGrass("LawnGrass", "красивый и легкий в уходе", 3000, 6,
                     "Italy", 30, "Green")


@pytest.fixture
def product_lawngrass_2():
    return LawnGrass("LawnGrass", "красивый и легкий в уходе", 4000, 6,
                     "Italy", 20, "Green")


def test_init(product_banan, product_banan2, product_lawngrass, product_smartphone, product_lawngrass_2, capsys):
    assert product_banan.name == 'Banan'
    assert product_banan.description == 'вкусный и полезный овощь'
    assert product_banan.get_price == 50
    assert product_banan.quantity == 140
    assert product_banan2.name == 'Banan'
    assert (product_banan2 + product_banan) == 14000
    print(product_banan2)
    captured = capsys.readouterr()
    assert captured.out == 'Banan, 50 руб. Остаток: 140 шт.\n'
    assert product_lawngrass.name == 'LawnGrass'
    assert product_lawngrass.country == 'Italy'
    assert product_smartphone.name == 'Samsung Galaxy C23 Ultra'
    assert product_smartphone.model == "Galaxy"
    with pytest.raises(TypeError) as exc_info:
        product_smartphone + product_lawngrass
    assert str(exc_info.value) == 'Нельзя складывать разные товары'
    assert (product_lawngrass_2 + product_lawngrass) == 42000
