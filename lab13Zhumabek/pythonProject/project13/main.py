# project13/main.py

# Способ 1: Импорт конкретных функций
from math_utils import add, divide
from string_utils import capitalize_words

# Способ 2: Импорт всего модуля с псевдонимом
import math_utils as mu
import string_utils as su

# Демонстрация работы
print("Сложение:", add(5, 3))
print("Деление:", divide(10, 2))

print("С заглавной буквы:", capitalize_words("жумабек"))
print("Количество букв:", su.count_letters("Жумабек"))

# Использование псевдонима
print("Умножение:", mu.multiply(4, 6))
print("Вычитание:", mu.subtract(9, 2))
