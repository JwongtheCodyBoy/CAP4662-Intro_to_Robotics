from coppelia_example import *

class RRTPlanner:
    def __init__(self, start, goal, max_iterations=1000, step_size=10, bias_prob=5/50):
        self.start = start
        self.goal = goal
        self.max_iterations = max_iterations
        self.step_size = step_size
        self.bias_prob = bias_prob
        self.tree = {tuple(start): None}  # Store nodes with their parent node for backtracking

    def random_sample(self):
        if np.random.rand() < self.bias_prob:
            return self.goal  # Bias towards the goal
        return np.random.uniform(low=-180, high=180, size=(6,))

    def nearest_node(self, sample):
        return min(self.tree.keys(), key=lambda node: np.linalg.norm(np.array(node) - sample))

    def steer(self, nearest, sample):
        direction = sample - np.array(nearest)
        distance = np.linalg.norm(direction)
        new_config = np.array(nearest) + (direction / distance) * self.step_size if distance > self.step_size else sample
        move_arm(new_config)  # Move the arm to the new configuration
        if check_collision() == 0:
            self.tree[tuple(new_config)] = tuple(nearest)  # Add to tree with parent info
            return new_config
        return None

    def plan(self):
        for _ in range(self.max_iterations):
            sample = self.random_sample()
            nearest = self.nearest_node(sample)
            new_node = self.steer(nearest, sample)
            if new_node is not None:
                if np.linalg.norm(new_node - self.goal) < self.step_size:
                    print("path Found")
                    return self.extract_path(new_node)
        return self.extract_path(new_node)

    def extract_path(self, goal_node):
        path = [goal_node]
        current = tuple(goal_node)
        
        # Backtrack from the goal to the start using parent references
        while current is not None:
            path.append(current)
            current = self.tree[current]
        
        path.reverse()  # To get the path from start to goal
        return path


# sim.startSimulation()

# # Usage example
# start_pos = np.array([0, -90, 90, 0, 90, 0])  # example start configuration in degrees
# start_pos = np.array([0, -0, 0, 0, 0, 0])  # example start configuration in degrees
# goal_pos = np.array([45, 45, 45, 45, 45, 0])  # example goal configuration in degrees
# rrt_planner = RRTPlanner(start=start_pos, goal=goal_pos)

# # path will be list of angles in radians
# path = rrt_planner.plan()

# move_arm(start_pos)

# for it in path:
#     move_arm(it)
#     time.sleep(0.5)

# sim.stopSimulation()
# print ('Program ended')
