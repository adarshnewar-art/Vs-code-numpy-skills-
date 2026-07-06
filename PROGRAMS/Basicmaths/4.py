# write the program to show the uses of the trignometric functions in numpy:
import numpy as np
# Create an array of angles in radians
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
# Calculate the sine of each angle
sine_values = np.sin(angles)
# Calculate the cosine of each angle
cosine_values = np.cos(angles)
# Calculate the tangent of each angle
tangent_values = np.tan(angles)
print("Angles (radians):", angles)
print("Sine values:", sine_values)
print("Cosine values:", cosine_values)
print("Tangent values:", tangent_values)