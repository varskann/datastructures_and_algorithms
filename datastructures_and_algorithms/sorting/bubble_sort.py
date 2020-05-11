__author__ = "Kanishk Varshney"
__data__ = "06-May-2020"

import inspect

def sort(array):
    """Sort array using Bubble sort

    Logic: 
        Keep swapping the adjacent elements of the arary
    Intuition: 
        As the name suggests, it moves by moving lightest(smallest) bubble to top
            - Keep scanning from bottom of bubbles to the current bubble
            - To keep bringing the smalles bubble to top
                - Keep comparing the bubble at bottom with the one on just top of it
                - If bottom bubble is lighter move it up / swap
                - Else, lighter bubble stays on top and keeps moving upwards
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
        for j in range(len(array)-1, i, -1):
            if array[j] < array[j-1]:
                ## Move the lighter bubble up
                _temp = array[j]
                array[j] = array[j-1]
                array[j-1] = _temp
            
    return array
    
if __name__ == "__main__":
    (inspect.getdoc(sort))
    print(sort([2,3,6,5,4,1,-1])) 
