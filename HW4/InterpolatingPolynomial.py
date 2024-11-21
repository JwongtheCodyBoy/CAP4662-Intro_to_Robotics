from RRTPlanner import *

class InterpolatingPolynomial:
    def __init__(self, path, total_time):
        self.path = path
        self.total_time = total_time
        self.num_segments = len(path) - 1
        self.segment_time = total_time / self.num_segments
    
    def Calculate_coefficients(self, start, goal, T):
        a0 = start
        a1 = 0
        a2 = (3 * (goal - start)) / T**2        # Acceleration coeffi
        a3 = (-2 * (goal - start)) / T**3       # Jerk  coeffi
        return a0, a1, a2, a3

    def Interpolate_segment(self, start, goal, T):
        # Generates interpolated angles for each joint in a segment
        coeffs = [self.Calculate_coefficients(start[i], goal[i], T) for i in range(6)]
        t_values = np.linspace(0, T, num=5)
        interpolated_points = []
        
        for t in t_values:
            point = [
                coeffs[i][0] + coeffs[i][1]*t + coeffs[i][2]*t**2 + coeffs[i][3]*t**3
                for i in range(6)
            ]
            interpolated_points.append(point)
        
        return interpolated_points

    def Execute_path(self):
        for i in range(self.num_segments):
            start = self.path[i]
            goal = self.path[i+1]
            interpolated_points = self.Interpolate_segment(start, goal, self.segment_time)
            
            for point in interpolated_points:
                move_arm(point)
                # time.sleep(0.01)
                

# Test Case                
sim.startSimulation()

start_pos = np.array([0, 0, 0, 0, 0, 0])  # example start configuration in degrees
goal_pos = np.array([45, 45, 45, 45, 45, 0])  # example goal configuration in degrees
rrt_planner = RRTPlanner(start=start_pos, goal=goal_pos)

# path will be list of angles in radians
path = rrt_planner.Plan()

move_arm(start_pos)

# for it in path:
#     move_arm(it)
#     time.sleep(0.05)

interplatingPoly = InterpolatingPolynomial(path, 100)

interplatingPoly.Execute_path()

sim.stopSimulation()
print ('Program ended')
