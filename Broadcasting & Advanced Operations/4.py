# taking a real example of broadcasting and advanced operations in numpy
import numpy as np
# Temperature conversion - Celsius to Fahrenheit
celsius = np.array([0, 10, 20, 30, 40])
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)  # [32. 50. 68. 86. 104.]

# Matrix ke sab elements mein ek number add karna
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
matrix_plus_10 = matrix + 10
print(matrix_plus_10)
# [[11 12 13]
#  [14 15 16]]