from unittest import TestCase, main
from sort import sort_arr
import random


class SortArrayTest(TestCase):
    def test_empty_array(self):
        self.assertEqual(
            sort_arr([]),
            []
        )
        self.assertEqual(
            sort_arr(None),
            []
        )

    def test_one_item_array(self):
        self.assertEqual(
            sort_arr([0]),
            [0]
        )

    def test_no_array(self):
        with self.assertRaises(TypeError) as e:
            sort_arr(1234)

    def test_rand_array(self):
        for _ in range(1000):
            arr = [random.randint(-999999999, 999999999) for i in range(random.randint(1, 1000))]
            self.assertEqual(sort_arr(arr), sorted(arr))


if __name__ == '__main__':
    main()
