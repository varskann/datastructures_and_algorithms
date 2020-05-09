__author__ = "Kanishk Varshney"
__data__ = "06-May-2020"

import inspect

def sort(array):
    """Sort array using Selection sort

    Logic: 
        Select n-smallest element and place it in the nth block of array
    Intuition: 
        Assume a card deck in your hand down, say 1 to 13
            - You scan through whole deck and SELECT smallest card, i.e., 1 
            - Put it at the very first position 
            - Scan through remaining deck and SELECT second smallest card, i.e., 2
            - Put it at the second position
    Time Complexity:
        Best case: O(n2)
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

    for i in range(0, len(array)):
        _min_element = array[i]
        _min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < _min_element:
                _min_element = array[j]
                _min_idx = j
                        
        ## Place the selected element at appropriate position
        _temp = array[_min_idx]
        array[_min_idx] = array[i]
        array[i] = _temp
    
    return array
    
if __name__ == "__main__":
    (inspect.getdoc(sort))
    print(sort([2,3,6,5,4,1,-1]))