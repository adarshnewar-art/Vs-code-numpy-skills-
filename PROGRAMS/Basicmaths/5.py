# Write a program to show the uses of all the exponential and logarithmic functions in numpy:
import numpy as np
# Create an array of values
values = np.array([1, 2, 3, 4, 5])
# Calculate the exponential of each value
exponential_values = np.exp(values)
# Calculate the natural logarithm of each value
natural_log_values = np.log(values)
# Calculate the base-10 logarithm of each value
base10_log_values = np.log10(values)
print("Original values:", values)
print("Exponential values:", exponential_values)
print("Natural logarithm values:", natural_log_values)
print("Base-10 logarithm values:", base10_log_values)
