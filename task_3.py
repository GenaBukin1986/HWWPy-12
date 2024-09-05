class Book:
    _id_counter = 1

    def __new__(cls, title, author):
        instance = super().__new__(cls)
        instance.id = cls._id_counter
        cls._id_counter += 1
        return instance

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'Номер книги: {self.id}\nАвтор: {self.author}\nНазвание: {self.title}'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}'"


if __name__ == "__main__":
    b_1 = Book("Green Book", "Пушкин")
    b_2 = Book("Book", "Гоголь")
    b_3 = Book("Эхо", "Лермонтов")
    b_4 = Book("Петушок", "Пушкин")
    print(b_4)
    print(b_2)
