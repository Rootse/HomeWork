from func.dict import gen_dict, clean_dict, get_dict_repeated_values
import random

def main():
    d = gen_dict()
    clean_dict(d)
    print()

    lst = [random.randint(1, 10) for _ in range(100)]
    n = 9
    print(get_dict_repeated_values(lst, n))


if __name__ == '__main__':
    main()
