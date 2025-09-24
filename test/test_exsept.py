import pytest
from src.product import Product
from src.exsept import Product_Zero
from src.category import Category
from src.category import Order

category_zero = Category('name', 'desc', [])
product_one = Product("name", "desc", "20", "50")


def test_product_zero():
    with pytest.raises(Product_Zero):
        product_5 = Product("name", 'desc', 5, 0)
    assert category_zero.average_price_tag() == 0


def test_order_zero(capsys):
    order_zero = Order(product_one, 60)
    captured = capsys.readouterr()
    assert captured.out == 'Тавара нет в нужном колличестве,Осталось:60\nОбработка заказа завершина\n'
