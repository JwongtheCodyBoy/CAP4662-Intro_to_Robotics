import numpy as np

def calculate_euler_angles(R):
    r11 = R[0, 0]
    r21 = R[1, 0]
    r31 = R[2, 0]
    r32 = R[2, 1]
    r33 = R[2, 2]
    
    # Calculate yaw, pitch, and roll
    gamma = np.arctan2(r21, r11)  # Yaw
    beta = np.arctan2(-r31, np.sqrt(r32**2 + r33**2))  # Pitch
    alpha = np.arctan2(r32, r33)  # Roll
    
    return alpha, beta, gamma

# Provided rotation matrix
R = np.array([[-0.0668266,  -0.33332244, -0.94044157],
[-0.08033315,  0.94128604, -0.32791338],
 [ 0.99452541,  0.05363529, -0.08967979]])

alpha, beta, gamma = calculate_euler_angles(R)

# Convert radians to degrees for better interpretability
alpha_deg = np.rad2deg(alpha)
beta_deg = np.rad2deg(beta)
gamma_deg = np.rad2deg(gamma)

print(f"Roll (α): {alpha_deg:.2f} degrees")
print(f"Pitch (β): {beta_deg:.2f} degrees")
print(f"Yaw (γ): {gamma_deg:.2f} degrees")
