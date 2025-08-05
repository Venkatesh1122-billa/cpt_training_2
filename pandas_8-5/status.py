import pandas as pd
try:
    df = pd.read_csv('hospital_data.csv')
    print("\n Original Hospital")
    print(df)

# Add a status column , based on age

    df['Status'] = df['Age'].apply(lambda x: 'Senior' if x>=50 else 'Adult' if x>=18 else 'Unknown' )
    print("\n Data frame with status column")
    print(df)
    
# Saving to csv

    df.to_csv('hospital_data_updated.csv', index = True)
    print("\ n Modified Dataframe saved to 'hospital_data_updated.csv'. ")
except FileNotFoundError:
    print("Error : 'hospital_data.csv' not found.")