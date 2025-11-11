class Teacher:
    def __init__(self, name, subject, years_experience):
        self.name = name
        self.subject = subject
        self.years_experience = years_experience
        self.students_count = 0

    def role(self):
        print(f"👨‍🏫 {self.name} преподает предмет '{self.subject}'")

    def teach(self):
        print(f"📚 {self.name} проводит лекцию по {self.subject}")
        self.students_count += 1

    def display_info(self):
        print(f"Преподаватель: {self.name}")
        print(f"Предмет: {self.subject}")
        print(f"Опыт работы: {self.years_experience} лет")
        print(f"Студентов обучил: {self.students_count}")


class Researcher:
    def __init__(self, name, research_field, publications_count):
        self.name = name
        self.research_field = research_field
        self.publications_count = publications_count
        self.grants_won = 0

    def role(self):
        print(f"🔬 {self.name} проводит исследования в области '{self.research_field}'")

    def conduct_research(self):
        print(f"🧪 {self.name} проводит исследование: {self.research_field}")
        self.publications_count += 1

    def win_grant(self, amount):
        print(f"💰 {self.name} выиграл грант на {amount} рублей!")
        self.grants_won += amount

    def display_info(self):
        print(f"Исследователь: {self.name}")
        print(f"Область исследований: {self.research_field}")
        print(f"Публикаций: {self.publications_count}")
        print(f"Выиграно грантов: {self.grants_won} руб.")


class Professor(Teacher, Researcher):
    def __init__(self, name, subject, years_experience, research_field, publications_count, university):
        Teacher.__init__(self, name, subject, years_experience)
        Researcher.__init__(self, name, research_field, publications_count)
        self.university = university
        self.projects_managed = []

    def role(self):
        print(f"🎓 ПРОФЕССОР {self.name} - Университет: {self.university}")
        super().role()  # Вызовет метод role() от Teacher
        print("📊 Также управляет академическими проектами")

    def manage_project(self, project_name):
        print(f"📋 {self.name} управляет проектом: '{project_name}'")
        self.projects_managed.append(project_name)

    def display_info(self):
        print("=" * 50)
        print(f"🎓 ПРОФЕССОР: {self.name}")
        print(f"🏛️ Университет: {self.university}")
        print(f"📚 Предмет: {self.subject}")
        print(f"🔬 Исследования: {self.research_field}")
        print(f"⏳ Опыт работы: {self.years_experience} лет")
        print(f"📄 Публикаций: {self.publications_count}")
        print(f"👥 Студентов обучил: {self.students_count}")
        print(f"💰 Выиграно грантов: {self.grants_won} руб.")
        print(f"📋 Проектов управляет: {len(self.projects_managed)}")
        if self.projects_managed:
            print(f"   Активные проекты: {', '.join(self.projects_managed)}")
        print("=" * 50)


# ДЕМОНСТРАЦИЯ РАБОТЫ
print("🎓 СИСТЕМА АКАДЕМИЧЕСКИХ РОЛЕЙ - МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ\n")

professor = Professor(
    name="Иван Петров",
    subject="Компьютерные науки",
    years_experience=15,
    research_field="Искусственный интеллект",
    publications_count=45,
    university="Технический университет"
)

print("1. ДЕМОНСТРАЦИЯ РОЛЕЙ:")
print("-" * 40)
professor.role()

print("\n2. РАБОЧИЕ ФУНКЦИИ:")
print("-" * 40)
professor.teach()
professor.conduct_research()
professor.win_grant(500000)
professor.manage_project("Разработка нейросетей")

print("\n3. ИНФОРМАЦИЯ О ПРОФЕССОРЕ:")
print("-" * 40)
professor.display_info()

print("\n4. ДЕМОНСТРАЦИЯ MRO (Method Resolution Order):")
print("-" * 40)
print("Порядок разрешения методов (MRO):")
for i, cls in enumerate(Professor.__mro__, 1):
    print(f"{i}. {cls.__name__}")

print("\n5. ПРОВЕРКА НАСЛЕДОВАНИЯ:")
print("-" * 40)
print(f"Professor является Teacher: {isinstance(professor, Teacher)}")
print(f"Professor является Researcher: {isinstance(professor, Researcher)}")
print(f"Professor является Professor: {isinstance(professor, Professor)}")
