import math

nodes = [(0,0.5,0), #3
         (0,0.5,0.5), #3'
         (0.3,0.5,0), #9
         (0.3,0.5,0.5), #9'
         (0.35,0.85,0.25)] #10

force_dict = {
    -1: -3,
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
calc_forces = [0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 0,0, 0,0, 0,0, 0,0, -3] #1-20 and the last one "-1" is force F
#angles are between 0 and 0.5pi, where 0 is horizontal and the pi is left out for clear comparison.
# cos(a) will be the horizontal component and sin(a) the vertical
angle_dict = {
    -1: [0.5, 0, 0.5],
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
    17: [0.13427118575450062, 0.4514102096524711, 0.3758747875120568],
    18: [0.1778076844893528, 0.3221923155106473, 0.5],
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

def forceX(mF, new):
    Fx = 0
    for i in range(len(mF)):
        Fx += calc_forces[mF[i]]*math.cos(angle_dict[mF[i]][0]*math.pi)
    if Fx < 0.01:
        Fx = 0
    return Fx

def forceY(mF, new):
    Fy = 0
    for i in range(len(mF)):
        Fy += calc_forces[mF[i]]*math.cos(angle_dict[mF[i]][1]*math.pi)
    return Fy

def solve_joint(mForces, newForces, kg):
    if len(newForces) > 2:
        print("too many unknowns!")
        return
    #sum of forces in X
    Fx = forceX(mForces, newForces)
    #sum of forces in Y
    Fy = forceY(mForces, newForces)

    #just to make the code "cleaner" will be replaced by a function that computes the angle instead of getting them from the list
    angleX1 = math.cos(angle_dict[newForces[0]][0]*math.pi)
    angleY1 = math.cos(angle_dict[newForces[0]][1]*math.pi)
    angleX2 = math.cos(angle_dict[newForces[1]][0]*math.pi)
    angleY2 = math.cos(angle_dict[newForces[1]][1]*math.pi)

    if not newForces[1]: #only one unknown, easy case
        T1 = -Fx/(angleX1*kg[0])
        return T1
    elif angleX1: #whether unknown force 1 has an x component
        if not angleX2: #Whether unknown force 2 has an x component
            T1 = -Fx / (angleX1*kg[0])
            T2 = -Fy - T1*angleY1*kg[0]
        elif angleY1: #both forces have an x component and the y sum is needed (most common and elaborate case)
            if angleY2:
                #T1 = -Fx - T2*angleX2
                #T1 = -Fy - T2*angleY2
                T2 = (Fx-Fy)/(angleY2 - angleX2) / kg[1]
                T1 = (-Fx - T2*angleX2*kg[1])/kg[0]
            else:
                T1 = -Fy/angleY1
                T2 = -Fx - T1*angleX1
        else:
            T2 = -Fy/angleY2
            T1 = -Fx - T2*angleX2
    else:
        T2 = -Fx/angleX2
    # sum check
    sum = T1*angleX1 + T2*angleX2 + Fx #should by definition always return 0.  I tested it, it gave -0.115 != 0
    print(sum, " = sum of forces with Fx =", Fx)
    calc_forces[newForces[0]] = T1
    calc_forces[newForces[1]] = T2
    return T1, T2

#sum of forces in joint 5
print(solve_joint([-1], [17, 18], [2, 1]))

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