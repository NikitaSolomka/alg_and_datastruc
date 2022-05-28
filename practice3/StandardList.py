from AbstractStructure import AbstractStructure
from practice2.Person import Person
from practice2.Person import Generator


class StandartList(AbstractStructure):
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
        if value in self.__list:
            self.__list.remove(value)
            self.size -= 1
            return True
        return False

    def get_all(self) -> list:
        return self.__list

    def __len__(self):
        return self.size


if __name__ == "__main__":

    s_list = StandartList()
    g = Generator()

    p1 = g.generate_single()
    p2 = g.generate_single()
    p3 = g.generate_single()

    print([p1, p2, p3])

    s_list.add(p1)
    s_list.add(p2)
    s_list.add(p3, 0)
    print(s_list.get_all())

    p4 = g.generate_single()
    print(s_list.insert(p4, 1))
    print(s_list.insert(p4, 10))

    print(s_list.get_all())
    print(len(s_list))

    print(s_list.find(p1))
    print(s_list.find(p2))

    print(s_list.get(2))
    print(s_list.remove(p2))
    print(s_list.remove(p2))
