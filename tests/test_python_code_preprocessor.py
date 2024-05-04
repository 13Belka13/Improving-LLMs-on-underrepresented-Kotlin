# test_python_code_preprocessor.py
from src.code_preprocessor.python_code_preprocessor import PythonCodePreprocessor


def test_preprocess_code():
    test_code = '''
# Импорт модулей
import math
from collections import defaultdict

# Объявление константы
PI = 3.14159

# Объявление переменной
global_variable = 42

# Объявление функции высшего порядка
def higher_order_function(function):
    return function(10)

# Объявление лямбда-функции
lambda_func = lambda x: x * 2

# Объявление класса
class Person:
    # Объявление метода инициализации
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Объявление метода класса
    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет.")

    # Объявление статического метода
    @staticmethod
    def static_method():
        print("Это статический метод.")

# Объявление класса-наследника
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_student_id(self):
        print(f"Мой студенческий ID: {self.student_id}")

# Объявление функции
def main():
    # Использование переменных и констант
    print(f"Значение PI: {PI}")
    global_variable += 10
    print(f"Значение global_variable: {global_variable}")

    # Использование функций
    def local_function(x, y):
        return x + y
    result = local_function(5, 7)
    print(f"Результат local_function: {result}")

    # Использование лямбда-функции
    lambda_result = lambda_func(5)
    print(f"Результат лямбда-функции: {lambda_result}")

    # Использование функции высшего порядка
    higher_order_result = higher_order_function(lambda x: x * 3)
    print(f"Результат функции высшего порядка: {higher_order_result}")

    # Создание объектов класса
    person = Person("Иван", 30)
    person.introduce()
    Person.static_method()

    student = Student("Алиса", 20, "12345")
    student.introduce()
    student.show_student_id()

    # Использование условного оператора
    age = 25
    message = "Взрослый" if age >= 18 else "Несовершеннолетний"
    print(f"Статус: {message}")

    # Использование цикла for
    for i in range(1, 6):
        print(f"Итерация {i}")

    # Использование цикла while
    count = 0
    while count < 3:
        print(f"Счетчик: {count}")
        count += 1

    # Использование обработки исключений
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Произошло исключение: {str(e)}")

    # Использование list comprehension
    squares = [x ** 2 for x in range(1, 6)]
    print(f"Квадраты чисел: {squares}")

    # Использование dict comprehension
    cube_dict = {x: x ** 3 for x in range(1, 6)}
    print(f"Словарь кубов: {cube_dict}")
    
'''

    preprocessor = PythonCodePreprocessor()
    preprocessed_code = preprocessor.preprocess_code(test_code)
    print("Preprocessed code:")
    print(preprocessed_code)


if __name__ == '__main__':
    test_preprocess_code()
