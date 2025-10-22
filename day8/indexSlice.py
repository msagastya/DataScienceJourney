import numpy as np
a = np.array([10, 20, 30, 40, 50])
print("First element:", a[0])
print("Last two:", a[-2:])
print("Step slicing:", a[::2])

b = np.array([[1, 2, 3], [4, 5, 6]])
print("Element (1,2):", b[1, 2])  # row 1, col 2