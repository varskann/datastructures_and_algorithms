__author__ = "Kanishk Varshney"
__data__ = "06-May-2020"

import inspect

def insert_element(array, x):
    """Insert x at appropriate position in sorted array A, mainitaining the sorted order

    Arguments:
        array {list} -- sorted array/list
        x {_} -- [element to be inserted]
    """
    j = len(array) - 1
    while j >= 0:
        if array[j] <= x:
            break
        j -= 1
    return array[:j+1] + [x] + array[j+1:]


def sort(array):
    """Recursive approach to Insertion sort. Logic and Intuition remains same
    Logic: 
        Insert each element at its appropriate  position by scanning back
    Intuition: 
        Assume a card deck facing down, and you have to arrange/sort cards in your hand
            - You pick one card, 
            - Compare it with cards starting from righmost,
            - Keep moving left till you find appropriate position
            - Insert it at its sorted position 
    Time Complexity:
        Best case: O(n)
        Average case: O(n2)
        Worst case: O(n2)
    Inplace: 
        Sorts entries in same array - True
    Stable:
        Equal elements will maintain order as in input array - True 
    
    Arguments:
        array {list} -- input array to be sorted

    Returns:
        list -- sorted output array
    """ 
    if len(array) == 1:
        return array
    
    return insert_element(sort(array[:-1]), array[-1])
    
if __name__ == "__main__":
    (inspect.getdoc(sort))
    print(sort([2,3,6,5,4,1,-1]))
