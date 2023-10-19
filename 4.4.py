class Student:
    total_students = 0

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = 0.0
        Student.total_students += 1

    def set_gpa(self, gpa):
        self.gpa = gpa
        print(f"У {self.name} средний балл: {self.gpa}")

    @staticmethod
    def is_honor(gpa):
        return gpa >= 9

    @classmethod
    def get_total_students(cls):
        return cls.total_students


def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Некорректный ввод числа. Попробуйте еще раз.")


def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Некорректный ввод числа. Попробуйте еще раз.")


students = []
while True:
    name = input("Введите имя студента (или '0' для выхода): ")
    if name.lower() == '0':
        break
    age = input_int("Введите возраст студента: ")
    major = input("Введите специальность студента: ")

    student = Student(name, age, major)
    students.append(student)

    gpa = input_float("Введите средний балл студента: ")

gpa_to_check = input_float("Введите средний балл для проверки, является ли студент отличником: ")
print(f"Студент со средним баллом {gpa_to_check} является отличником: {Student.is_honor(gpa_to_check)}")

total_students = Student.get_total_students()
print(f"Всего студентов: {total_students}")
