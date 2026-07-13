import numpy as np
arr = np.array([5, 10, 15, 20, 25, 30, 35])

# a) find the number greater than 20
# b) find the number smaller than 15
# c) find elements between 15 and 30
# d) count elements greater than 20

count_greater_than_20 = np.sum(arr > 20)
greater_than_20 = arr[arr > 20]
smaller_than_15 = arr[arr < 15]
between_15_and_30 = arr[(arr > 15) & (arr < 30)]

print("Elements greater than 20:", greater_than_20)
print("Elements smaller than 15:", smaller_than_15)
print("Elements between 15 and 30:", between_15_and_30)
print("Count of elements greater than 20:", count_greater_than_20)
