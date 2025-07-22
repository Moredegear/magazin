

class Product:
    """класс для пркдставления продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product, list_products):
        """обновляет список продуктов(цену,количество,ассортимент)"""
        result = None
        if list_products != []:
            print('cписок не пустой')
            for product in list_products:
                if product.name == dict_product['name']:
                    product.quantity += dict_product['quantity']
                    if product.get_price >= dict_product['price']:
                        return []
                    else:
                        product.get_price(dict_product['price'])
                        return []

        else:
            cls.name = dict_product['name']
            cls.description = dict_product['description']
            cls.price = dict_product['price']
            cls.quantity = dict_product['quantity']
            result = cls(dict_product['name'], dict_product['description'], dict_product['price'],
                         dict_product['quantity'])
        return result

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def get_price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if price < self.__price:
                answer = input("Вы уверены что хотите понизить цену товара(Да:'Y' Нет:'N')")
                if answer.lower() == 'y':
                    self.__price = price
                else:
                    print("Изменение цены отменено")
            else:
                self.__price = price
                print("цена изменена")
