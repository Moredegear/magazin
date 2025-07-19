import pytest
from src.product import Product
from src.product import Category
from src.product import get_class_from_json


@pytest.fixture
def product_banan():
    return Product('Banan', "вкусный и полезный овощь", 50, 140)


def test_init(product_banan):
    assert product_banan.name == 'Banan'
    assert product_banan.description == 'вкусный и полезный овощь'
    assert product_banan.price == 50
    assert product_banan.quantity == 140


@pytest.fixture
def category_fruits():
    return Category("fruits", "вкусные и полезные фрукты", ["banan", "apple", "watermelon"])


def test_category_init(category_fruits):
    assert category_fruits.name == 'fruits'
    assert category_fruits.description == 'вкусные и полезные фрукты'
    assert category_fruits.products == ['banan', 'apple', 'watermelon']
    assert category_fruits.product_count == 3
    assert category_fruits.category_count == 1


def test_get_class_from_json():
    category_product_list = get_class_from_json("../data/products.json")
    category_phone = category_product_list[0][0]
    category_tv = category_product_list[0][1]
    product_1 = category_product_list[1][0]
    assert category_phone.name == "Смартфоны"
    assert category_phone.description == ("Смартфоны, как средство не только коммуникации,"
                                          " но и получение дополнительных функций для удобства жизни")
    assert category_phone.product_count == 3
    assert category_phone.category_count == 1
    assert category_tv.name == "Телевизоры"
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
