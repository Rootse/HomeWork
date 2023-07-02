from func.sum_num_file import sum_num_file, create_file
from func.create_cat_from_file import create_cat_from_file


def main():
    for i in range(1, 11):
        create_file(f'{i}')

    print(sum_num_file(3, 6, '.'))


if __name__ == '__main__':
    main()
