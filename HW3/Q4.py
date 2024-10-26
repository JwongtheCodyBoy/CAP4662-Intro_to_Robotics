import numpy as np
from collections import deque

GRID_SIZE = 10
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
wavefront = np.full((GRID_SIZE, GRID_SIZE), 0)

def pathplanning(S, G, n, O):
    global grid
    global wavefront
    
    # Mark the obstacles in the grid
    for i in range(n):
        x1, y1 = O[i][0]
        x2, y2 = O[i][1]
        grid[y1:y2 + 1, x1:x2 + 1] = 1

    start = (S[1], S[0]) 
    goal = (G[1], G[0])    

    wavefront[start] = 2 

    queue = deque([start])  # Start the queue with the start point

    # Directions for neighbors
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),         
        (-1, -1), (-1, 1), (1, -1), (1, 1)         
    ]

    # Perform wavefront 
    while queue:
        current = queue.popleft()
        current_distance = wavefront[current]

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            # Check if the neighbor is within bounds and not an obstacle
            if 0 <= neighbor[0] < GRID_SIZE and 0 <= neighbor[1] < GRID_SIZE:
                if wavefront[neighbor] == 0 and grid[neighbor] != 1:
                    wavefront[neighbor] = current_distance + 1
                    queue.append(neighbor)

    path = []
    current = goal 

    while current != start:
        path.append((current[1], current[0])) 
        neighbors = []

        # Check neighbors to find the next step towards the start
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if 0 <= neighbor[0] < GRID_SIZE and 0 <= neighbor[1] < GRID_SIZE:
                if wavefront[neighbor] > 0:  # Not an obstacle and visited
                    neighbors.append((neighbor, wavefront[neighbor]))

        if not neighbors:
            return []  # No path found

        # Find the neighbor with the minimum distance to start
        current = min(neighbors, key=lambda x: x[1])[0]

    path.append((start[1], start[0])) 
    
    # Reverse the path to get it from start to goal
    path.reverse()  

    return path

def main():
    S = (0, 0) 
    G = (9, 9)
    
    # Obstacles defined by their top-left and bottom-right corners 
    O = [  
        [(2, 2), (4, 4)]
    ]
    n = len(O)

    path = pathplanning(S, G, n, O)
    print("Homework 3, Question 4:")
    print("Path from start to goal:", path)
    
    # Drawing path onto wavefront
    for x, y in path:
        wavefront[x][y] = 1
        
    wavefront[S[0]][S[1]] = -5
    wavefront[G[0]][G[1]] = -6
    print("\nLet -5 represent the start, -6 represent the end, and 1s represent the path:\n")
    print(wavefront)

main()
