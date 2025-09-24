from src.product import Product
from abc import ABC, abstractmethod
from src.exsept import Order_Zero


class BaseCategory(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Order(BaseCategory):
    order_count = 0

    def __init__(self, product: Product, quantity):
        self.quantity_update(product, quantity)
        self.product = product
        self.quantity = quantity
        self.__price = product.get_price * quantity
        Order.order_count += 1

    def __str__(self):
        return f"Заказ на {self.quantity} {self.product.name} Общей стоимостью: {self.get_price}руб."

    @property
    def get_price(self):
        return self.__price

    def quantity_update(self, product: Product, quantity):
        try:
            product.quantity_update(quantity)
        except Order_Zero as e:
            print(e)
        else:
            product.quantity_update(quantity)
        finally:
            print("Обработка заказа завершина")


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

    def average_price_tag(self):
        try:
            all_price = 0
            for product in self.__products:
                all_price += product.get_price
            apt = all_price / len(self.__products)
        except ZeroDivisionError:
            result = 0
        else:
            result = apt
        finally:
            return result


product_one = Product("name", "desc", "20", "50")
order_zero = Order(product_one, 60)
