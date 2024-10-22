import numpy as np
# Question 4

def RotateX(theta):
    Rx= np.array([[1, 0, 0],
                  [0, np.cos(theta), -np.sin(theta)],
                  [0, np.sin(theta), np.cos(theta)]])
    return Rx

def RotateY(theta):
    Ry = np.array([[np.cos(theta), 0, np.sin(theta)],
                   [0, 1, 0],
                   [-np.sin(theta), 0, np.cos(theta)]])
    return Ry

def RotateZ(theta):
    Rz = np.array([[np.cos(theta), -np.sin(theta), 0],
                   [np.sin(theta), np.cos(theta), 0],
                   [0, 0, 1]])
    return Rz

# Question 5
def Euler(theta1, theta2, theta3, turn1 ='x', turn2 = 'y', turn3 = 'z'): # this is in order R sub(x,y,z)
    turnOrder = [(turn3, theta3), (turn2, theta2), (turn1, theta1)]
    myMatrix = np.array([[1,0,0],
                         [0,1,0],
                         [0,0,1]])
    
    for turn, theta in turnOrder:
        match turn:
            case 'x':
                myMatrix = myMatrix @ RotateX(theta)
            case 'y':
                myMatrix = myMatrix @ RotateY(theta)
            case 'z':
                myMatrix = myMatrix @ RotateZ(theta)
            case _:
                print(f'Euler angle, Turn order not allowed: {turn}')
    
    return myMatrix 

def RPY(theta1, theta2, theta3):
    R_x = RotateX(theta1)  
    R_y = RotateY(theta2)  
    R_z = RotateZ(theta3) 
    
    return R_z @ R_y @ R_x


# Question 6
def computeDH(a, alpha, d, theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

def FK(DH):
    n = len(DH) 
    A = np.eye(4) 
    
    for i in range(n):
        theta, d, a, alpha = DH[i]  
        A = A @ computeDH(a, alpha, d, theta)
    
    return A

def main():
    phi = np.radians(90)
    theta = np.radians(90)
    psi = np.radians(90)
    print("Question 4:")
    print(f"Rotate X matrix by {np.degrees(phi)}")
    print(RotateX(phi))
    print(f"\nRotate Y matrix by {np.degrees(theta)}")
    print(RotateY(theta))
    print(f"\nRotate Z matrix by {np.degrees(psi)}")
    print(RotateZ(psi))
    
    print("\nQuestion 5:")
    print(f"Euler angle (current) Rotate Z,Y,Z by {np.degrees(phi)} {np.degrees(theta)} {np.degrees(psi)}")
    print(Euler(phi, theta, psi, 'z', 'y', 'z'))
    print("\n")
    print(f"RPY angle (fixed) by Z:{np.degrees(phi)} Y:{np.degrees(theta)} X:{np.degrees(psi)}")
    print(RPY(phi, theta, psi))
    
    DH_params = [
        [0, np.pi/2, 5, np.pi/6],  # Joint 1
        [0, np.pi/4, 2, np.pi/3],  # Joint 2
        [1, np.pi/3, 0, np.pi/4]   # Joint 3
        ]
    
    print("\nQuestion 6:")
    print("DH Parameter used:")
    print(" a\talpha\t\td\ttheta")
    print("----------------------------------------------")
    [print(param) for param in DH_params]
    print("\nFoward Kinamatics from DH")
    print(FK(DH_params)) 
    
main()