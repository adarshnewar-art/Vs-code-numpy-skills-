# Write a pyhton program to add , subtract ,multipy the elements of the two arrays position wise
import numpy as np
# Example arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])
# Add the arrays position wise
added = arr1 + arr2
# Subtract the arrays position wise 
subtracted = arr1 - arr2
# Multiply the arrays position wise
multiplied = arr1 * arr2
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Added array:", added)
print("Subtracted array:", subtracted)
print("Multiplied array:", multiplied)
