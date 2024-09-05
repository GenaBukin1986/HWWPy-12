class Person:
    def __init__(self, name: str, age: int, email: str):
        self.__setattr__('name', name)
        self.__setattr__('age', age)
        self.__setattr__('email', email)

    def __setattr__(self, key, value):
        result = None
        if key == 'name':
            if not value.istitle() or not value.isalpha():
                raise AttributeError(f"Атрибут {key} должне начинаться с заглавной буквы и состоять только из букв")
            result = object.__setattr__(self,key, value)
        if key == 'age':
            if not isinstance(value, int):
                raise AttributeError(f"Атрибут {key} должен быть целым числом")
            elif value > 120 or value < 0:
                raise AttributeError(f"Атрибут {key} должен быть в диапазоне от 0 до 120")
            result = object.__setattr__(self,key, value)
        if key == 'email':
            if '@' not in value:
                raise AttributeError(f"Атрибут {key}, должен содержать '@'")
            result = object.__setattr__(self,key, value)
        return result

    def __repr__(self):
        return f"Person('{self.name}', {self.age}, '{self.email}')"


    def __str__(self):
        return f'Гражданин: {self.name}\nВозраст: {self.age}\nЭлектронная почта: {self.email}'

if __name__ == "__main__":
    p_1 = Person("Василий", 45, 'dog@mail.ru')
    print(p_1)
    print(repr(p_1))
    p_2 = Person("Василий", 120, 'dog@mail.ru')
    print(p_2)
