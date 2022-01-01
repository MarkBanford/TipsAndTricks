import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [100, 200, 300, 400, 500], 'B': [1000, 2000, 3000, 4000, 5000]})

# for a larger DF, we can use Numpy (r,c)

df1 = pd.DataFrame(np.random.rand(4, 8), columns=list('ABCDEFGH'))
# print(df)
# print(df[1:3])

df = pd.DataFrame(index=pd.date_range(start='1/1/2018', periods=8),
                  data=np.random.rand(8, 2), columns=['A', 'B'])

df.at[df.index[-1], 'B'] = 1.1  # replace last value in B with 1.1
# print(df)

bool_filt = df.index > '2018-01-06'
# print(df[bool_filt])

# resampling

date_index = pd.date_range(start='01-Jan-2019', end='30-Jan-2019', freq='min')
data = np.random.rand(len(date_index), 2)
df_intraday = pd.DataFrame(index=date_index, data=data, columns=['A_col', 'B_col'])

# print(df_intraday.head(5))
df_hourly_last = df_intraday.resample('H').last()
df_sum_columns = df_intraday.sum(axis=0)
print(df_sum_columns)

df_sum_rows = df_intraday.sum(axis=1)
print(df_sum_rows)
