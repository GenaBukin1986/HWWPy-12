class Product:
    def __init__(self, name: str, price: int | float, quantity: int):
        self.__setattr__('name', name)
        self.__setattr__('price', price)
        self.__setattr__('quantity', quantity)


    def __setattr__(self, key, value):
        result = None
        if key == 'price':
            if not isinstance(value, int | float):
                raise AttributeError(f'Атрибут {key} должен быть целым числом, либо числом с плавающей точкой')
            elif value <= 0:
                raise AttributeError(f'Атрибут {key} должен быть больше нуля')
            result = object.__setattr__(self, key, value)
        if key == 'quantity':
            if not isinstance(value, int):
                raise AttributeError(f'Атрибут {key} должен быть целым числом')
            elif value <= 0:
                raise AttributeError(f'Атрибут {key} должен быть больше нуля')
            result = object.__setattr__(self, key, value)
        if key == 'name':
            result = object.__setattr__(self, key, value)
        return result

    def __str__(self):
        return f'Продукт: {self.name}\nЦена: {self.price}\nКоличество: {self.quantity}'

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"


if __name__ == '__main__':
    p1 = Product("Колбаса", 2, 0)
    p2 = Product("Pachka", 33, 3)
    print(p1)
