from unittest import TestCase, main
from create_cat_from_file import create_cat_from_file


class TestFunctions(TestCase):
    def test_cat_from_file(self):
        cats1 = create_cat_from_file("test_files/cats1.txt", "r", encodings="utf-8")
        self.assertEqual(len(cats1), 3)
        self.assertEqual(cats1[0].name, "Barsik")
        self.assertEqual(cats1[0].weight, 5.0)
        self.assertEqual(cats1[0].purring_frequency, 75)

        self.assertEqual(cats1[1].name, "Murzik")
        self.assertEqual(cats1[1].weight, 3.5)
        self.assertEqual(cats1[1].purring_frequency, 100)

        self.assertEqual(cats1[2].name, "Pushok")
        self.assertEqual(cats1[2].weight, 4.2)
        self.assertEqual(cats1[2].purring_frequency, 80)

        self.assertEqual(cats1[2].name, "Pushok")
        self.assertEqual(cats1[2].weight, 4.2)
        self.assertEqual(cats1[2].purring_frequency, 80)

        cats2 = create_cat_from_file("test_files/cats2.txt", "r", encodings="utf-8")
        self.assertEqual(cats2, "Invalid line: Fluffy 5 efes")

        cats3 = create_cat_from_file("test_files/cats3.txt", "r", encodings="utf-8")
        self.assertEqual(cats2, "Invalid line: Felix fe 100")


if __name__ == '__main__':
    main()
