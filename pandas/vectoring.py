import pandas as pd
print("Enter 4 numbers , space seperated: ")
numbers = input().strip().split()
numbers = [float(num) for num in numbers]
try:
    if len(numbers) !=4:
        raise ValueError("Give 4 numbers only !!!")
    series = pd.Series(numbers, index = ['a','b','c','d'])
    print("\n Original series: ")
    print(series)

# doubling values vector operations
    doubled = series*2
    print("\n series after doublig series: ")
    print(doubled)

# adding 100 to all values vector operations

    added = series+100
    print("\n series after adding 100: ")
    print(added)
except ValueError as e:
    print(f"Error:{e}")