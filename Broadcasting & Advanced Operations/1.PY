# what is broadcasting in python?
# Broadcasting in Python, particularly in the context of NumPy, refers to the ability of NumPy arrays to perform arithmetic operations on arrays of different shapes and sizes. When performing operations between two arrays, NumPy automatically expands the smaller array to match the shape of the larger array, allowing for element-wise operations without the need for explicit looping.
# let's look at an example to illustrate broadcasting with a array and a scalar value
import numpy as np
# Create a 1d array of values
values = np.array([1, 2, 3, 4, 5])
# Create a scalar value
scalar = 10
# Perform broadcasting operation
result = values + scalar
# Print the results
print("Original array:", values)
print("Scalar value:", scalar)
print("Result after broadcasting:", result)