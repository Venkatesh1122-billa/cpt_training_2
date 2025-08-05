import numpy as np
import pandas as pd
try:
    df = pd.read_csv('hospital_data.csv')
    series = df['Age']
    print("\n Original age series :")
    print(series)
# Replace invalid ages , <0 or >120 with NaN
    
    clean_series = series.where((series >= 0) & (series <= 120),np.nan)
    print("\n Age series after replacing invalid ages with NaN:")
    print(clean_series)
    df['Age'] = clean_series
    df.to_csv('hospital_data.csv', index = False)
    print("\n updated csv saved to 'hospital_data.csv'.")
except FileNotFoundError:
    print("Error :'hospital_data.csv' not found.")