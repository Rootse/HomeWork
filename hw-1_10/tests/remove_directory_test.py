from unittest import main, TestCase
from os import getcwd, mkdir
from os.path import join, exists
from func.files_and_dirs import remove_directory


class TestRemoveDirectory(TestCase):
    def setUp(self):
        self.pwd = getcwd()
        self.dir_path1 = f"{self.pwd}/test_dir1"
        self.dir_path2 = f"{self.dir_path1}/test_dir2"
        mkdir(self.dir_path1)
        mkdir(self.dir_path2)
        with open(join(self.dir_path1, "test_file.txt"), "w") as f:
            f.write("test")

    def tearDown(self):
        remove_directory(self.dir_path1)

    def test_remove_directory(self):
        result = remove_directory(self.dir_path1)
        self.assertFalse(result)
        self.assertTrue(exists(self.dir_path1))

        result = remove_directory(self.dir_path2)
        self.assertTrue(result)
        self.assertFalse(exists(self.dir_path2))

        result = remove_directory('')
        self.assertFalse(result)

        result = remove_directory('/123')
        self.assertFalse(result)


if __name__ == '__main__':
    main()
