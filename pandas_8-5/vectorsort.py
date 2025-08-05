import pandas as pd
try:
    df = pd.read_csv('hospital_data.csv')
    print("\n Original Hospital")
    print(df)
    
# Add discount_cost column (10% discount)
  
    df['Discount'] =df['Bill']*0.9
    
# Sorting by bill

    sorted_df = df.sort_values('Bill', ascending = False)
    print("\n Sorted by Medical Bills (descending order):")
    print(sorted_df)
except FileNotFoundError:
    print("Error : 'Hospital_data.csv' not found.")