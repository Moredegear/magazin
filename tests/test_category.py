import pytest
from src.category import Category
from src.utils import get_class_from_json


@pytest.fixture
def category_fruits():
    return Category("fruits", "вкусные и полезные фрукты", ["banan", "apple", "watermelon"])


def test_category_init(category_fruits):
    assert category_fruits.name == 'fruits'
    assert category_fruits.description == 'вкусные и полезные фрукты'
    assert category_fruits.product_count == 3
    assert category_fruits.category_count == 1


def test_category():
    category_product_dict = get_class_from_json("../data/products.json")
    product_sm = category_product_dict["products"][0]
    category_phone = Category("Смртфоны", "Полезная техника", [])
    category_phone.add_product(product_sm)
    assert category_phone.get_products == ['Samsung Galaxy C23 Ultra, 180000.0руб., Остаток: 5шт.']
    category_phone.add_product(product_sm)
    new_price = 2000000.0
    product_sm.get_price(new_price)
    assert category_phone.get_products == ['Samsung Galaxy C23 Ultra, 200000.0руб., Остаток: 10шт.']
