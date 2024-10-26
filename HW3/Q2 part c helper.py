import numpy as np

n = ''
while n !='q':
    alpha = float(input('give Alpha: '))
    beta = float(input('give Beta: '))
    gamma = float(input('give Gama: '))
    
    R = np.array([
        [np.cos(alpha) * np.cos(beta), 
         np.cos(alpha) * np.sin(beta) * np.sin(gamma) - np.sin(alpha) * np.cos(gamma), 
         np.cos(alpha) * np.sin(beta) * np.cos(gamma) + np.sin(alpha) * np.sin(gamma)],
         
        [np.sin(alpha) * np.cos(beta), 
         np.sin(alpha) * np.sin(beta) * np.sin(gamma) + np.cos(alpha) * np.cos(gamma), 
         np.sin(alpha) * np.sin(beta) * np.cos(gamma) - np.cos(alpha) * np.sin(gamma)],
         
        [-np.sin(beta), 
         np.cos(beta) * np.sin(gamma), 
         np.cos(beta) * np.cos(gamma)]
    ])
    print()
    print(R)
    print()
    
    n = input('q to quit, else anything else')