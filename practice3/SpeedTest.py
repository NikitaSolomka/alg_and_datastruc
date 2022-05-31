from practice2.Person import Generator
from StandardList import StandardList
from datetime import datetime

gen = Generator()

# Генерация новых объектов
timer_start = datetime.utcnow()
gen_10_000 = gen.generate_10_000()
timer_stop = datetime.utcnow() - timer_start
print(f'Генерация 10 000 элементов:\n{timer_stop}\n')

# Таймер для добавления элементов в конец массива
timer_start = datetime.utcnow()

s_list = StandardList()
for person in gen_10_000:
    s_list.add(person)

timer_stop = datetime.utcnow() - timer_start
print(f'Добавление 10 000 элементов в конец массива:\n{timer_stop}\tРазмер массива: {s_list.size}\n')

# Таймер для добавления элементов в начало массива
timer_start = datetime.utcnow()

s_list = StandardList()
for person in gen_10_000:
    s_list.add(person, 0)

timer_stop = datetime.utcnow() - timer_start
print(f'Добавление 10 000 новых элементов в начало:\n{timer_stop}\tРазмер массива: {s_list.size}\n')

# Таймер для замены элемента
timer_start = datetime.utcnow()

for person in gen_10_000:
    s_list.insert(person, len(gen_10_000) - 1)

timer_stop = datetime.utcnow() - timer_start
print(f'Последовательная замена последнего элемента 10 000 значений:\n{timer_stop}\tРазмер массива: {s_list.size}\n')

# Таймер для поиска элемента
timer_start = datetime.utcnow()

res = s_list.find(gen_10_000[0])

timer_stop = datetime.utcnow() - timer_start
print(f'Поиск первого элемента:\n{timer_stop}\tРазмер массива: {s_list.size} Индекс элемента: {res}\n')


# Таймер для поиска элемента
timer_start = datetime.utcnow()

res = s_list.find(gen_10_000[9999])

timer_stop = datetime.utcnow() - timer_start
print(f'Поиск последнего элемента:\n{timer_stop}\tРазмер массива: {s_list.size} Индекс элемента: {res}\n')

# Таймер для поиска элемента по индексу
timer_start = datetime.utcnow()

res = s_list.get(9999)

timer_stop = datetime.utcnow() - timer_start
print(f'Поиск последнего элемента из 10 000 по индексу:\n{timer_stop}\tРазмер массива: {s_list.size} Элемент: {res}\n')

# Таймер для удаления первых элементов
timer_start = datetime.utcnow()

for person in gen_10_000:
    s_list.remove(person)

timer_stop = datetime.utcnow() - timer_start
print(f'Удаление 1-го элемента 10 000 раз:\n{timer_stop}\tРазмер массива: {s_list.size}\n')

# Таймер для удаления последних элементов
timer_start = datetime.utcnow()

# Заполнение списка, после предыдущего удаления
for person in gen_10_000:
    s_list.add(person)

for person in reversed(gen_10_000):
    s_list.remove(person)

timer_stop = datetime.utcnow() - timer_start
print(f'Удаление последнего элемента 10 000 раз:\n{timer_stop}\tРазмер массива: {s_list.size}')
