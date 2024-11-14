import sys
import numpy as np
sys.path.append('zmqRemoteApi')
import math
import time
from zmqRemoteApi import RemoteAPIClient



print ('Program started')
# connect to the coppelia scene
client = RemoteAPIClient()
if client != -1:
    print ('Connected to remote API server')
else:
    print ('Failed connecting to remote API server')
    sys.exit('Could not connect to Coppelia')


sim = client.getObject('sim')
# get the handles of arm joints
arm_handle = sim.getObject('/UR5')
armjoint1_handle = sim.getObject('/UR5/joint')
armjoint2_handle = sim.getObject('/UR5/joint/joint')
armjoint3_handle = sim.getObject('/UR5/joint/joint/joint')
armjoint4_handle = sim.getObject('/UR5/joint/joint/joint/joint')
armjoint5_handle = sim.getObject('/UR5/joint/joint/joint/joint/joint')
armjoint6_handle = sim.getObject('/UR5/joint/joint/joint/joint/joint/joint')
# get the handles of end effector
endeffector_handle = sim.getObject('/UR5/joint/joint/joint/joint/joint/joint/suctionPad')
# get the handles of the tables and boxes
# table1_handle = sim.getObject('/Table1')
# table2_handle = sim.getObject('/Table2')
# box1_handle = sim.getObject('/Box1')
# box2_handle = sim.getObject('/Box2')

# set the arm to position control
sim.setObjectInt32Param(armjoint1_handle, 2000, 1)
sim.setObjectInt32Param(armjoint1_handle, 2001, 1)
sim.setObjectInt32Param(armjoint2_handle, 2000, 1)
sim.setObjectInt32Param(armjoint2_handle, 2001, 1)
sim.setObjectInt32Param(armjoint3_handle, 2000, 1)
sim.setObjectInt32Param(armjoint3_handle, 2001, 1)
sim.setObjectInt32Param(armjoint4_handle, 2000, 1)
sim.setObjectInt32Param(armjoint4_handle, 2001, 1)
sim.setObjectInt32Param(armjoint5_handle, 2000, 1)
sim.setObjectInt32Param(armjoint5_handle, 2001, 1)
sim.setObjectInt32Param(armjoint6_handle, 2000, 1)
sim.setObjectInt32Param(armjoint6_handle, 2001, 1)

# function to control the movement of the arm, the input are the angles of joint1, joint2, joint3, joint4, joint5, joint6. The unit are in degrees
def move_arm(armpose):
    armpose_convert = []
    for i in range(6):
        armpose_convert.append(round(armpose[i]/180 * math.pi,3))
    sim.setJointTargetPosition(armjoint1_handle, armpose_convert[0])
    sim.setJointTargetPosition(armjoint2_handle, armpose_convert[1])
    sim.setJointTargetPosition(armjoint3_handle, armpose_convert[2])
    sim.setJointTargetPosition(armjoint4_handle, armpose_convert[3])
    sim.setJointTargetPosition(armjoint5_handle, armpose_convert[4]) 
    sim.setJointTargetPosition(armjoint6_handle, armpose_convert[5])    
    time.sleep(0.05)

# function to check the collision between each pf the components
def check_collision():
    robotCollection=sim.createCollection(0)
    sim.addItemToCollection(robotCollection, sim.handle_tree, arm_handle, 0)
    result = sim.checkCollision(robotCollection, sim.handle_all)[0]
    if result == 0:       
        return 0
    else:
        print('Collision detected!')
        return 1

# you do not need to modify the code above
sim.startSimulation()
# move arm to a certain pose
# move_arm([30, 30, 30, 30, 30, 30])
# # read the position and orientation of the end-effector
# position = sim.getObjectPosition(endeffector_handle, sim.handle_world)
# orientation = sim.getObjectOrientation(endeffector_handle, sim.handle_world)
# orientation[0] = orientation[0] / math.pi * 180
# orientation[1] = orientation[1] / math.pi * 180
# orientation[2] = orientation[2] / math.pi * 180
# print(position, orientation)
# # print the collision checking result, 1 means there is collision, 0 means no collision
# print(check_collision())
# input('haha')

# sim.stopSimulation()


# print ('Program ended')


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


# Usage example
start_pos = np.array([0, -90, 90, 0, 90, 0])  # example start configuration in degrees
start_pos = np.array([0, -0, 0, 0, 0, 0])  # example start configuration in degrees
goal_pos = np.array([45, 45, 45, 45, 45, 0])  # example goal configuration in degrees
rrt_planner = RRTPlanner(start=start_pos, goal=goal_pos)

# path will be list of angles in radians
path = rrt_planner.plan()

move_arm(start_pos)

for it in path:
    move_arm(it)
    time.sleep(0.5)

sim.stopSimulation()
print ('Program ended')
