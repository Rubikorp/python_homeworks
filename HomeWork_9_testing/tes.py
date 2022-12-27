import unittest
from functions import *


class MyTestCase(unittest.TestCase):
    def test_sortArray(self):
        self.assertEqual(sort_array([1, 2, 3, 4, 5]), [2, 1, 4, 3, 5])  # add assertion here

    def test_appendRatting(self):
        self.assertEqual(append_ratting(), [7, 5, 3, 3, 3, 2])

    def test_findSeason(self):
        self.assertEqual(find_season(3), "dict_keys(['весна'])")

    def test_printTypeList(self):
        self.assertEqual(print_type_list([True, 1, 2, "Hello", False]), [bool, int, int, str, bool])

    def test_fullTime(self):
        self.assertEqual(full_time(360), '0:6:0')

    def test_sumCount(self):
        self.assertEqual(sum_count(5), 615)

    def test_findMaxNumberInCount(self):
        self.assertEqual(find_max_number_in_count(675), 7)

    def test_dayResult(self):
        self.assertEqual(day_result(30, 300), '26 день результата')

    def test_deduplication(self):
        self.assertEqual(deduplication(10, 5), 2.0)

    def test_tittleWord(self):
        self.assertEqual(tittle_word('word hello name'), 'Word Hello Name')

if __name__ == '__main__':
    unittest.main()
