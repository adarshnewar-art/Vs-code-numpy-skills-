# taking some hard examples of broadcasting and advanced operations in numpy
import numpy as np
# Create a 3D array of values
values_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# Create a 2D array of values
values_2d = np.array([[10, 20], [30, 40]])
# Perform broadcasting operation
result = values_3d + values_2d
# Print the results
print("Original 3D array:\n", values_3d)
print("2D array:\n", values_2d)
print("Result after broadcasting:\n", result)

