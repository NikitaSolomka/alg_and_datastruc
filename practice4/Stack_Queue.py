from practice4.AbstractLimitStructure import AbstractQueue, AbstractStack
from practice2.Person import Person, Generator
from colorama import Fore


class Stack(AbstractStack):
    __list: list = list()
    size: int = 0

    def push(self, value: Person) -> bool:
        try:
            self.__list.append(value)
            self.size += 1
            return True
        except ValueError:
            return False

    def pop(self) -> [Person, None]:
        try:
            obj = self.__list.pop()
            self.size -= 1
            return obj
        except IndexError:
            return None

    def top(self) -> [Person, None]:
        try:
            return self.__list[-1]
        except IndexError:
            return None

    def __len__(self):
        return self.size

    def get_all(self) -> list:
        return self.__list.copy()

    def cleaning(self) -> bool:
        self.__list.clear()
        self.size = 0
        return True


class Queue(AbstractQueue):
    __list: list = list()
    size: int = 0

    def enqueue(self, value: Person) -> bool:
        try:
            self.__list.append(value)
            self.size += 1
            return True
        except ValueError:
            return False

    def dequeue(self) -> [Person, None]:
        try:
            obj = self.__list.pop(0)
            self.size -= 1
            return obj
        except IndexError:
            return None

    def top(self) -> [Person, None]:
        try:
            return self.__list[0]
        except IndexError:
            return None

    def __len__(self):
        return self.size

    def get_all(self) -> list:
        return self.__list.copy()

    def cleaning(self) -> bool:
        self.__list.clear()
        self.size = 0
        return True


if __name__ == "__main__":
    g = Generator()
    my_list = Stack()

    print(f'{Fore.LIGHTGREEN_EX}Реализация класса Stack\n{"-"*200}{Fore.RESET}')
    # Генерация объектов
    p1 = g.generate_single()
    p2 = g.generate_single()
    p3 = g.generate_single()

    # Сгенерированные объекты:
    print(f'{Fore.CYAN}Сгенерированные объекты:   {[p1, p2, p3]}')

    # Добавление объектов методом Push:
    my_list.push(p1)
    my_list.push(p2)
    my_list.push(p3)

    # Результат использования метода Push:
    print(f'\nРезультат добавления объектов в массив, с помощью метода push:\n{my_list.get_all()}')

    # Использование метода Pop:
    print(f'\nРезультат использования метода pop:  {my_list.pop()}')
    print(f'\nМассив, после использования метода pop на нём:\n{my_list.get_all()}')

    # Использование метода Top:
    print(f'\nРезультат использования метода top:  {my_list.top()}')
    print(f'\nМассив, после использования метода top на нём:\n{my_list.get_all()}{Fore.RESET}')

    print(f'\n{Fore.LIGHTGREEN_EX}Конец реализации класса Stack\n{"-" * 200}{Fore.RESET}')

    print(f'\n\n{Fore.LIGHTGREEN_EX}Реализация класса Queue\n{"-" * 200}{Fore.RESET}')

    mylist = Queue()

    # Генерация объектов
    p4 = g.generate_single()
    p5 = g.generate_single()
    p6 = g.generate_single()

    # Сгенерированные объекты:
    print(f'{Fore.CYAN}Сгенерированные объекты:   {[p4, p5, p6]}')

    # Добавление объектов методом enqueue:
    mylist.enqueue(p4)
    mylist.enqueue(p5)
    mylist.enqueue(p6)

    # Результат использования метода enqueue:
    print(f'\nРезультат добавления объектов в массив, с помощью метода enqueue:\n{mylist.get_all()}')

    # Использование метода dequeue:
    print(f'\nРезультат использования метода dequeue:  {mylist.dequeue()}')
    print(f'\nМассив, после использования метода dequeue на нём:\n{mylist.get_all()}')

    # Использование метода Top:
    print(f'\nРезультат использования метода top:  {mylist.top()}')
    print(f'\nМассив, после использования метода top на нём:\n{mylist.get_all()}{Fore.RESET}')

    print(f'\n{Fore.LIGHTGREEN_EX}Конец реализации класса Queue\n{"-" * 200}{Fore.RESET}')
