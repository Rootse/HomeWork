from unittest import TestCase, main
from func.dict import gen_dict, clean_dict, get_dict_repeated_values


class TestDictionary(TestCase):
    def test_add_pairs(self):
        d = gen_dict()
        self.assertEqual(len(d), 100)
        clean_dict(d)
        self.assertFalse(d)

    def test_read_values(self):
        d = gen_dict()
        for key in d.keys():
            self.assertEqual(d[key], d.get(key))
        clean_dict(d)
        self.assertFalse(d)


class TestGetRepeatedValues(TestCase):
    def test_get_repeated_values(self):
        lst = [1, 2, 3, 4, 5] * 20
        n = 5
        self.assertEqual(get_dict_repeated_values(lst, n), [1, 2, 3, 4, 5])

    def test_equal_list(self):
        lst = []
        n = 0
        self.assertEqual(get_dict_repeated_values(lst, n), [])


if __name__ == '__main__':
    main()
