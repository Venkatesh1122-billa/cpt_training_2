import pandas as pd
try:
    df = pd.read_csv('hospital_data.csv')
    series = df['Bill']
    print("\n Original Hospital DataFrame")
    print(series)
    
# User manual input
    print("\n Enter Patient_ID to update:")
    patient_id = input().strip()
    print("Enter new Bill for {patient_id}:")
    new_cost = float(input())
    
#Update bill series and save
    if patient_id in df['Patient_Id'].values:
        index = df[df['Patient_Id'] == patient_id].index[0]
        series[index] = new_cost
        print("\n Updated Medical Bill series.")
        print(series)
# update dataframe and save
        df['Bill'] = series
        df.to_csv('hospital_data.csv', index = False)
        print("|Updated csv saved to 'hospital_data.csv'")
    else:
         print(f"Error: patient_id {patient_id} not found.")
except FileNotFoundError:
    print(f"Error: 'hospital_data.csv' not found.")
    

    