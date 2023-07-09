from unittest import TestCase, main
from os import remove
from os.path import isfile
from func.zip_file import zip_extension_file


class TestCreateArchive(TestCase):

    def setUp(self):
        f = open('test.txt', 'w')
        f.close()

    def tearDown(self):
        remove('test.txt')
        remove('test.zip')

    def test_create_archive(self):
        zip_extension_file('test', '.txt')
        self.assertTrue(isfile('test.zip'))


if __name__ == '__main__':
    main()
