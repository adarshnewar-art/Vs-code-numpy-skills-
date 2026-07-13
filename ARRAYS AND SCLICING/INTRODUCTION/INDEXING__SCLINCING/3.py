#  let us atke a real example of slicing in an array using numpy library in python
# Student Marks - 4 students, 3 subjects
import numpy as np
marks = np.array([[85, 90, 78],
                  [92, 88, 95],
                  [76, 81, 89],
                  [88, 92, 85]])

# marks of first student
print(marks[0])              # [85 90 78]

# marks of second student, third subject
print(marks[1, 2])           # 95

# marks of all students, first subject
print(marks[:, 0])           # [85 92 76 88]

# marks of second and third students
print(marks[1:3])            # 2D array

# Last two students, first two subjects
print(marks[-2:, :2])        # Last 2 rows, first 2 columns

# Reverse rows
print(marks[::-1])           # reverse order