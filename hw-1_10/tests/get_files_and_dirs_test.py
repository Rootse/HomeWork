from unittest import TestCase, main
from os import getcwd
from func.files_and_dirs import get_files_and_dirs


class TestGetFilesAndDirs(TestCase):
    def test_get_files_and_dirs(self):
        directory_path = getcwd()
        file_extension = ".txt"
        checkbox = True
        result = get_files_and_dirs(directory_path, file_extension, checkbox)
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)


if __name__ == '__main__':
    main()
