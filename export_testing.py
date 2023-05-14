import pandas as pd

# create a sample dataframe
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'gender': ['F', 'M', 'M']}
df = pd.DataFrame(data)

# export the dataframe as a CSV file
df.to_csv('output.csv', index=False)
