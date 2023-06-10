def f(str1: str, str2: str) -> bool:
    for i in range(len(str1) - len(str2) + 1):
        for j in range(len(str2) - 1, -1, -1):
            if str1[i + j] != str2[j]:
                break
            elif j == 0:
                return True
    return False


if __name__ == '__main__':
    print(f("😾", "😾 "))
    print(f("2221😾2", "2212"))
    print(f("22212", ""))
    print(f("", "12345"))
    print(f("12345", "244"))
    print(f("22212", "2212"))
    print(f("12345", "234"))
    print(f("12345", "235"))
    print(f("12345", "2"))
