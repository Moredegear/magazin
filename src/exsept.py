class Product_Zero(Exception):

    def __init__(self, quantity):
        if quantity > 0:
            self.massage = quantity
        else:
            self.massage = "Количество товара не должно ровняться нулю"

    def __str__(self):
        return self.massage


class Order_Zero(Exception):
    def __init__(self, remainder, quantity):
        if remainder > 0:
            self.massage = remainder
        else:
            self.massage = f"Тавара нет в нужном колличестве,Осталось:{quantity}"

    def __str__(self):
        return self.massage
