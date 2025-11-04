name = input("Введите имя сотрудника: ")
experience = input("Введите стаж работы (в годах): ")
with open("employees.txt", "a") as file:
    file.write(f"\n{name}, {experience}")
print("Запись добавлена успешно!")
print("\nОбновленный список сотрудников:")
with open("employees.txt", "r") as file:
    for line in file:
        print(line.strip())