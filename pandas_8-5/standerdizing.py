import pandas as pd
try:
    df = pd.read_csv('hospital_data.csv')
    series = df['Name']
    print("\n Original Name Series ")
    print(series)
    clean_series = series.str.title().str.strip()
    print("Name series after standardizing with (titlecase, stripped space):")
    print(clean_series)
    
# Saving to csv dataframe
    df['Name'] = clean_series
    df.to_csv('hospital_data.csv',index = False)
    print("Data saved to csv file")
except FileNotFoundError:
    print("Error: 'hospital_data.csv' not found")        