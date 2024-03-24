
x0 = float(input())
y0 = float(input())
x = x0
y = y0
distance_traveled = 0


while True:
  
  distance = float(input("Enter the distance to travel: "))

  
  if distance <= 0:
    break

  
  if distance <= 25:
    y += distance
    
  elif distance <= 50:
    y -= distance
    
  elif distance <= 75:
    x += distance
    
  else:
    x -= distance
    

  
  distance_traveled += distance


import math
final_distance = math.sqrt((x - x0)**2 + (y - y0)**2)


print("Final Coordinates: (%.2f, %.2f)" % (x, y))
print("Total Distance Traveled: %.2f" % distance_traveled)
print("Straight Line Distance: %.2f" % final_distance)
