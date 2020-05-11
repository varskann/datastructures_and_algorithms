__author__ = "Kanishk Varshney"
__data__ = "07-May-2020"

import inspect

def merge_and_count(array1, array2):
    """merge two arrays in sorted order and count inversions done

    Arguments:
        array1 {list} -- 
        array2 {list} -- 

    Returns:
        list -- merged array
    """
    out_array = []
    num_inversions = 0
    i = j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            out_array.append(array1[i])
            i += 1
        else:
            num_inversions += len(array1[i:])
            out_array.append(array2[j])
            j += 1

    out_array.extend(array1[i:])
    out_array.extend(array2[j:])

    return out_array, num_inversions


def count_inversions(array):
    """
    Logic: 
        Count number of inversions in an array
    Intuition: 
        - While merging, count the number of inversions done to merge
        - i.e., # Count of elements in left array g.t. element of right array for each element of right array
    Time Complexity:
        Best case: O(nlogn)
        Average case: O(nlogn)
        Worst case: O(nlogn)
    
    Arguments:
        array {list} -- input array to count inversions in

    Returns:
        list -- sorted output array
        int -- Number of inversions in array
    """  
    if len(array) <= 1:
        return array, 0

    mid = len(array)//2
    
    _array_left, _count_left = count_inversions(array[:mid])
    _array_right, _count_right = count_inversions(array[mid:])
    
    _array_merge, _count_merge = merge_and_count(_array_left, _array_right)
    
    return _array_merge, _count_left + _count_right + _count_merge
         
if __name__ == "__main__":
    print(count_inversions([10, 9, 8, 7, 6, 5, 4, 3, 2,1]))
