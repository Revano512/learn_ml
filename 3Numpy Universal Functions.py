import numpy as np

# Numpy Universal Function
np1 = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])

print(np1)

# Square root of each element
print(np.sqrt(np1))

# Absolute value
print(np.absolute(np1))

# Exponentials
print(np.exp(np1))

# Min/Max
print(np.max(np1))
print(np.min(np1))

# Sign positive or negative
print(np.sign(np1))             # Returns -1 if negative and 1 if positive

# Trigonometry, sin cos log
print(np.sin(np1))
print(np.cos(np1))
print(np.log(np1))

# You can see the documentation for more at https://numpy.org/devdocs/reference/ufuncs.html