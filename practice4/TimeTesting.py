from datetime import datetime
from practice2.Person import Generator
from Stack_Queue import Stack, Queue
from colorama import Fore


class StackTime:

    def __init__(self, gen):
        self.stack = Stack()
        self.gen = gen

    def time_push(self):
        timer_start = datetime.utcnow()
        for item in self.gen:
            self.stack.push(item)
        timer_stop = datetime.utcnow() - timer_start
        print("Push 10 000 объектов:\n" + Fore.CYAN + str(timer_stop) + Fore.RESET)

    def time_pop(self):
        timer_start = datetime.utcnow()

        for i in range(len(self.gen)):
            self.stack.pop()

        timer_stop = datetime.utcnow() - timer_start
        print("Pop 10 000 объектов:\n" + Fore.CYAN + str(timer_stop) + Fore.RESET)

    def time_top(self):
        timer_start = datetime.utcnow()

        for i in range(len(self.gen)):
            self.stack.top()

        timer_stop = datetime.utcnow() - timer_start
        print("Top 10 000 объектов:\n" + Fore.CYAN + str(timer_stop) + Fore.RESET)


class QueueTime:
    def __init__(self, gen):
        self.queue = Queue()
        self.gen = gen

    def time_enqueue(self):
        timer_start = datetime.utcnow()
        for item in self.gen:
            self.queue.enqueue(item)
        timer_stop = datetime.utcnow() - timer_start
        print("Enqueue 10 000 объектов:\n" + Fore.CYAN + str(timer_stop) + Fore.RESET)

    def time_dequeue(self):
        timer_start = datetime.utcnow()

        for i in range(len(self.gen)):
            self.queue.dequeue()

        timer_stop = datetime.utcnow() - timer_start
        print("Dequeue 10 000 объектов:\n" + Fore.CYAN + str(timer_stop) + Fore.RESET)

    def time_top(self):
        timer_start = datetime.utcnow()

        for i in range(len(self.gen)):
            self.queue.top()

        timer_stop = datetime.utcnow() - timer_start
        print("Top 10 000 объектов:\n" + Fore.CYAN + str(timer_stop) + Fore.RESET)


if __name__ == "__main__":

    G = Generator()
    generate = G.generate_10_000()
    st = StackTime(generate)

    print(f"{Fore.GREEN}---------\n| Stack |\n---------{Fore.RESET}")
    st.time_push()
    st.time_top()
    st.time_pop()

    qu = QueueTime(generate)
    print(f"\n\n{Fore.GREEN}---------\n| Queue |\n---------{Fore.RESET}")
    qu.time_enqueue()
    qu.time_dequeue()
    qu.time_top()
