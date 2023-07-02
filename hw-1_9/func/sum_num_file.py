import random


def create_file(name: str) -> None:
    with open(f"{name}.txt", "w") as f:
        for _ in range(3):
            f.write(f"{random.randrange(1, 100)}\n")


def sum_num_file(num1: int, num2: int, path: str) -> int:
    sum_num = 0
    try:
        for i in [num1, num2]:
            with open(f"{path}/{i}.txt", "r") as f:
                numbers = [line.rstrip("\n") for line in f]
                if len(numbers) < 3:
                    return f"Error: File {i}.txt contains less than 3 numbers"
                for line in numbers:
                    sum_num += int(line)
    except FileNotFoundError:
        return "Error: File not found"
    except ValueError:
        return "Error: File contains non-numeric data"

    return sum_num
