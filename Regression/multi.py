import pickle
my_list = [10,2,3,'Hatori',True]
with open('data.pkl', 'wb') as f:
    pickle.dump(my_list, f)

with open('data.pkl', 'rb') as f:
    loaded_list = pickle.load(f)
print(loaded_list)