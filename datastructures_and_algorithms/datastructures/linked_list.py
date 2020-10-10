__author__ = "Kanishk Varshney"
__data__ = "04-Oct-2020"

"""
Linked List Class 
"""
import random
from typing import List, Any

class Node():
    def __init__(self, _value: Any, _next=None):
        self.value = _value
        self.next = _next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, _value):
        if self.head is None:
            self.head = Node(_value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(_value)

    def traverse(self):
        temp = self.head
        ll_data = []
        while temp.next is not None:
            ll_data.append(temp.value)
            temp = temp.next
        ll_data.append(temp.value)
        print("-->".join(list(map(str, ll_data))))
        return ll_data

    def search(self, x: int) -> bool:
        temp = self.head
        


    

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(11)
    ll.traverse()

        