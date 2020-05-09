__author__ = "Kanishk Varshney"
__data__ = "06-May-2020"

import inspect

def sort(array):
    """
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
    for i in range(1, len(array)):
        _current_value = array[i]
        j = i-1
        while j >= 0 and array[j] > _current_value:
            array[j+1] = array[j]
            j -= 1
            
        ## insert array[i] at appropriate position
        array[j+1] = _current_value
    
    return array
    
if __name__ == "__main__":
    (inspect.getdoc(sort))
    print(sort([2,3,6,5,4,1,-1]))