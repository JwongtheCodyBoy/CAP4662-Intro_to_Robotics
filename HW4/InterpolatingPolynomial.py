from RRTPlanner import *

class InterpolatingPolynomial:
    def __init__(self, path, total_time):
        self.path = path
        self.total_time = total_time
        self.num_segments = len(path) - 1
        self.segment_time = total_time / self.num_segments
    
    def calculate_coefficients(self, start, goal, T):
        # Boundary conditions: start and goal angles and zero velocities at both ends
        a0 = start
        a1 = 0
        a2 = (3 * (goal - start)) / T**2
        a3 = (-2 * (goal - start)) / T**3
        return a0, a1, a2, a3

    def interpolate_segment(self, start, goal, T):
        # Generates interpolated angles for each joint in a segment
        coeffs = [self.calculate_coefficients(start[i], goal[i], T) for i in range(6)]
        t_values = np.linspace(0, T, num=12)  # Adjust as needed
        interpolated_points = []
        
        for t in t_values:
            point = [
                coeffs[i][0] + coeffs[i][1]*t + coeffs[i][2]*t**2 + coeffs[i][3]*t**3
                for i in range(6)
            ]
            interpolated_points.append(point)
        
        return interpolated_points

    def execute_path(self):
        for i in range(self.num_segments):
            start = self.path[i]
            goal = self.path[i+1]
            interpolated_points = self.interpolate_segment(start, goal, self.segment_time)
            
            for point in interpolated_points:
                move_arm(point)
                time.sleep(0.05)  # Adjust timing if necessary
                
                
sim.startSimulation()
# Usage example
start_pos = np.array([0, -90, 90, 0, 90, 0])  # example start configuration in degrees
start_pos = np.array([0, -0, 0, 0, 0, 0])  # example start configuration in degrees
goal_pos = np.array([45, 45, 45, 45, 45, 0])  # example goal configuration in degrees
rrt_planner = RRTPlanner(start=start_pos, goal=goal_pos)

# path will be list of angles in radians
path = rrt_planner.plan()

move_arm(start_pos)

# for it in path:
#     move_arm(it)
#     time.sleep(0.5)


interplatingPoly = InterpolatingPolynomial(path, 1)

interplatingPoly.execute_path()

sim.stopSimulation()
print ('Program ended')
