# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])
# print("Element at [0,1]:", arr[0,1])
# print("First row:", arr[0, :])
# print("First first element sliced:", arr[:, 1:])
# arr[0,0] = 100
# print("Modified array:\n", arr)


import numpy as np
arr = [1,2,3,np.nan, 5]
print(" Mean Ignoring NaN: ", np.nanmean(arr))
print("sum:" , np.sum(arr))
print("std ignoring NaN:", np.std(arr[np.isnan(arr)]))
