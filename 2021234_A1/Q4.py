import math
def distance_covered(a, b, delta):
  distance = 0
  t = a
  while t < b:
    arg = 140000/(140000 - 2100 * t)
    if arg <= 0:
      break
    v1 = 2000 * math.log(arg) - 9.8 * t
    if v1 < 0:
      v1 = 0
    t += delta
    arg = 140000/(140000 - 2100 * t)
    if arg <= 0:
      break
    v2 = 2000 * math.log(arg) - 9.8 * t
    if v2 < 0:
      v2 = 0
    avg_v = (v1 + v2) / 2
    distance += avg_v * delta
  return distance

a = float(input())
b = float(input())

print(distance_covered(a, b, 0.25))