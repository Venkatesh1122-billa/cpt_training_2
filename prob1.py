'''code to extract all the odd numbers from user input
and print them in a list using array of numpy
input : 1 2 3 4 5 
output : [-1 , 2 , -1 , 4, -1]'''


import numpy as np
data = input('Enter numbers seperated by space:')
arr = np.array(list(map(int, data.split())))
result = np.where(arr %2!=0, -1, arr)
print("Result :",result)