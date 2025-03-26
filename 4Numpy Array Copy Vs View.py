import numpy as np

# Copy Vs. View
np1 = np.array([0,1,2,3,4,5])

'''
# Create a view
np2 = np1.view()

print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np1[0] = 41

print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')        # whenever we change the original, the viewed one changes too, viewed means that the viewed is connected to the original

# Also, if you make a change to the viewed, the original one will update, so whichever you update, the other one(s) will also be updated

'''

# Create a copy
np2 = np1.copy()

print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np1[0] = 41

print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')        # When we use copy, the copied one doesn't update


