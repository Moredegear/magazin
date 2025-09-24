from src.utils import get_class_from_json
from src.config import BASE_DIR


def test_get_class_from_json():
    products_path = BASE_DIR.joinpath('data', 'products.json')
    category_product_dict = get_class_from_json(products_path)
    category_phone = category_product_dict["category"][0]
    category_tv = category_product_dict["category"][1]
    product_1 = category_product_dict["products"][0]
    assert category_phone.name == "Смартфоны"
    assert category_phone.description == ("Смартфоны, как средство не только коммуникации,"
                                          " но и получение дополнительных функций для удобства жизни")
    assert category_phone.product_count == 18
    assert category_phone.category_count == 11
    assert category_tv.name == "Телевизоры"
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
