from PIL import ImageChops, Image

from func.conver_img import convert_img, draw_square


def main():
    from_ext = "jpg"
    to_ext = "png"

    new_img = convert_img(from_ext, to_ext)

    for img in new_img:
        draw_square(img)


if __name__ == '__main__':
    main()
