from os import walk
from os.path import join, splitext
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def draw_square(img_path: str) -> None:
    text = "Hello,\nWorld!"

    with Image.open(img_path) as img:
        img = img.filter(ImageFilter.GaussianBlur(10))

        draw = ImageDraw.Draw(img)
        width, height = img.size
        square_size = min(width, height) // 5
        left = (width - square_size) // 2
        top = (height - square_size) // 2
        right = left + square_size
        bottom = top + square_size
        draw.rectangle((left, top, right, bottom), outline="white", width=10)

        font_path = get_files('.', 'ttf')[0]
        font_size = min(width, height) // 20
        font = ImageFont.truetype(font_path, font_size)
        textwidth, textheight = draw.textsize(text, font=font)
        x = (img.width - textwidth) / 2
        y = (img.height - textheight) / 2
        draw.text((x, y), text, fill="white", font=font)

        img.save(img_path)


def get_files(directory_path: str, file_extension: str) -> list:
    files_list = []

    for root, _, files in walk(directory_path):
        for file in files:
            if file.endswith(file_extension):
                files_list.append(join(root, file))

    return files_list


def convert_img(from_extension: str, to_extension: str) -> list:
    images = get_files('.', from_extension)
    new_images = []
    if not images:
        return new_images

    for imag in images:
        new_image = f"{splitext(imag)[0]}.{to_extension}"

        with Image.open(imag) as img:
            img.save(new_image)

        new_images.append(new_image)

    return new_images
