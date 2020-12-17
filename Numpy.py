# Python program to demonstrate  
# basic array characteristics 
import numpy as np

# Creating array object 
arr = np.array([[1, 2, 3],
                [4, 2, 5]])

# Printing type of arr object 
print("Array is of type: ", type(arr))

# Printing array dimensions (axes) 
print("No. of dimensions: ", arr.ndim)

# Printing shape of array 
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array 
print("Size of array: ", arr.size)

# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype)
# -------------------------------------------------------
y = [[1, 2, 3, ], [4, 5, 6], [7, 8, 9]]

x = np.array(y)
print(y)

print(np.zeros((3, 3)) -5)

print(np.ones((3, 4)))

print(np.eye(4))

print(np.arange(50).reshape(5, 10))

print(np.linspace(0, 100, 5))

print(np.random.randint(5))
