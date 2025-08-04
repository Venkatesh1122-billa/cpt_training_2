''' code to show the computation of statistics and 
access series attributes.
100 200 150 300 250
print original data, which is serialized 
Statistis:
mean
sum
max
min
Attributes:
index  = ['a'.......'e']
values = [100.0 ........250.0]'''

import pandas as pd
print("Enter 5 random numbers , space seperated: ")
numbers =  input().strip().split()
numbers = [float(num) for num in numbers]
try:
    if len(numbers) !=5:
        raise ValueError("please provide only 5 numbers:")
    series = pd.Series(numbers, index = ['a','b','c','d','e'])
    print("\n original series: ")
    print(series)

# Statistics

    print(f" Statistics :")
    print(f"Mean:{series.mean()}")
    print(f"Sum:{series.sum()}")
    print(f"Max:{series.max()}")
    print(f"Min:{series.min()}")

#Attributes
    print("\n Attributes")
    print(f"Index :{series.index.tolist()}")
    print(f"Values :{series.values.tolist()}")
    print(f"DataType :{series.dtype}")
except ValueError as e:
    print(f"Error:{e}")


    