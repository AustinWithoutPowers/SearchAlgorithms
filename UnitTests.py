import unittest
import SearchAlgorithms as sa

# Declare testing arrays
ARRAY_ONE = [0, 1, 2]
ARRAY_TWO = [4, 1, 2, -3]

# Selection sort tests
class TestSelectionSort(unittest.TestCase):
    def test_basics_asc(self):
        self.assertEqual(sa.selection_sort(ARRAY_ONE), [0, 1, 2])

    def test_basics_desc(self):
        self.assertEqual(sa.selection_sort(ARRAY_ONE, False), [2, 1, 0])

    def test_negative_asc(self):
        self.assertEqual(sa.selection_sort(ARRAY_TWO), [-3, 1, 2, 4])
    
    def test_negative_desc(self):
        self.assertEqual(sa.selection_sort(ARRAY_TWO, False), [4, 2, 1, -3])

class TestInsersionSort(unittest.TestCase):
    def test_basics_asc(self):
        self.assertEqual(sa.insersion_sort(ARRAY_ONE), [0, 1, 2])

    def test_basics_desc(self):
        self.assertEqual(sa.insersion_sort(ARRAY_ONE, False), [2, 1, 0])

    def test_negative_asc(self):
        self.assertEqual(sa.insersion_sort(ARRAY_TWO), [-3, 1, 2, 4])
    
    def test_negative_desc(self):
        self.assertEqual(sa.insersion_sort(ARRAY_TWO, False), [4, 2, 1, -3])

class TestQuickSort(unittest.TestCase):
    def test_basics_asc(self):
        self.assertEqual(sa.quick_sort(ARRAY_ONE), [0, 1, 2])

    def test_basics_desc(self):
        self.assertEqual(sa.quick_sort(ARRAY_ONE, False), [2, 1, 0])

    def test_negative_asc(self):
        self.assertEqual(sa.quick_sort(ARRAY_TWO), [-3, 1, 2, 4])
    
    def test_negative_desc(self):
        self.assertEqual(sa.quick_sort(ARRAY_TWO, False), [4, 2, 1, -3])

class TestMergeSort(unittest.TestCase):
    def test_basics_asc(self):
        self.assertEqual(sa.merge_sort(ARRAY_ONE), [0, 1, 2])

    def test_basics_desc(self):
        self.assertEqual(sa.merge_sort(ARRAY_ONE, False), [2, 1, 0])

    def test_negative_asc(self):
        self.assertEqual(sa.merge_sort(ARRAY_TWO), [-3, 1, 2, 4])
    
    def test_negative_desc(self):
        self.assertEqual(sa.merge_sort(ARRAY_TWO, False), [4, 2, 1, -3])
    
if __name__ == '__main__':
    unittest.main()