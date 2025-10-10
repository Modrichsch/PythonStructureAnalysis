import math

nodes = [(0,0.5,0), #3
         (0,0.5,0.5), #3'
         (0.3,0.5,0), #9
         (0.3,0.5,0.5), #9'
         (0.35,0.85,0.25)] #10

force_dict = {
    6: 1.716,
    7: 0.098,
    8: 0.136,
    9: -0.966,
    10: -1.682,
    11: 2.459,
    12: -1.726,
    13: 1.825,
    14: 3.2,
    15: -2.507,
    19: 5.143,
    20: -1.366,
}
#angles are between 0 and 0.5pi, where 0 is horizontal and the pi is left out for clear comparison.
# cos(a) will be the horizontal component and sin(a) the vertical
angle_dict = {
    6: [0.5, 0.0, 0.5],
    7: [0.32797913037736937, 0.17202086962263075, 0.5],
    8: [0.6211189415908434, 0.12111894159084333, 0.5],
    9: [0.0, 0.5, 0.5],
    10: [0.0, 0.5, 0.5],
    11: [0.285, 0.435, 0.229],
    12: [0.594897731703665, 0.23749504804274926, 0.2903876877151751],
    13: [0.4631625679551186, 0.2003931591710909, 0.3040867239846964],
    14: [0.12566591637800234, 0.3743340836219976, 0.5],
    15: [0.6068103096969111, 0.22107814162091644, 0.3150767403019983],
    19: [0.0, 0.5, 0.5],
    20: [0.5, 0.5, 0.0]
}

angle : float = 0
position = (0.18,0.8,0.25)
deltaX = 0.0  #fill in the desired value here
deltaY = -0.05  #fill in the desired value here
new_pos = []

new_pos.append(position[0] + deltaX)
new_pos.append(position[1] )#+ deltaY)
new_pos.append(position[2])


def angler(pos2):
    dx = new_pos[0]-pos2[0]
    dy = new_pos[1]-pos2[1]
    return math.atan(dy/dx)

def forceX(i):
    return force_dict[i]*math.cos(angle_dict[i][0]*math.pi)

def forceY(i):
    return force_dict[i]*math.cos(angle_dict[i][1]*math.pi)

def forceZ(i):
    return force_dict[i]*math.cos(angle_dict[i][2]*math.pi)
#sum of forces in joint 10
Fx = 2*forceX(13) + 2*forceX(15) - forceX(19)
print(Fx, " Fx")
Fz = 2*forceZ(13) + 2*forceZ(15) #should be 0 is not right now
Fy = 2*forceY(13) + 2*forceY(15) + forceY(19)
angle = angler(nodes[4])
T14 = math.sqrt(Fx**2 + Fy**2 + Fz**2)
print(T14)

#calculating T11 with joint 3:
Fy = forceY(6)
T11 = Fy/math.cos(angle_dict[11][1]*math.pi)
print(T11)

#sum of forces in joint 4 (y)
for i in range(5):
    angle = angler(nodes[0])
    forceY(12)

#material use:
for y in range(5):
    material = 0 #m
    for i in range(5):
        material += math.dist(new_pos, nodes[i])
    print(material, "meters of material at y =", new_pos[1])
    new_pos[1] += deltaY

#angle calculation automation
for i in range(1):
    pass