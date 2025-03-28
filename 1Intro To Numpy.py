import numpy as np
import pandas as pd

np1 = np.array([0,1,2])
print(np1)

# shape is like the len function for numpy
print(np1.shape)

# ndarray = n-dimensional array

# Range
np2 = np.arange(10)
print(np2)

# Step
np3 = np.arange(0,10,2)
print(np3)

# Zeros
np4 = np.zeros(10)
print(np4)

# Multidimensional zeros
np5 = np.zeros((2,10))
print(np5)

# Full
np6 = np.full((10),6)
print(np6)

# Multidimensional Full
np7 = np.full((2,10),6)
print(np7)

# Convert python lists to np
my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8)

