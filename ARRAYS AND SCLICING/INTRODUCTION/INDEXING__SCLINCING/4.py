# let us take an array to reverse it using slicing in python and numpy library
import numpy as np
# Create an array of values
values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# Reverse the array
reversed_values = values[::-1]
# Print the results
print("Original array:", values)
print("Reversed array:", reversed_values)