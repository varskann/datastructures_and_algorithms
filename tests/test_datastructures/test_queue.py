import pytest
from datastructures_and_algorithms.datastructures.queue import Queue


def test_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1, "deque didn't return earliest element"
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    assert q.traverse() == [2, 3, 4, 5, 6], "Queue storage corrupt"


def test_queue_char():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    assert q.dequeue() == "a", "deque didn't return earliest element"
    q.enqueue("d")
    assert q.traverse() == ["b", "c", "d"], "Queue storage corrupt"