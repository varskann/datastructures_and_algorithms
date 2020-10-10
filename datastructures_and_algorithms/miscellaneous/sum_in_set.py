__author__ = "Kanishk Varshney"
__data__ = "04-Oct-2020"

import inspect
from datastructures_and_algorithms.sorting.merge_sort import sort as merge_sort

def binary_search(array, x):
    """Binary search for x in the array

    Arguments:
        array {list} -- sorted array
        x {-} -- element to be searched
    Returns:
        boolean - True, if x is found in array. Else, False
    """
    if len(array) < 1:
        return False
    elif len(array) == 1:
        if array[0] == x:
            return True
        else:
            return False
    else:
        _mid = int(len(array) / 2)
        _mid_element = array[_mid]
        if _mid_element == x:
            return True
        else:
            if _mid_element < x:
                return binary_search(array[_mid+1:], x)
            else:
                return binary_search(array[:_mid], x)
        
    return _mid
        

def sum_in_set(array, x):
    """Search if any two elements in arary sum exactly x

    Arguments:
        array {list} -- query array
        x {int} -- sum value to be searched for
    """
    _sorted_array = merge_sort(array)
    for i in range(len(_sorted_array)):
        _x1 = _sorted_array[i]
        if binary_search(_sorted_array[i+1:], x-_x1):
            return True

    return False

def sum_in_set_linear(array, x):
    """Search if any two elements in array sum exactly x

    We will maintain a set, whose lookup will be O(1), to keep track of traversed elements
    Args:
        array ([type]): [description]
        x ([type]): [description]
    """

    s = set() 
    for i in range(len(array)):
        diff = x - array[i]
        if diff in s:
            return True
        s.add(array[i])
    return False
    
if __name__ == "__main__":
    print(sum_in_set([2,3,6,5,4,1,-1], 9)) 
