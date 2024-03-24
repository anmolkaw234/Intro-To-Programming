import math

def square(x):
  return x**2

def f_prime(x, target):
  return 2*x

def find_square_root(f, f_prime, x0, target):
  for i in range(100):
    x1 = x0 - (f(x0) - target)/f_prime(x0, target)
    if abs(f(x1) - target) < 0.2:
      return x1
    x0 = x1
  print("Square root not found after 100 iterations")

target = float(input("Enter the target number: "))
x0 = float(input("Enter initial guess: "))
sqrt = find_square_root(square, f_prime, x0, target)
print("Square root found:", sqrt)