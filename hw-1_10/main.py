from func.files_and_dirs import remove_directory, get_files_and_dirs
from os import getcwd


def main():
    pwd = getcwd()
    res = get_files_and_dirs(f'{pwd}', '.py', False)
    print(res)

    res = remove_directory('/Users/mac/PycharmProjects/HW/test/')
    print(res)


if __name__ == '__main__':
    main()

