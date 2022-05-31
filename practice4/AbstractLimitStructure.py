from abc import ABC, abstractmethod


class AbstractStack(ABC):

    @abstractmethod
    def push(self, value: object):
        ...

    @abstractmethod
    def pop(self) -> object:
        ...

    @abstractmethod
    def top(self) -> object:
        ...


class AbstractQueue(ABC):

    @abstractmethod
    def enqueue(self, value: object):
        ...

    @abstractmethod
    def dequeue(self) -> object:
        ...

    @abstractmethod
    def top(self) -> object:
        ...


class AbstractDeque(ABC):

    @abstractmethod
    def push_front(self, value: object):
        ...

    @abstractmethod
    def push_back(self, value: object):
        ...

    @abstractmethod
    def pop_front(self) -> object:
        ...
