import random
import time
import coppelia_example

# Define UR5 joint limits (example values; adjust to match your UR5's real limits)
joint_limits = {
    'q1': (-180, 180),
    'q2': (-90, 90),
    'q3': (-180, 180),
    'q4': (-180, 180),
    'q5': (-90, 90),
    'q6': (-360, 360)
}

# Function to generate a random pose within the joint limits
def generate_random_pose():
    return [
        random.uniform(joint_limits['q1'][0], joint_limits['q1'][1]),
        random.uniform(joint_limits['q2'][0], joint_limits['q2'][1]),
        random.uniform(joint_limits['q3'][0], joint_limits['q3'][1]),
        random.uniform(joint_limits['q4'][0], joint_limits['q4'][1]),
        random.uniform(joint_limits['q5'][0], joint_limits['q5'][1]),
        random.uniform(joint_limits['q6'][0], joint_limits['q6'][1])
    ]

def main():
    coppelia_example.sim.startSimulation()

    # Generate and check 100 poses
    free_space_poses = []
    numColi = 0
    for _ in range(100):
        pose = generate_random_pose()
        coppelia_example.move_arm(pose)
        time.sleep(0.5)  # Add a short delay for the movement to complete

        # Check if the pose is collision-free
        if coppelia_example.check_collision() == 0:  # 0 means no collision
            free_space_poses.append(pose)
        else:
            numColi += 1

    # Output poses in free space (collision-free)
    print("Poses in free space (collision-free):")
    for pose in free_space_poses:
        print(pose)

    coppelia_example.sim.stopSimulation()
    print(f'Simulation ended with, {numColi} collisions and {len(free_space_poses)} free space position')

main()