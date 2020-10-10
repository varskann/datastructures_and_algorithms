__author__ = "Kanishk Varshney"
__data__ = "04-Oct-2020"

"""
Queue  Class 
"""
import random
from typing import List, Any

class Node():
    def __init__(self, _value: Any, _next=None):
        self.value = _value
        self.next = _next

class Queue():
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def enqueue(self, _value: Any):
        temp = self._tail
        self._tail = Node(_value)

        if self.is_empty():
            self._head = self._tail
        else:
            temp.next = self._tail
       
    def dequeue(self) -> Any:
        _value = self._head.value
        self._head = self._head.next
        if self.is_empty():
            self._tail = None
        return _value

    def traverse(self):
        temp = self._head
        ll_data = []
        while temp.next is not None:
            ll_data.append(temp.value)
            temp = temp.next
        ll_data.append(temp.value)
        return ll_data
       

if __name__ == "__main__":
    ll = Queue()
    ll.enqueue(5)
    ll.enqueue(10)
    ll.enqueue(11)
    print(ll.dequeue())
    ll.traverse()


        