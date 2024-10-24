import numpy as np

def MatrixMulti(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Matrix dimensions do not match for multiplication.")
    return np.dot(A, B)

def VectorCross(p1, p2):
    if p1.shape[0] != 3 or p2.shape[0] != 3:
        raise ValueError("Vectors must be 3-dimensional for cross product.")
    return np.cross(p1, p2)

def InverseMat(A):
    return np.linalg.inv(A)

def TransposeMat(A):
    return A.T

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
    res = MatrixMulti(A,p)


    # print resulted matrix
    print(res)
    print(TransposeMat(A))


main()