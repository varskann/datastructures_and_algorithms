import pytest
from datastructures_and_algorithms.datastructures.stack import Stack

def test_stack():
    q = Stack()
    q.push(1)
    q.push(2)
    assert q.pop() == 2, "Stack didn't return last element"
    q.push(3)
    q.push(4)
    assert q.traverse() == [4, 3, 1], "Stack storage corrupt"


def test_stack_char():
    q = Stack()
    q.push("a")
    q.push("b")
    assert q.pop() == "b", "Stack didn't return last element"
    q.push("c")
    q.push("d")
    assert q.traverse() == ["d", "c", "a"], "Stack storage corrupt"