from src.utils import get_class_from_json

def test_get_class_from_json():
    category_product_dict = get_class_from_json("../data/products.json")
    category_phone = category_product_dict["category"][0]
    category_tv = category_product_dict["category"][1]
    product_1 = category_product_dict["products"][0]
    assert category_phone.name == "Смартфоны"
    assert category_phone.description == ("Смартфоны, как средство не только коммуникации,"
                                          " но и получение дополнительных функций для удобства жизни")
    assert category_phone.product_count == 4
    assert category_phone.category_count == 2
    assert category_tv.name == "Телевизоры"
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"