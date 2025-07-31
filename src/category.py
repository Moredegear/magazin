from src.product import Product
from abc import ABC, abstractmethod


class BaseCategory(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Order(BaseCategory):
    def __init__(self, product: Product):
        self.product = product
        self.quantity = product.quantity
        self.price = product.get_price * product.quantity

    def __str__(self):
        return f"Заказ на {self.quantity} {self.product.name} Общей стоимостью: {self.price}руб."


class Category(BaseCategory):
    """класс для представления категории"""

    category_count = 0
    product_count = 0
    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.all_products} шт."

    @property
    def all_products(self):
        result = 0
        for product in self.__products:
            result += product.quantity
        return result

    def add_product(self, product: Product):
        if issubclass(product.__class__, Product):
            dict_product = {}
            dict_product["name"] = product.name
            dict_product["description"] = product.description
            dict_product["price"] = product.get_price
            dict_product["quantity"] = product.quantity
            product = Product.new_product(dict_product, self.__products)
            if product == []:
                pass
            else:
                self.__products.append(product)

    @property
    def get_products(self):
        result = []
        for product in self.__products:
            product = f"{product.name}, {product.get_price}руб., Остаток: {product.quantity}шт."
            result.append(product)
        return result
