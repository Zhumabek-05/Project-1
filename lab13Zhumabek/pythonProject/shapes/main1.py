# main.py
from shapes.circle import Circle
from shapes.rectangle import Rectangle

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Площадь круга: {circle.area():.2f}")
print(f"Площадь прямоугольника: {rectangle.area()}")
