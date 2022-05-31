from Stack_Queue import Stack, Queue
from practice2.Person import Generator, Person


def test_stack_push():
    stack_list = Stack()
    g = Generator()
    value = g.generate_single()
    stack_list.push(value)
    assert value == stack_list.get_all()[0]
    stack_list.cleaning()


def test_stack_push_type():
    stack_list = Stack()
    g = Generator()
    value = g.generate_single()
    stack_list.push(value)
    assert isinstance(stack_list.top(), Person)
    stack_list.cleaning()


def test_stack_get_all():
    stack_list = Stack()
    g = Generator()
    values = [g.generate_single() for _ in range(5)]
    for value in values:
        stack_list.push(value)
    assert values == stack_list.get_all()
    stack_list.cleaning()


def test_stack_size():
    stack_list = Stack()
    g = Generator()
    stack_list.push(g.generate_single())
    stack_list.push(g.generate_single())
    stack_list.push(g.generate_single())
    assert len(stack_list) == 3
    stack_list.cleaning()


def test_stack_top():
    stack_list = Stack()
    g = Generator()
    stack_list.push(g.generate_single())
    stack_list.push(g.generate_single())
    gen = g.generate_single()
    stack_list.push(gen)
    assert stack_list.top() == gen
    stack_list.cleaning()


def test_stack_pop():
    stack_list = Stack()
    g = Generator()
    stack_list.push(g.generate_single())
    stack_list.push(g.generate_single())
    gen = g.generate_single()
    stack_list.push(gen)
    assert stack_list.pop() == gen
    assert len(stack_list) == 2
    stack_list.cleaning()


def test_stack_pop_empty():
    stack_list = Stack()
    assert stack_list.pop() is None
    assert len(stack_list) == 0
    stack_list.cleaning()


def test_queue_enqueue():
    queue_list = Queue()
    g = Generator()
    value = g.generate_single()
    queue_list.enqueue(value)
    assert value == queue_list.get_all()[0]
    queue_list.cleaning()


def test_queue_enqueue_type():
    queue_list = Queue()
    g = Generator()
    value = g.generate_single()
    queue_list.enqueue(value)
    assert isinstance(queue_list.top(), Person)
    queue_list.cleaning()


def test_queue_size():
    queue_list = Queue()
    g = Generator()
    queue_list.enqueue(g.generate_single())
    queue_list.enqueue(g.generate_single())
    queue_list.enqueue(g.generate_single())
    assert len(queue_list) == 3
    queue_list.cleaning()


def test_queue_dequeue():
    queue_list = Queue()
    g = Generator()
    queue_list.enqueue(g.generate_single())
    queue_list.enqueue(g.generate_single())
    assert queue_list.get_all()[0] == queue_list.dequeue()
    assert len(queue_list) == 1
    queue_list.cleaning()


def test_queue_dequeue_empty():
    queue_list = Queue()
    assert queue_list.dequeue() is None
    assert len(queue_list) == 0
    queue_list.cleaning()


def test_queue_top():
    queue_list = Queue()
    g = Generator()
    gen = g.generate_single()
    queue_list.enqueue(gen)
    queue_list.enqueue(g.generate_single())
    queue_list.enqueue(g.generate_single())
    assert queue_list.top() == gen
    queue_list.cleaning()


def test_queue_get_all():
    queue_list = Stack()
    g = Generator()
    values = [g.generate_single() for _ in range(5)]
    for value in values:
        queue_list.push(value)
    assert values == queue_list.get_all()
    queue_list.cleaning()

