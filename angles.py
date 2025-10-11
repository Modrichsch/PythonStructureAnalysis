import math
x = 40
y = 25
z = 0
angles = []
mag = math.sqrt(x**2 + y**2 + z**2)
angles.append(math.acos(x/mag)/math.pi)
angles.append(math.acos(y/mag)/math.pi)
angles.append(math.acos(z/mag)/math.pi)

print(angles)