import math

def f(x):
  return x**3 - 10.5*x**2 + 34.5*x - 35

def f_prime(x):
  return 3*x**2 - 21*x + 34.5

def find_root(f, f_prime, x0):
  for i in range(100):
    x1 = x0 - f(x0)/f_prime(x0)
    if abs(f(x1)) < 0.2:
      return x1
    x0 = x1
  print("Root not found after 100 iterations")

x0 = float(input("Enter initial value of x: "))
root = find_root(f, f_prime, x0)
print("Root found:", root)























