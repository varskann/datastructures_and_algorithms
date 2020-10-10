__author__ = "Kanishk Varshney"
__data__ = "04-Oct-2020"

"""
Array Utilities / Helper Functions
"""
import random
from typing import List

def generate_integer_array(l : int, minmax: int = 100, sorted:bool=False) -> List[int]:
    """Generate integer array of Length l
    Array integers are 

    Args:
        l (int): length of requested array
        minmax (int): range of the array elements(from -minmax to + minmax). Defaults to 100.
        sorted (bool, optional): [description]. Defaults to False.

    Returns:
        List[int]: out_list
    """
    out_list = []
    for _ in range(l):
        out_list.append(random.randint(-minmax, minmax))
    return out_list
