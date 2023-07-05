from os import listdir, remove, rmdir
from os.path import isfile, join, isdir


def get_files_and_dirs(directory_path: str, file_extension: str, checkbox: bool) -> list:
    files_list = []
    dirs_list = []
    for item in listdir(directory_path):
        if isfile(join(directory_path, item)):
            files_list.append(join(directory_path, item))
            continue

        dirs_list.append(join(directory_path, item))
        if checkbox:
            f, d = get_files_and_dirs(join(directory_path, item), file_extension, False)
            files_list.append(f)
            dirs_list.append(d)

    return [files_list, dirs_list]


def remove_directory(directory_path: str) -> bool:
    if not directory_path or not isdir(directory_path):
        return False
    for item in listdir(directory_path):
        if isdir(join(directory_path, item)):
            return False

    for item in listdir(directory_path):
        remove(join(directory_path, item))

    rmdir(directory_path)
    return True
