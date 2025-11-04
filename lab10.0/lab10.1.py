with open("employees.txt", "r") as file:
    experience_years = []
    for line in file:
        name, years = line.strip().split(", ")
        experience_years.append(int(years))
        print(f"{name} - {years} лет опыта")
    print("Средний стаж работы:", sum(experience_years) / len(experience_years))