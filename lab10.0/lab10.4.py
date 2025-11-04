class LowExperienceError(Exception):
    """Исключение для малого опыта работы"""
    pass


class HighExperienceError(Exception):
    """Исключение для слишком большого опыта работы"""
    pass


try:
    experience = int(input("Введите стаж работы сотрудника: "))

    if experience < 1:
        raise LowExperienceError("Слишком малый опыт! Минимальный стаж - 1 год.")
    elif experience > 40:
        raise HighExperienceError("Слишком большой опыт! Максимальный стаж - 8040 лет.")
    elif experience < 3:
        raise LowExperienceError("Внимание: сотрудник с малым опытом работы.")

    print("Стаж принят. Сотрудник добавлен в базу.")

except LowExperienceError as e:
    print(f"Предупреждение: {e}")
except HighExperienceError as e:
    print(f"Ошибка проверки: {e}")
except ValueError:
    print("Ошибка: Стаж работы должен быть числом!")