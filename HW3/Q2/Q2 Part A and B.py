import numpy as np
from random import randint

list_of_angles = []

# Part A
def computeDH(a, alpha, d, theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

def FK(DH):
    n = len(DH) 
    A =np.array([               # when UR5e in sim set to (0,0,0) and 0 oreintation, gripper is facing -x and -y from world origin so fix by changing first matrix 
        [-1, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]) 
    # np.eye(4) 
    
    for i in range(n):
        theta, a, d, alpha = DH[i]  
        A = A @ computeDH(a, alpha, d, theta)
    
    return A

def PartB(DH):
    for it in range(10):
        t = randint(-60,60)
        list_of_angles.append(t)
        theta = np.deg2rad(t)
        copyDH = [
                [row[0]-theta if i == 0 else val for i, val in enumerate(row)]
                for row in DH
            ] 
        
        # print (f"\n{DH}\n\n{copyDH}\n")
        FK_mtr = FK(copyDH)
        
        print(f"Random Matrix {it + 1}, using theta: {t} in degrees, {theta} in radians")
        print(FK_mtr)
        print()


# Testing using deg = 30
# def PartB(DH):
#     t = 30
#     list_of_angles.append(t)
#     theta = np.deg2rad(t)
#     copyDH = [
#             [row[0]-theta if i == 0 else val for i, val in enumerate(row)]
#             for row in DH
#         ] 
    
#     # print (f"\n{DH}\n\n{copyDH}\n")
#     FK_mtr = FK(copyDH)
    
#     print(f"Random Matrix, using theta: {t} in degrees, {theta} in radians for all thetas")
#     print(FK_mtr)
#     print()

def main():
    np.set_printoptions(precision=5, suppress=True)
    print("\n\n\nJonathan Wong Homework 3, Question 2 A and B:\n")
    # Ordering Theta, a, d, alpha,      Radians and m because tahts what was on the slides 
    # from Lect 6, pg 7
    DH_params = [
        [np.pi/2, 0     , 0.0892  , np.pi/2],       # Joint 1
        [np.pi/2, 0.425   , 0     , 0],             # Joint 2
        [0      , 0.392   , 0     , 0],             # Joint 3
        [np.pi/2, 0     , 0.1093  , np.pi/2],       # Joint 4
        [0      , 0     , 0.09475 , -np.pi/2],      # Joint 5
        [0      , 0     , 0.0825  , 0]              # Joint 6
        ]
    
    # PART A
    FK_mtx = FK(DH_params)
    print("Part A: Foward Kinamatics Matrix of UR5e:")
    print(FK_mtx)
    print("\n\n")
    
    
    # PART B
    print("Part B: Randomly generating 10 sets of joint angles:")
    PartB(DH_params)
    print("\n")
    
    print("Angles used for part C:", list_of_angles)
main()