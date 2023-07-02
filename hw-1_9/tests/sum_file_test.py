from unittest import TestCase, main
from sum_num_file import sum_num_file, create_file


class SumNumFileTest(TestCase):
    def test_sum_of_numbers(self):
        self.assertEqual(sum_num_file(1, 2, "test_files"), 88)
        self.assertEqual(sum_num_file(2, 3, "test_files"), 145)
        self.assertEqual(sum_num_file(3, 4, "test_files"), "Error: File contains non-numeric data")
        self.assertEqual(sum_num_file(5, 6, "test_files"), "Error: File contains less than 3 numbers")
        self.assertEqual(sum_num_file(6, 7, "test_files"), "Error: File not found")


if __name__ == '__main__':
    main()
