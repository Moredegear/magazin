
class Category:
    """класс для представления категории"""
    category_count = 0
    name: str
    description: str
    products: list
    category_count: int
    product_count: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.product_count = len(products)

        Category.category_count += 1
