import pandas as pd

df = pd.DataFrame({'A': [100, 200], 'B': [300, 400]})

# Use df.rename where we use a dict, the keys are the old name and vals are new names

df = df.rename({'A': 'NEW_A', 'B': 'NEW_B'}, axis='columns')

# lets say we want to replace the _ with a &

df.columns = ['col_one', 'col_two']
df.columns = df.columns.str.replace('_', '&')
print(df)
