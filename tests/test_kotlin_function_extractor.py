# test_kotlin_code_preprocessor.py
from pythonProject.collect_data import KotlinFunctionExtractor


def test_extract_functions():
    test_code = '''
// Объявление пакета
package com.example

// Импорт классов
import kotlin.math.*

// Объявление константы
const val PI = 3.14159

// Объявление переменной
var globalVariable = 42

// Объявление функции высшего порядка
fun higherOrderFunction(function: (Int) -> Int): Int {
    return function(10)
}

// Объявление лямбда-функции
val lambda: (Int) -> Int = { x -> x * 2 }

// Объявление класса с первичным конструктором
@Suppress("ConstructorParameterNaming")
class Person(val name: String, var age: Int) {
    // Объявление вторичного конструктора
    constructor(name: String) : this(name, 0)

    // Объявление функции-члена класса
    fun introduce() {
        println("Меня зовут $name, мне $age лет.")
    }

    // Объявление вложенного класса
    inner class Job(val title: String) {
        fun showJobTitle() {
            println("Я работаю $title в компании ${this@Person.name}.")
        }
    }
}

// Объявление интерфейса
interface Printable {
    fun print()
}

// Объявление класса с реализацией интерфейса
class Document(val content: String) : Printable {
    override fun print() {
        println("Содержимое документа: $content")
    }
}

// Объявление класса данных
data class User(val id: Int, val name: String, val email: String)

// Объявление перечисления
enum class Color {
    RED, GREEN, BLUE
}

// Главная функция
fun main() {
    // Использование переменных и констант
    println("Значение PI: $PI")
    globalVariable += 10
    println("Значение globalVariable: $globalVariable")

    // Использование функций
    fun localFunction(x: Int, y: Int): Int {
        return x + y
    }
    val result = localFunction(5, 7)
    println("Результат localFunction: $result")

    // Использование лямбда-функции
    val lambdaResult = lambda(5)
    println("Результат лямбда-функции: $lambdaResult")

    // Использование функции высшего порядка
    val higherOrderResult = higherOrderFunction { it * 3 }
    println("Результат функции высшего порядка: $higherOrderResult")

    // Создание объектов класса
    val person = Person("Иван", 30)
    person.introduce()
    val job = person.Job("Программист")
    job.showJobTitle()

    // Использование класса с реализацией интерфейса
    val document = Document("Это пример документа.")
    document.print()

    // Использование класса данных
    val user = User(1, "Алиса", "alice@example.com")
    println("Данные пользователя: $user")

    // Использование перечисления
    val color = Color.GREEN
    println("Выбранный цвет: $color")

    // Использование условного выражения
    val age = 25
    val message = if (age >= 18) "Взрослый" else "Несовершеннолетний"
    println("Статус: $message")

    // Использование цикла for
    for (i in 1..5) {
        println("Итерация $i")
    }

    // Использование цикла while
    var count = 0
    while (count < 3) {
        println("Счетчик: $count")
        count++
    }

    // Использование обработки исключений
    try {
        val result = 10 / 0
    } catch (e: ArithmeticException) {
        println("Произошло исключение: ${e.message}")
    }

    // Использование функции расширения
    fun String.reverseString(): String {
        return this.reversed()
    }
    val str = "Hello, World!"
    println("Перевернутая строка: ${str.reverseString()}")
}
    '''

    extractor = KotlinFunctionExtractor()
    functions = extractor.extract_functions(test_code)
    print("Functions:")
    print(functions)


if __name__ == '__main__':
    test_extract_functions()