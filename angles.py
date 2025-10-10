import math
x = -15
y = 35
z = -25
angles = []
mag = math.sqrt(x**2 + y**2 + z**2)
angles.append(math.acos(x/mag)/math.pi)
angles.append(math.acos(y/mag)/math.pi)
angles.append(math.acos(z/mag)/math.pi)

print(angles)