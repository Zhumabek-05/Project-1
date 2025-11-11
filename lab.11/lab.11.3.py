import math


# БАЗОВЫЙ КЛАСС - Фигура
class Shape:
    def area(self):
        pass  # Абстрактный метод - будет переопределен в дочерних классах

    def perimeter(self):
        pass

    def display_info(self):
        print(f"Фигура: {self.__class__.__name__}")


# ПРОИЗВОДНЫЙ КЛАСС - Круг
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display_info(self):
        super().display_info()
        print(f"🔵 Радиус: {self.radius}")
        print(f"📐 Площадь: {self.area():.2f}")
        print(f"📏 Длина окружности: {self.perimeter():.2f}")


# ПРОИЗВОДНЫЙ КЛАСС - Прямоугольник
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def display_info(self):
        super().display_info()
        print(f"📏 Ширина: {self.width}, Высота: {self.height}")
        print(f"📐 Площадь: {self.area()}")
        print(f"📏 Периметр: {self.perimeter()}")


# ПРОИЗВОДНЫЙ КЛАСС - Треугольник
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def display_info(self):
        super().display_info()
        print(f"🔺 Основание: {self.base}, Высота: {self.height}")
        print(f"📐 Площадь: {self.area()}")
        print(f"📏 Периметр: {self.perimeter()}")


# ПРОИЗВОДНЫЙ КЛАСС - Квадрат (наследуется от Rectangle)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Ширина и высота равны
        self.side = side

    def display_info(self):
        super().display_info()
        print(f"◼️ Сторона квадрата: {self.side}")


# ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА
print("🎯 ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА С ФИГУРАМИ\n")

# Создаем список разных фигур
shapes = [
    Circle(5),  # Круг с радиусом 5
    Rectangle(4, 6),  # Прямоугольник 4x6
    Triangle(3, 4, 3, 4, 5),  # Треугольник с основанием 3, высотой 4 и сторонами 3, 4, 5
    Square(5)  # Квадрат со стороной 5
]

print("1. ИНФОРМАЦИЯ О ВСЕХ ФИГУРАХ:")
print("=" * 50)
for shape in shapes:
    shape.display_info()
    print("-" * 30)

print("\n2. ТОЛЬКО ПЛОЩАДИ (ПОЛИМОРФИЗМ В ДЕЙСТВИИ):")
print("=" * 50)
for i, shape in enumerate(shapes, 1):
    area = shape.area()
    print(f"Фигура {i} ({shape.__class__.__name__}): Площадь = {area:.2f}")

print("\n3. ТОЛЬКО ПЕРИМЕТРЫ:")
print("=" * 50)
for i, shape in enumerate(shapes, 1):
    perimeter = shape.perimeter()
    print(f"Фигура {i} ({shape.__class__.__name__}): Периметр = {perimeter:.2f}")

print("\n4. СРАВНЕНИЕ ФИГУР ПО ПЛОЩАДИ:")
print("=" * 50)
for i, shape in enumerate(shapes, 1):
    area = shape.area()
    if area > 20:
        size = "большая"
    elif area > 10:
        size = "средняя"
    else:
        size = "маленькая"
    print(f"Фигура {i}: Площадь {area:.2f} - {size}")
