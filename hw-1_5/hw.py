name = input("Введите свое имя: ")
print("Привет", name)
print("Сумма введеных чисел:", sum(map(float, input(f"{name} введи числа через пробел: ").split())))