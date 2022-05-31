from practice4.AbstractLimitStructure import AbstractQueue, AbstractStack
from practice2.Person import Person, Generator


class Stack(AbstractStack):
    __list = list()

    def push(self, value: Person) -> bool:
        try:
            self.__list.append(value)
            return True
        except ValueError:
            return False

    def pop(self) -> [Person, None]:
        try:
            return self.__list.pop()
        except IndexError:
            return None

    def top(self) -> [Person, None]:
        try:
            return self.__list[-1]
        except IndexError:
            return None

    def __len__(self) -> int:
        return len(self.__list)

    def get_all(self) -> list:
        return self.__list.copy()


class Queue(AbstractQueue):
    __list = list()

    def enqueue(self, value: Person) -> bool:
        try:
            self.__list.append(value)
            return True
        except ValueError:
            return False

    def dequeue(self) -> [Person, None]:
        try:
            return self.__list.pop(0)
        except IndexError:
            return None

    def top(self) -> [Person, None]:
        try:
            return self.__list[0]
        except IndexError:
            return None

    def __len__(self) -> int:
        return len(self.__list)

    def get_all(self) -> list:
        return self.__list.copy()


if __name__ == "__main__":
    g = Generator()

    stack = Stack()
    for i in range(5):
        stack.push(g.generate_single())
    print(stack.get_all())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.get_all())
    print(stack.pop())
    print(stack.get_all())