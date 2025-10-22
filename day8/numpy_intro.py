import numpy as np

# 1D Array
a = np.array([1, 2, 3, 4])
print("1D Array:", a)

# 2D Array
b = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", b)

# Array of zeros
z = np.zeros((2, 3))
print("Zeros:\n", z)

# Array of ones
o = np.ones((3, 2))
print("Ones:\n", o)

# Range and linspace
r = np.arange(0, 10, 2)
print("Range:", r)

l = np.linspace(0, 1, 5)
print("Linspace:", l)

print("Shape:", b.shape)
print("Size:", b.size)
print("Data type:", b.dtype)
print("Dimensions:", b.ndim)