# Write a program to show the uses of the statistical functions in numpy:
import numpy as np
# Create an array of values
values = np.array([1, 2, 3, 4, 5])

# Calculate the mean of the values
mean_value = np.mean(values)

# Calculate the median of the values
median_value = np.median(values)

# Calculate the standard deviation of the values
std_deviation = np.std(values)

# Calculate the variance of the values
variance_value = np.var(values)

# Calculate the sum of the values
sum_value = np.sum(values)

# Calculate the minimum and maximum of the values
min_value = np.min(values)
max_value = np.max(values)

# Calculate the index of the minimum and maximum values
min_index = np.argmin(values)
max_index = np.argmax(values)

# Calculate the range of the values
range_value = max_value - min_value

# Print the results
print("Original values:", values)
print("Mean value:", mean_value)
print("Median value:", median_value)
print("Standard deviation:", std_deviation)
print("Variance:", variance_value)
print("Sum:", sum_value)
print("Minimum value:", min_value)
print("Maximum value:", max_value)
print("Index of minimum value:", min_index)
print("Index of maximum value:", max_index)
print("Range:", range_value)