''' 
input : 1 2 3 4 5
output : [-1 , 2 , -1 , 4, -1]
output : [True , 2 , True , 4, True]
output : [1, 'even', 3, 'even', 5]'''

import numpy as np
data = input('Enter numbers separated by space:')
arr = np.array(list(map(int, data.split())), dtype=object)      
arr[arr % 2 != 1] = 'even'
print(arr)
