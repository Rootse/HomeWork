from math_1.math_func import multiplication

def elevation(n: int, degree: int) -> int:
  result = 0
  for i in range(degree):
    result += multiplication(n, n)

  return result
