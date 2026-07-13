# Taking another example with 2D array and addition with 1D array of broadcasting in numpy library
import numpy as np
# Create a 2D array of values
values_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Create a 1D array of values
values_1d = np.array([10, 20, 30])
# Perform broadcasting operation
result = values_2d + values_1d
# Print the results
print("Original 2D array:\n", values_2d)
print("1D array:\n", values_1d)
print("Result after broadcasting:\n", result)
