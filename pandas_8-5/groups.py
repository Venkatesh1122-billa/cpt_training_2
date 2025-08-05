import pandas as pd
try:
    df = pd.read_csv('hospital_data.csv')
    print("\n Original Hospital")
    print(df)
    
#Grouping by department
    
    grouped = df.groupby('Department')['Bill'].mean()
    print("\n Average Medical Cost by Department ")
    print(grouped)
except FileNotFoundError:
    print("Error : 'Hospital_data.csv' not found.")