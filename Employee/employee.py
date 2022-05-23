from datetime import datetime
from datetime import date
import names
import random


class Employee:
    name: str
    surname: str
    birthdate: str
    gender: str

    def __init__(self, name: str, surname: str,  birthdate: str, gender: str):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def __repr__(self):
        return f'Person({self.name} {self.surname}, {self.gender}, {self.birthdate})'

    def check_positions(self) -> list:
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
        return vacancies

    def get_info(self):
        v = self.check_positions()
        if len(v) >= 1:
            return f'{self.name} {self.surname}, Вам доступны данные вакансии: {", ".join(v)}'
        elif len(v) <= 0:
            return f'{self.name} {self.surname}, к сожалению для Вас доступных вакансий сейчас нет'


class Generator:
    genders = ['female', 'male']

    def create_date(self):
        year = random.randint(1967, date.today().year)
        month = random.randint(1, 12)
        if month == 2:
            day = random.randint(1, 28)
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            day = random.randint(1, 31)
        else:
            day = random.randint(1, 30)
        return f'{year}-{month}-{day}'

    def generate_single(self) -> Employee:
        gen = random.randint(0, 1)
        gender = self.genders[gen]
        name = names.get_first_name(gender)
        surname = names.get_last_name()

        birthdate = self.create_date()
        return Employee(name, surname, birthdate, gender)

    def generate_1000(self) -> list:
        persons = list()
        while True:
            persons.append(self.generate_single())
            if len(persons) == 1000:
                break
        return persons

    def generate_10_000(self) -> list:
        persons = list()
        while True:
            persons.append(self.generate_single())
            if len(persons) == 10000:
                break
        return persons


if __name__ == '__main__':
    p = Employee("Lilly", "King", "2000-06-13", "female")
    print(p)
    print(p.get_info() + '\n')

    p = Employee("Mark", "White", "1996-06-13", "male")
    print(p)
    print(p.get_info() + '\n')

    g = Generator()
    p = g.generate_single()
    print(p)
    print(p.get_info() + '\n')

    print(f'{g.generate_1000()} \n')

    # print(f'{g.generate_10_000()} \n')
