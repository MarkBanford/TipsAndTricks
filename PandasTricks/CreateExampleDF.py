import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [100, 200], 'B': [300, 400]})

# for a larger DF, we can use Numpy (r,c)

df1 = pd.DataFrame(np.random.rand(4, 8), columns=list('ABCDEFGH'))
print(df1)
