__author__ = "Kanishk Varshney"
__data__ = "04-Oct-2020"

"""
Stack  Class 
"""
import random
from typing import List, Any

class Node():
    def __init__(self, _value: Any, _next=None):
        self.value = _value
        self.next = _next

class Stack():
    """LIFO
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def push(self, _value: Any):
        temp = self.head
        self.head = Node(_value)
        self.head.next = temp

       
    def pop(self) -> Any:
        _value = self.head.value
        self.head = self.head.next
        if self.is_empty():
            self.tail = None
        return _value

    def traverse(self):
        temp = self.head
        ll_data = []
        while temp.next is not None:
            ll_data.append(temp.value)
            temp = temp.next
        ll_data.append(temp.value)
        print("-->".join(list(map(str, ll_data))))
        return ll_data
       

if __name__ == "__main__":
    ll = Stack()
    ll.push(5)
    print(ll.pop())
    ll.push(10)
    ll.push(11)
    ll.push(12)

    print(ll.pop())
    ll.traverse()


        