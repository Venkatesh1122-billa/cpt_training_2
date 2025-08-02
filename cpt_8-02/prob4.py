''' 
input : [2,3,5,6,7]
output :[False, True, True, False, True]'''

import numpy as np
data = input('Enter numbers seperated by space:')
arr = np.array(list(map(int, data.split())))
mask = arr%3 ==0
print(mask)



