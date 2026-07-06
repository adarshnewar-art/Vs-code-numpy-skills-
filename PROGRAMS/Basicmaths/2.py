# Write a program to multiply and divide all the elements of the array with the user given number
import numpy as np
# Example array
arr = np.array([10, 20, 30, 40, 50])
# Get user input
num = float(input("Enter a number to multiply and divide the array elements: "))
# Multiply the array elements by the user input
multiplied = arr * num
# Divide the array elements by the user input
divided = arr / num
print("Original array:", arr)
print("Array after multiplication:", multiplied)
print("Array after division:", divided)