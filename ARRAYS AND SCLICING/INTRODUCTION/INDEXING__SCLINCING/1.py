# What is slicing in array ?
# ~Slicing in an array refers to the process of extracting a portion of the array by specifying a range of indices.
# ~In Python, slicing is done using the colon (:) operator. The syntax for slicing is array[start:stop:step], where start is the index of the first element to include, stop is the index of the first element to exclude, and step is the number of indices to skip between elements.

# for example let us take the following array:
import numpy as np
# Create an array of values
values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing the array to get elements from index 2 to 5 (excluding index 5)
sliced_values = values[2:5]
# Slicing the array to get every second element from index 0 to 8
sliced_values_step = values[0:9:2]

# Print the results
print("Original values:", values)
print("Sliced values (index 2 to 5):", sliced_values)
print("Sliced values with step (every second element):", sliced_values_step)