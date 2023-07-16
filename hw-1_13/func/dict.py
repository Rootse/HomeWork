import random
import logging


def clean_dict(d: dict) -> None:
    logging.info("Dictionary deletion...")
    d.clear()


def gen_dict() -> dict:
    d = {}
    for i in range(1, 101):
        d[i] = str(random.randint(0, 100))

    for k, v in d.items():
        print(f"key: {k} | value: {v}")

    return d


def get_dict_repeated_values(arr: list, n: int) -> list:
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    print(f"list: {arr} \ndict: {d}")
    return [k for k, v in d.items() if v >= n]