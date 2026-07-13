import numpy as np
arr1d = np.array([10, 20, 30])
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# a) add arr1d to arr2d
# b) divide arr2d by arr1d
# c) multiply arr2d by arr1d

added = arr2d + arr1d
divided = arr2d / arr1d
multiplied = arr2d * arr1d

print("Added:\n", added)
print("Divided:\n", divided)
print("Multiplied:\n", multiplied)