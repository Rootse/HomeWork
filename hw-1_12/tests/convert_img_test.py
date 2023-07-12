from unittest import TestCase, main
from os import remove, getcwd
from os.path import exists
from func.conver_img import get_files, convert_img, draw_square
from PIL import Image, ImageChops


class TestCreateArchive(TestCase):

    def setUp(self):
        self.from_ext = 'jpg'
        self.from_img = './tests/test_img/link-icon-right-side.jpg'
        self.to_ext = 'png'
        self.to_img = './tests/test_img/link-icon-right-side.png'
        self.result = './tests/test_img/result.raw'
        self.dir = '.'
        self.ttf = 'tests/test_font/Roboto-Bold.ttf'
        print(getcwd())

    def tearDown(self):
        images = get_files(self.dir, self.to_ext)

        if not images:
            return

        for i in images:
            remove(i)

    def test_draw_square(self):
        self.assertTrue(exists(self.from_img))
        self.assertTrue(exists(self.ttf))

        self.assertFalse(exists(self.to_img))
        convert_img(self.from_ext, self.to_ext)
        self.assertTrue(exists(self.to_img))

        draw_square(self.to_img)
        with Image.open(self.to_img) as img:
            with Image.open(self.result) as res:

                diff = ImageChops.difference(img, res)

                self.assertFalse(diff.getbbox())


if __name__ == '__main__':
    main()
