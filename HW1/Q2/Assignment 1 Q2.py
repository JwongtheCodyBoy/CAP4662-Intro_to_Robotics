import numpy as np

# Matrix Multiplications
def MatrixMulti(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Matrix dimensions do not match for multiplication")
    return np.dot(A, B)

# Vector Cross Product
def VectorCross(p1, p2):
    rp1 = p1.reshape(3,)
    rp2 = p2.reshape(3,)

    if rp1.shape[0] != 3 or rp2.shape[0] != 3:
        raise ValueError("Vectors must be 3-dimensional for cross product")
    return np.cross(rp1, rp2).reshape(3,1)

# Inversing Matrixs
def InverseMat(A):
    return np.linalg.inv(A)

# Transposing Matrixs
def TransposeMat(A):
    return A.T

# Function that does test cases
def main(): 
    alpha = np.radians(45)
    beta = np.radians(-15)

    A =np.array([[np.cos(alpha), -np.sin(alpha), 0],
                [np.sin(alpha),  np.cos(alpha),  0],
                [0, 0, 1]]) 

    B =np.array([[np.cos(beta), -np.sin(beta), 0],
                [np.sin(beta),  np.cos(beta),  0],
                [0, 0, 1]]) 

    p = np.array([[0],[1],[2]])

    # 4 Other Matrices, completing A1-A7 
    A4 =np.array([[np.cos(alpha), 0, np.sin(alpha)],
                [0,  1,  0],
                [-np.sin(alpha), 0, np.cos(alpha)]]) 
    
    A5 =np.array([[1, 0, 0],
                [0 ,np.cos(alpha), -np.sin(alpha)],
                [0, np.sin(alpha),  np.cos(alpha)]])
    
    A6 =np.array([[np.cos(beta), 0, np.sin(beta)],
                [0,  1,  0],
                [-np.sin(beta), 0, np.cos(beta)]]) 
    
    A7 =np.array([[1, 0, 0],
                [0 ,np.cos(beta), -np.sin(beta)],
                [0, np.sin(beta),  np.cos(beta)]])
     

    # Matrix test cases
    p1 = np.array([[-1 / (2 ** 0.5)],[1 / (2 ** 0.5)],[2]]) #vector Ap
    p2 = np.array([[1 / (2 ** 0.5)],[1 / (2 ** 0.5)],[2]])  #vector Bp

    AB = MatrixMulti(A,B)
    Ap = MatrixMulti(A,p)
    Atp = MatrixMulti(TransposeMat(A), p)
    InvAp = MatrixMulti(InverseMat(A), p)

    p1xp2 = VectorCross(p1,p2)
    p1tp2 = MatrixMulti(TransposeMat(p1),p2)

    # Print resulted matrix (A1-A3)
    print(f"For Alpha = {np.degrees(alpha)} and Beta = {np.degrees(beta)}")
    print(f"First Matrix A:\n{A}\n")
    print(f"Second Matrix B:\n{B}\n")
    print(f"Third Matrix AB:\n{AB}\n")

    # Printing 4 Other Matrices (A4-A7)
    print(f"\nPrinting 4 Other Matrices (A4 - A7)")
    print(f"Matrix A4:\n{A4}\n")
    print(f"Matrix A5:\n{A5}\n")
    print(f"Matrix A6:\n{A6}\n")
    print(f"Matrix A7:\n{A7}\n")

    # Print resulted Vectors
    print(f"Vector Ap:\n{Ap}\n")
    print(f"Vector A Transposed p:\n{Atp}\n")
    print(f"Vector A inversed p:\n{InvAp}\n")
    print(f"Vector p1xp2:\n{p1xp2}\n")
    print(f"Vector p1tp2:\n{p1tp2}\n")


main()