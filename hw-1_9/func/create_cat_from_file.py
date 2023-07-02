class Cat:
    def __init__(self, name: str, weight: float, purr_freq: int):
        self.name = name
        self.weight = weight
        self.purr_freq = purr_freq


def create_cat_from_file(file_name: str):
    cats = []
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            try:
                name, weight, purring_frequency = line.strip().split()
                cats.append(Cat(str(name), float(weight), int(purring_frequency)))
            except ValueError:
                print(f"Invalid line: {line.strip()}")
    return cats