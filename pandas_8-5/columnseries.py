import pandas as pd
names = pd.Series(['apples','orange','kiwi'])
df = names.to_frame(name = 'Name')

# Add New Column

df['Price'] = [50,30,80]
print(df)