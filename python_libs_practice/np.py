import numpy as np
import matplotlib.pyplot as plt
import math

a = np.array([[1, 2, 3], 
             [4, 5, 6]], dtype=float)
print(a, a-2)

# print(a.shape)
# print(a)

# # b = np.array([1, 2, 3, 4, 5, 6])
# # print(b,a)

# # a "view" is a shallow copy of the array
# # when list slicing you create a view in numpy not a deep copy like in python lists
# print("Element (0, 1):", a[0,1]) # access element [0][1]
# print("number of dimensions:", a.ndim) # number of dimensions len(a.shape) == a.ndim
# print("size:", a.size) # total number of elements

# b =  np.zeros((3,4)) 
# print(b)

# print(np.ones((2,3,4),dtype=np.int16))
# d = np.arange(10,25,5)
# print(d)
#print(np.linspace(0,2,9))
# e = np.full((2,2),7)
# print(e)
# f = np.eye(2)
print(np.random.random((2,2)))
# print(np.empty((3,2)))

