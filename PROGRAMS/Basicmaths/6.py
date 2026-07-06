# Write a program to show the uses of the rounding functions in numpy:
import numpy as np
# Create an array of floating-point numbers
arr = np.array([1.2, 2.5, 3.7, 4.1, 5.9])
# Round the array elements to the nearest integer
rounded = np.round(arr)
# Round the array elements to the nearest integer towards zero
rounded_towards_zero = np.trunc(arr)
# Round the array elements to the nearest integer away from zero
rounded_away_from_zero = np.ceil(arr)
print("Original array:", arr)
print("Rounded array:", rounded)
print("Rounded towards zero:", rounded_towards_zero)
print("Rounded away from zero:", rounded_away_from_zero)
