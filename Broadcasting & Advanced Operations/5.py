#  now learning more operation sof broadcasting in numpy library
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# Compare with scalar
print(arr > 3)         # [False False False  True  True]
print(arr == 2)        # [False  True False False False]
print(arr <= 4)        # [ True  True  True  True False]

# more type of examples 
arr = np.array([10, 20, 30, 40, 50, 60])

# Condition create karo
condition = arr > 30
print(condition)       # [False False False  True  True  True]

# Filter apply karo
filtered = arr[condition]
print(filtered)        # [40 50 60]

# Ek line mein
result = arr[arr > 30]
print(result)          # [40 50 60]

