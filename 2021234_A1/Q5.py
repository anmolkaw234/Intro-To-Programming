angle_degree = float(input())
x = angle_degree*(3.14/180) #conversion from degree to radians
b = float(input())
tanx = x + ((x**3)/3) + 2*((x**5)/15) + 17*((x**7)/315)
h = b*tanx
l = ((h**2)+(b**2))**(1/2)
print("Height of the pole: " + str(h))
print("Distance to the tip of the pole: " + str(l))
