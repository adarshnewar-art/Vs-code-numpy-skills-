# now let use see the example of where operstions in numpy library
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 3)
print(result)  # (array([3, 4]),)


# some more examples of where operations in numpy library
arr = np.array([10, 20, 30, 40, 50])
result = np.where(arr > 30)
result1 = np.where(arr < 30)
print(result)  # (array([3, 4]),)
print(result1) # (array([0, 1, 2]),)

