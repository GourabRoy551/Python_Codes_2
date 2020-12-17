import numpy as np


x = np.arange(25).reshape(5, 5)
print(x)
print(x[2][2])
print(x[2, 2])

print(x[0:2, 2:])

