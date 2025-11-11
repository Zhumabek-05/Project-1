class Warrior:
    def __init__(self, name, level, player_id, rating, abilities):
        # Конструктор класса - принимает аргументы
        self.name = name
        self.level = level
        self.player_id = player_id
        self.rating = rating
        self.abilities = abilities

    def display_info(self):
        print(f"=== ИНФОРМАЦИЯ О ВОИНЕ ===")
        print(f"👤 Имя: {self.name}")
        print(f"🎯 Уровень: {self.level}")
        print(f"🆔 ID игрока: {self.player_id}")
        print(f"⭐ Рейтинг: {self.rating}/10")
        print(f"✨ Способности: {', '.join(self.abilities)}")


# ПРАВИЛЬНОЕ СОЗДАНИЕ ОБЪЕКТА
player1 = Warrior(
    "Ottoman",  # name
    88,  # level
    "PLR055",  # player_id
    9.5,  # rating
    ["Неуязвимость", "Двойной удар", "Берсерк"]  # abilities
)
player2 = Warrior(
    "Raid",  # name
    89,  # level
    "PLR055",  # player_id
    9.0,  # rating
    ["ghost", "ulta", "Берсерк"]  # abilities
)
player1.display_info()
player2.display_info()