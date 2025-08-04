''' code eloborates how to filter string data in a series based on 
insensitivity '''

import pandas as pd
print("Enter 4 random strings , space seperated : ")
strings = input().strip().split()
print("Enter substrig : ")
substring = input().strip()
try:
    if len(strings) != 5:
        raise ValueError("Please provide 5 strings only :")
    series = pd.Series(strings)
    print("\n Original Series: ")
    print(series)
    filtered_series = series[series.str.lower().str.contains(substring.lower(), na=False)]
    print(f"strings containing '{substring}' (case-insensitive):")
    print(filtered_series if not filtered_series.empty else "No match found .")

except ValueError as e:
    print(f"Error{e}")