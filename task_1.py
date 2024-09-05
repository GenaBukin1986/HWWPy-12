import csv


class Validate:
    def __init__(self, param1, param2) -> None:
        self.param1 = param1
        self.param2 = param2

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.param1(value) and not self.param2(value):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалить')

    def _validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Должна передавать строка")
        if value.isdigit() or value.istitle():
            raise AttributeError("ФИО должно состоять только из букв и начинаться с заглавной буквы")


class Student:
    # name = Validate(str.istitle, str.isdigit)  # Имя
    # middle_name = Validate(str.istitle, str.isdigit)  # Отчество
    # surname = Validate(str.istitle, str.isdigit)  # Фамилия

    def __init__(self, name: str, middle_name: str, surname: str, subjects_file: str = 'subjects.csv') -> None:
        self.__setattr__('name', name)
        self.__setattr__('middle_name', middle_name)
        self.__setattr__('surname', surname)
        # self.middle_name = middle_name
        # self.surname = surname
        self.subjects = {}
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        if name == 'name' or name == 'middle_name' or name == 'surname':
            if value.isdigit() or not value.istitle():
                raise AttributeError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        return object.__setattr__(self, name, value)

    def add_grade(self, subject, grade):
        """ Добавляет оценку по заданному предмету.
        Убеждается, что оценка является целым числом от 2 до 5"""
        if isinstance(grade, int) and (2 <= grade <= 5):
            self.__getattr__(subject)['grades'].append(grade)
        else:
            raise AttributeError("Оценка должна быть целым числом от 2 до 5")

    def add_test_score(self, subject, test_score):
        """ Добавляет результат теста по заданному предмету.
        Убеждается, что результат теста является целым числом от 0 до 100"""
        if isinstance(test_score, int) and (0 <= test_score <= 100):
            self.__getattr__(subject)['test_scores'].append(test_score)
        else:
            raise AttributeError("Результат теста должна быть целым числом от 0 до 100")

    def get_average_test_score(self, subject):
        """ Возвращает средний балл по тестам для заданного предмета."""
        if self.__getattr__(subject):
            score = self.subjects[subject]['test_scores']
            score_one = sum(score) / len(score) if score else 0
            return f'{subject}: {score_one} cредний бал по тестам'

    def get_average_grade(self):
        """Возвращает средний балл по всем предметам."""
        all_scores = [i['grades'] for i in self.subjects.values()]
        scores = []
        for i in all_scores:
            for j in i:
                scores.append(j)
        string_scores = sum(scores) / len(scores) if scores else 0
        return f"Средний балл по всем предметам: {string_scores}"

    def __str__(self):
        string_subject = ', '.join([k for k in self.subjects])
        return f"Студент: {self.name}, {self.middle_name}, {self.surname}\n" \
               f"Предметы: {string_subject}"

    def __repr__(self):
        return f"Student('{self.name}', '{self.middle_name}', '{self.surname}')"

    def load_subjects(self, file):
        """Загружает предметы из файла CSV.
        Использует модуль csv для чтения данных
        из файла и добавляет предметы в атрибут"""
        try:
            with open(file, 'r', newline='', encoding='utf-8') as f:
                text = csv.reader(f)
                for i in text:
                    for j in i:
                        self.subjects[j] = {'grades': [], 'test_scores': []}
        except:
            raise FileNotFoundError(f"Файла с таким названием {file} нет в данной директории")


    def __getattr__(self, item):
        if item not in self.subjects:
            raise ValueError(f"Предмет {item} не найден")
        return self.subjects[item]

if __name__ == "__main__":
    std = Student("Gетр", "Gетрович", "Gетров")
    print(std)
    std.add_grade("История", 4)
    std.add_grade("История", 5)
    std.add_test_score("История", 49)
    print(std.get_average_test_score("История"))
    print(std.get_average_test_score("Математика"))
    print(std.__getattr__("История"))
    print(std.get_average_grade())

