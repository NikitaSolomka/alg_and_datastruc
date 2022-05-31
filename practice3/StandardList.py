from AbstractStructure import AbstractStructure
from practice2.Person import Person
from practice2.Person import Generator


class StandardList(AbstractStructure):
    __list: list = list()
    value: Person
    size: int = 0

    def add(self, value, index: [int, None] = None) -> bool:
        if index is not None and self.size <= index < -self.size:
            return False

        if index is None:
            self.__list.append(value)
        else:
            self.__list.insert(index, value)
        self.size += 1
        return True

    def insert(self, value, index: int) -> bool:
        if index is None or self.size <= index or -self.size > index:
            return False

        self.__list[index] = value
        return True

    def find(self, value) -> [int, None]:
        if value in self.__list:
            return self.__list.index(value)
        return None

    def get(self, index: int) -> [Person, None]:
        if self.size > index >= -self.size:
            return self.__list[index]
        return None

    def remove(self, value) -> bool:
        try:
            if value in self.__list:
                self.__list.remove(value)
                self.size -= 1
                return True
        except ValueError:
            return False

    def get_all(self) -> list:
        return self.__list

    def __len__(self):
        return self.size


if __name__ == "__main__":

    my_list = StandardList()
    g = Generator()

    p1 = g.generate_single()
    p2 = g.generate_single()
    p3 = g.generate_single()

    # Сгенерированные объекты:
    print(f'Сгенерированные объекты:   {[p1, p2, p3]}')

    # Добавление объектов в конец списка (без индекса):
    my_list.add(p1)
    my_list.add(p2)
    my_list.add(p3)

    # Результат добавления объектов в конец списка:
    print(f'Результат добавления объектов в конец списка:   {my_list.get_all()}')

    # Добавление объекта в конкретную позицию (со смещением):
    p4 = g.generate_single()
    print(f'\nГенерация нового объекта:   {[p4]}')

    my_list.add(p4, 1)
    print(f'Результат добавления объекта в конкретную позицию:')
    print(my_list.get_all())

    # Добавления объекта в конкретную позицию, с заменой:
    p5 = g.generate_single()
    print(f'\nГенерация нового объекта:   {[p5]}')
    my_list.insert(p5, 0)
    print(f'Результат добавления объекта с заменой:')
    print(my_list.get_all())

    # Поиск элемента по его значению, для получения индекса:
    print(f'\nРезультат поиска объекта {[p5]} для получения его индекса:')
    print(my_list.find(p5))

    # Поиск объекта по его индексу:
    print(f'\nРезультат поиска объекта по его индексу, например 2:')
    print(my_list.get(2))

    # Удаление объекта
    print(f'\nУдаление объекта {[p5]} и {[p3]} из списка:')
    print(f'Удаление объекта p5: {my_list.remove(p5)}')
    print(f'Удаление объекта p3: {my_list.remove(p3)}')
    print(f'Проба повторного удаления уже удаленного объекта: {my_list.remove(p5)}')
    print(my_list.get_all())

