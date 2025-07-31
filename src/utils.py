from src.product import Product
from src.category import Category
import json


def get_class_from_json(file_path: str) -> dict:
    """функция подгрузки классов категорий и продуктов из json файла"""
    category_list = []
    product_list = []
    result = {}
    with open(file_path, encoding="utf-8") as json_file:
        data = json.load(json_file)
        for categoryes in data:
            category = Category(
                categoryes["name"], categoryes["description"], categoryes["products"]
            )
            category_list.append(category)
            for products in categoryes["products"]:
                product = Product(
                    products["name"],
                    products["description"],
                    products["price"],
                    products["quantity"],
                )
                product_list.append(product)
    result["category"] = category_list
    result["products"] = product_list
    return result
