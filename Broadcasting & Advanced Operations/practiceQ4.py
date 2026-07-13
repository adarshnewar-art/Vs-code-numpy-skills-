import numpy as np
marks = np.array([35, 45, 55, 65, 75, 85, 95])

# a) print the number is greater than 50 or not is not print fail else print pass
# b) do 1.5x if the marks is greater than 60 or else make it same 
# c) write even at even and odd at odd index
import numpy as np
marks = np.array([35, 45, 55, 65, 75, 85, 95])

# a) Pass/Fail (np.where )
result_a = np.where(marks > 50, "Pass", "Fail")
print("a)", result_a)
# Output: ['Fail' 'Fail' 'Pass' 'Pass' 'Pass' 'Pass' 'Pass']

# b) 1.5x if > 60, else same (np.where )
result_b = np.where(marks > 60, marks * 1.5, marks)
print("b)", result_b)
# Output: [35.  45.  55.  97.5 112.5 127.5 142.5]

# c) Even/Odd (check numbers, not index)
result_c = np.where(marks % 2 == 0, "Even", "Odd")
print("c)", result_c)
# Output: ['Odd' 'Odd' 'Odd' 'Odd' 'Odd' 'Odd' 'Odd']
