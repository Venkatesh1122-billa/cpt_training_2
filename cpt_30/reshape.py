import numpy as np
a = np.arange(1,10)
print(a)

reshaped = a.reshape((3,3))
print(reshaped)

print("Element at (1,1):", reshaped[1,1])
linear = reshaped.flatten()
print(linear)
print("greater than 5:", linear[linear>5])
print("less than 5:", linear[linear<5])

print("Random numbers between 0 to 3 :",np.random.rand(3))
print("Random integer :\n ", np.random.randint(1,100,(2,3)))