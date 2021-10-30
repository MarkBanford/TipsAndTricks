''' updating col using dictionary'''

import pandas as pd

mydict = {'Tom': 20, 'John': 25, }

data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [None, 21, 19, None]}

df = pd.DataFrame(data)

df['Age'] = df.Name.map(mydict)

print(df)
