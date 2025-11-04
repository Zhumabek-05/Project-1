try:
    name = input("Введите имя сотрудника: ")
    experience = input("Введите стаж работы: ")
    if not experience.isdigit():
        raise ValueError("Стаж работы должен быть числом!")
    experience_int = int(experience)
    if experience_int < 0:
        raise ValueError("Стаж работы не может быть отрицательным!")
    with open("employees.txt", "a") as file:
        file.write(f"\n{name}, {experience_int}")
    print("Запись добавлена успешно!")
    try:
        with open("employees.txt", "r") as file:
            print("\nТекущий список сотрудников:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Ошибка: Файл не найден!")

except ValueError as e:
    print(f"Ошибка ввода: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    print("Программа завершена.")