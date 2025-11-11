class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.species} {self.name} издает звук.")

    def move(self):
        print(f"{self.name} перемещается.")


class Dog(Animal):
    def __init__(self, name, breed="неизвестной породы"):
        super().__init__(name, "Собака")
        self.breed = breed

    def speak(self):
        print(f"🐕 {self.name} ({self.breed}) громко лает: Гав-гав!")

    def guard(self):
        print(f"{self.name} охраняет дом!")


class Cat(Animal):
    def __init__(self, name, color="неизвестного цвета"):
        super().__init__(name, "Кошка")
        self.color = color

    def speak(self):
        print(f"🐈 {self.name} ({self.color}) мяукает: Мяууу~")

    def purr(self):
        print(f"{self.name} мурлычет: Мрррр...")


# ТЕСТИРОВАНИЕ
print("🎭 ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА\n")

animals = [
    Animal("Неопознанный", "Животное"),
    Dog("Рекс", "Овчарка"),
    Dog("Шарик", "Дворняжка"),
    Cat("Васька", "Рыжий"),
    Cat("Мурка", "Серая")
]

print("1. КАЖДОЕ ЖИВОТНОЕ ГОВОРИТ ПО-СВОЕМУ:")
for animal in animals:
    animal.speak()

print("\n2. ПРОВЕРКА ТИПОВ ОБЪЕКТОВ:")
for animal in animals:
    print(f"{animal.name} является {type(animal).__name__}")

print("\n3. ВСЕ ЖИВОТНЫЕ МОГУТ ПЕРЕДВИГАТЬСЯ:")
for animal in animals:
    animal.move()
