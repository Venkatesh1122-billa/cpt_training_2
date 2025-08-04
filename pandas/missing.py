'''Missing Value operation on NaN'''

import numpy as np
import pandas as pd
series = pd.Series([10, np.nan, 30, np.nan, 50],index = ['a','b','c','d','e'])
print("\n origial series: ")
print(series)

#check missing values

print("\n missing values: ")
print(series.isna())

#Replace nan with 0 

filled_series = series.fillna(0)
print("\n series after filling NaN with o: ")
print(filled_series)

#Missing value deletion

dropped_series = series.dropna()
print("\n series after dropping missing values : ")
print(dropped_series)