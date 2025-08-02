'''code to extract all the odd numbers from user input
and print them in a list using array of numpy
inpt : 1 2 3 4 5 9 8 7 6
output : [1, 3, 5, 9, 7]
'''
# import numpy as np
# def extract_odd_numbers():
#     user_input = input("Enter numbers separated by space: ")    
#     numbers = list(map(int, user_input.split()))
#     odd_numbers = np.array([num for num in numbers if num % 2 != 0])
#     print("Odd numbers:", odd_numbers.tolist()) 
# extract_odd_numbers()


import numpy as np
data = input("Enter numbers separated by space: ")
arr = np.array(list(map(int, data.split())))
odd_numbers = arr[arr % 2 != 0]
print("Odd numbers:", odd_numbers.tolist())



