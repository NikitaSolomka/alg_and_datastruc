from employee import Employee
from employee import Generator


def test_employee():
    p = Employee('some', 'example', '2000-01-01', 'male')
    assert p.name == 'some'
    assert p.surname == 'example'
    assert p.birthdate == '2000-01-01'
    assert p.gender == 'male'


def test_employee_getinfo():
    p = Employee('some', 'example', '2003-02-05', 'male')
    assert isinstance(p.get_info(), str)


def test_gen_single_type():
    g = Generator()
    p = g.generate_single()
    assert isinstance(p, Employee)
    assert isinstance(p.name, str)
    assert isinstance(p.surname, str)
    assert isinstance(p.birthdate, str)
    assert isinstance(p.gender, str)


def test_gen_1000_type():
    g = Generator()
    persons = g.generate_1000()
    assert isinstance(persons, list)
    assert isinstance(persons[0], Employee)
    assert len(persons) == 1000


def test_gen_10_000_type():
    g = Generator()
    persons = g.generate_10_000()
    assert isinstance(persons, list)
    assert isinstance(persons[0], Employee)
    assert len(persons) == 10000
