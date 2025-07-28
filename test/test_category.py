import pytest
from src.category import Category
from src.utils import get_class_from_json
from src.config import BASE_DIR


@pytest.fixture
def category_fruits():
    return Category("fruits", "вкусные и полезные фрукты", ["banan", "apple", "watermelon"])


def test_category_init(category_fruits):
    assert category_fruits.name == 'fruits'
    assert category_fruits.description == 'вкусные и полезные фрукты'
    assert category_fruits.product_count == 3
    assert category_fruits.category_count == 1


def test_category(capsys):
    products_path = BASE_DIR.joinpath('data', 'products.json')
    category_product_dict = get_class_from_json(products_path)
    product_sm = category_product_dict["products"][0]
    category_phone = Category("Смртфоны", "Полезная техника", [])
    category_phone.add_product(product_sm)
    assert category_phone.get_products == ['Samsung Galaxy C23 Ultra, 180000.0руб., Остаток: 5шт.']
    product_sm.get_price = 2000000.0
    category_phone.add_product(product_sm)
    assert category_phone.get_products == ['Samsung Galaxy C23 Ultra, 2000000.0руб., Остаток: 10шт.']
    category_tv = category_product_dict["category"][1]
    category_phone.add_product(category_tv)
    assert category_phone.get_products == ['Samsung Galaxy C23 Ultra, 2000000.0руб., Остаток: 10шт.']
    product_app = category_product_dict["products"][1]
    category_phone.add_product(product_app)
    print(category_phone)
    captured = capsys.readouterr()
    assert captured.out == 'Смртфоны, количество продуктов: 18 шт.\n'
