'''Arays - import numpy'''

import numpy as np
x  = np.array([1,2,3,4,5])
print("Array 1-D" ,  x)

y  = np.array([[1,2],[3,4,]])
print("Array 2-D \n" ,  y)

o = np.ones((3,6))
print("Ones \n",o)

z = np.zeros((10,10))
print("Zeroes \n",z)

i = np.eye(8)
print("Identical co-ordinates: \n",i)

r = np.arange(0,11,2)
print("Array :",r)

seperate = np.linspace(0,1,10)
print("linspace :",seperate)