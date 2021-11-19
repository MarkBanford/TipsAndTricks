import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))


def func1():
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
    return df


def func2(df):
    print(df.head())


func2(df)
