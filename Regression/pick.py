import numpy as np
import pickle 
data = np.array(([1,2,3],[4,5,6]))

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)