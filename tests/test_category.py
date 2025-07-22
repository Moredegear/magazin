import pytest
from src.category import Category

@pytest.fixture
def category_fruits():
    return Category("fruits", "вкусные и полезные фрукты", ["banan", "apple", "watermelon"])


def test_category_init(category_fruits):
    assert category_fruits.name == 'fruits'
    assert category_fruits.description == 'вкусные и полезные фрукты'
    assert category_fruits.products == ['banan', 'apple', 'watermelon']
    assert category_fruits.product_count == 3
    assert category_fruits.category_count == 1
