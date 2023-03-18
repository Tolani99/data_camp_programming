"""
This code shows how to do a column_stack
using column_stack() function
"""
# Import numpy as np
import numpy as np

# Use the np array
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

# Use the column_stack function
c = np.column_stack((a, b))

# Print the output
print(c)

# Print the Shape
print("\nThe shape of c is {}".format(c.shape))
