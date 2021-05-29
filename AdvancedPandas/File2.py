import numpy as np
import pandas as pd

data = np.arange(100).reshape(20, 5)  # r, c

print(pd.__version__)

columnName = ['columns_' + str(i) for i in range(5)]

df = pd.DataFrame(data, columns=columnName)

print(np.cumsum(df['columns_0']))

##############################################################################


dictCheck = {'a': 10, 'b': 20, 'c': 30}

sampleNumpy = np.array(['a', 'b', 'c', 'a', 'a', 'c'])

data = pd.DataFrame(sampleNumpy, columns=['columnName'])


# data = data['columnName'].map(dictCheck)


def checkFunc(x):
    if 0 < x < 10:
        return 'G10'
    if 10 < x < 20:
        return 'G20'
    if x>20:
        return 'G99'


df = df.applymap(lambda x: checkFunc(x))  # apply function to whole df

print(df)
