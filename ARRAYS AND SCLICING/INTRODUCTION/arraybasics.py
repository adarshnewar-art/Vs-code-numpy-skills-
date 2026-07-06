# What is indexing in array ?
# Indexing in an array refers to the process of accessing individual elements within the array using their position or index. 
# In Python, array indices start from 0, meaning the first element is at index 0, the second element is at index 1, and so on.

# write a python program to demonstrate indexing in an array using numpy:
import numpy as np

# Create an array of values
values = np.array([1, 2, 3, 4, 5])

# Access individual elements using their indices
first_element = values[0]
second_element = values[1]
last_element = values[-1]

# Print the results
print("Original values:", values)
print("First element:", first_element)
print("Second element:", second_element)
print("Last element:", last_element)

# Now indexing can also be used to access elements in multi-dimensional arrays. For example, in a 2D array, you can access elements using two indices: one for the row and one for the column.

import numpy as np
# Create a 2D array of values
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access individual elements using their indices
element_2_3 = matrix[1, 2]  # Access the element in the second row and third column
element_1_1 = matrix[0, 0]  # Access the element in the first row and first column
element_3_2 = matrix[2, 1]  # Access the element in the third row and second column

# Print the results
print("Original matrix:")
print(matrix)
print("Element at row 2, column 3:", element_2_3)
print("Element at row 1, column 1:", element_1_1)
print("Element at row 3, column 2:", element_3_2)