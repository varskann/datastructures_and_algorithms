

import unittest
import random

from datastructures_and_algorithms import __version__
from datastructures_and_algorithms.sorting import (
    # bubble_sort,
    insertion_sort,
    # selection_sort,
    # merge_sort,
    # quick_sort,
    # counting_sort,
    # bucket_sort,
    # shell_sort,
    # heap_sort,
    # brick_sort,
    # tim_sort,
    # cocktail_sort,
    # gnome_sort
)

def test_version():
    assert __version__ == '0.1.0'

class TestSortingAlgorithm:
    def test_test_setup(self):
        self.assertIsNotNone(getattr(self, 'sort', None))
        self.assertIsNotNone(getattr(self, 'inplace', None))
        self.assertIsNotNone(getattr(self, 'alph_support', None))

    def _check_sort_list(self, arr, expected):
        cp_arr = list(arr)
        sarr = self.sort(cp_arr)

        self.assertTrue(
            isinstance(sarr, list), 'weird result type: ' + str(type(sarr)))
        self.assertEqual(len(sarr), len(arr))
        self.assertEqual(sarr, expected)
        if self.inplace:
            self.assertTrue(cp_arr is sarr, 'was not inplace')
        else:
            self.assertTrue(cp_arr is not sarr, 'was inplace')
            self.assertEqual(cp_arr, arr, 'inplace modified list')

    def _check_sort_alph(self, inp, expected):
        if not self.alph_support:
            return

        self._check_sort_list(list(inp), list(expected))

    def test_sort_empty(self):
        self._check_sort_list([], [])

    def test_sort_single(self):
        self._check_sort_list([5], [5])

    def test_sort_single_alph(self):
        self._check_sort_alph('a', 'a')

    def test_sort_two_inorder(self):
        self._check_sort_list([1, 2], [1, 2])

    def test_sort_two_outoforder(self):
        self._check_sort_list([2, 1], [1, 2])

    def test_sort_5_random_numeric(self):
        arr = list(range(5))
        random.shuffle(arr)
        self._check_sort_list(arr, list(range(5)))

    def test_sort_15_random_numeric(self):
        arr = list(range(15))
        random.shuffle(arr)
        self._check_sort_list(arr, list(range(15)))

    def test_sort_5_random_alph(self):
        arr = ['a', 'b', 'c', 'd', 'e']
        random.shuffle(arr)
        self._check_sort_alph(''.join(arr), 'abcde')

    def test_sort_15_random_alph(self):
        arr = [chr(ord('a') + i) for i in range(15)]
        exp = ''.join(arr)
        random.shuffle(arr)
        self._check_sort_alph(''.join(arr), exp)


class TestInsertionSort(TestSortingAlgorithm):
    inplace = True
    alph_support = True

    @staticmethod
    def sort(arr):
        return insertion_sort.sort(arr)
