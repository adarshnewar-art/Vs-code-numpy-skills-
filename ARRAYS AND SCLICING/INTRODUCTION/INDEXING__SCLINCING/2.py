import numpy as np
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

# Single row
print(matrix[0])           # [1 2 3 4] - first row

# Multiple rows
print(matrix[0:2])         # first two rows (2D output)

# Single column
print(matrix[:, 0])        # [1 5 9 13] - first column

# Multiple columns
print(matrix[:, 1:3])      # 2nd and 3rd columns (all rows)

# Both row and column
print(matrix[1:3, 0:2])    # Rows 1-2, Columns 0-1
print(matrix[::2, ::2])    # Alternate rows and columns