import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salesData = pd.read_excel(
    'Sample - Superstore.xls')

pivot = pd.pivot_table(salesData, index='Sub-Category', values=['Sales', 'Profit'], aggfunc='mean').reset_index()

salesData['OrderDateMonth'] = salesData['Order Date'].apply(lambda x: x.month)
salesData['OrderDateYear'] = salesData['Order Date'].apply(lambda x: x.year)

salesMonthYear = pd.pivot_table(salesData, index=['OrderDateMonth'], columns=['OrderDateYear'], aggfunc='sum',
                                values='Sales')

salesMonthYear.plot()

print(salesMonthYear.pct_change())

salesMonthYear.to_csv('test.csv')

########################## rolling means

# rObj = salesMonthYear.rolling(2)
# mean = rObj.mean()
# print(mean)
