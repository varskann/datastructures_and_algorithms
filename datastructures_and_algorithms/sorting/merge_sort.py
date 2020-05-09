__author__ = "Kanishk Varshney"
__data__ = "07-May-2020"

import inspect

def merge(array1, array2):
    """merge two arrays in sorted order.

    Arguments:
        array1 {list} -- 
        array2 {list} -- 

    Returns:
        list -- merged array
    """
    out_array = []
    i = j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            out_array.append(array1[i])
            i += 1
        else:
            out_array.append(array2[j])
            j += 1

    out_array.extend(array1[i:])
    out_array.extend(array2[j:])

    return out_array


def sort(array):
    """
    Logic: 
        Sort Merge small sub-arrays
    Intuition: 
        - You divide the work to two people, 
        - Two sub-parts sort the sub-arrays,
        - You merge the sorted output returned by 
            - Insert it at its sorted position 
    Time Complexity:
        Best case: O(nlogn)
        Average case: O(nlogn)
        Worst case: O(nlogn)
    Inplace: 
        Sorts entries in same array - False
    Stable:
        Equal elements will maintain order as in input array - True 
    
    Arguments:
        array {list} -- input array to be sorted

    Returns:
        list -- sorted output array
    """  
    if len(array) <= 1:
        return array

    mid = len(array)//2
    
    return merge(sort(array[:mid]), sort(array[mid:]))
        
if __name__ == "__main__":
    print(inspect.getdoc(sort))
    print(sort([2,3,6,5,4,1,-1]))
