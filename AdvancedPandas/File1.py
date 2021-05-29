import numpy as np
import pandas as pd

data = np.arange(100).reshape(20, 5)  # r, c

print(pd.__version__)

columnName = ['columns_' + str(i) for i in range(5)]

df = pd.DataFrame(data, columns=columnName)

# print(df)

# slicing

# print(df[:4])  # selects first 4 rows

# print(df[7:14])

# selecting by labels

# print(df.loc[:2, ['columns_2', 'columns_3']])  #selects 4 rows with specified cols


# selection by position

print(df.iloc[1][1])  # single cell value

# print(df.iloc[:4, :4])  # print sub-section

print(df[df['columns_1'] < 18])  # filter

df = df.replace([0, 1, 2], np.NaN)  # replace 0 with NaN
print(df.iloc[:4, :4])

# check for missing values ie NaN
print(df.isnull().sum())


# replace NaN with mean of that column

df = df.fillna(df.mean())
print(df.iloc[:4, :4])
