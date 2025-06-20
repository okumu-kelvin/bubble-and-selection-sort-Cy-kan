import unittest
from selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):
    def test_sorted_list(self):
        self.assertEqual(selection_sort([1, 2, 3]), [1, 2, 3])

    def test_unsorted_list(self):
        self.assertEqual(selection_sort([3, 1, 2]), [1, 2, 3])

    def test_with_duplicates(self):
        self.assertEqual(selection_sort([4, 2, 4, 3]), [2, 3, 4, 4])

    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])

    def test_single_element(self):
        self.assertEqual(selection_sort([7]), [7])

if __name__ == '__main__':
    unittest.main()
