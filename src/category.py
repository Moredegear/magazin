from src.product import Product


class Category:
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

    def add_product(self, product: Product):
        dict_product = {}
        dict_product['name'] = product.name
        dict_product['description'] = product.description
        dict_product['price'] = product.get_price
        dict_product['quantity'] = product.quantity
        product = Product.new_product(dict_product, self.__products)
        if product == []:
            print('количество тавара обнавленно')
        else:
            self.__products.append(product)

    @property
    def get_products(self):
        result = []
        for product in self.__products:
            product = f'{product.name}, {product.get_price}руб., Остаток: {product.quantity}шт.'
            result.append(product)
        return result
