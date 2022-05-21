from datetime import datetime


class Employee:
    def __init__(self, name, surname, birthdate, gender, phone, position):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.phone = phone
        self.position = position

        self.check()

    def check(self):
        age = int((datetime.today() - datetime.strptime(self.birthdate, "%Y-%m-%d")).days / 365.25)
        vacancies = list()
        if self.gender == "male":
            if age >= 25:
                vacancies.append("Инженер")
            if age in range(18, 26):
                vacancies.append("Курьер")
        elif self.gender == "female":
            if age >= 45:
                vacancies.append("Уборщица")
            if age in range(20, 31):
                vacancies.append("Секретарь")

        self.get_info(vacancies)

    def get_info(self, v):
        if len(v) >= 1:
            print(f'{self.name} {self.surname}, Вам доступны данные вакансии: {", ".join(v)}. '
                  f'Мы Вам перезвоним в течении 1-2 дней, по указанному Вами номеру ({self.phone})')
        elif len(v) <= 0:
            print(f'{self.name} {self.surname}, к сожалению для Вас доступных вакансий сейчас нет')


if __name__ == '__main__':
    p1 = Employee("Lilly", "King", "2000-06-13", "female", "380631781345", "Секретарь")
    p2 = Employee("Thomas", "Davies", "1996-06-13", "male", "38098973677", "Инженер")
    p3 = Employee("Amelia", "Brown", "2003-06-13", "female", "38098434011", "Секретарь")
    p4 = Employee("George", "Wilson", "1996-02-13", "male", "380992192687", "Курьер")
    p5 = Employee("Connor", "Evans", "2003-06-13", "male", "3809824365337", "Инженер")
