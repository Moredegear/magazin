import json


class Product:
    """класс для пркдставления продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """класс для представления категории"""
    name: str
    description: str
    products: list
    category_count: int
    product_count: int

    def __init__(self, name, description, products):
        self.category_count = 0
        self.name = name
        self.description = description
        self.products = products
        self.product_count = len(products)
        self.category_count += 1


def get_class_from_json(file_path: str) -> tuple[list[Category], list[Product]]:
    """функция подгрузки классов категорий и продуктов из json файла"""
    category_list = []
    product_list = []
    with open(file_path, encoding="utf-8") as json_file:
        data = json.load(json_file)
        for categoryes in data:
            category = Category(categoryes["name"], categoryes["description"], categoryes["products"])
            category_list.append(category)
            for products in category.products:
                product = Product(products["name"], products["description"], products["price"], products["quantity"])
                product_list.append(product)
    return category_list, product_list
