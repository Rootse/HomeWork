from os import listdir
from os.path import isfile, join, splitext
from zipfile import ZipFile


def get_files(directory_path: str, file_extension: str) -> list:
    files_list = []
    for item in listdir(directory_path):
        _, extension = splitext(join(directory_path, item))
        if isfile(join(directory_path, item)) and extension.replace('.', '') == file_extension.replace('.', ''):
            files_list.append(join(directory_path, item))
            continue

    return files_list


def zip_extension_file(name: str, file_extension: str) -> None:
    files = get_files('.', file_extension)

    with ZipFile(f'{name}.zip', 'w') as zip:
        for i in files:
            zip.write(i)
