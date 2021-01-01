'''Often when looping through a list you want to access not only the index with a position in the list but the actual element as well.'''

x = ['a', 'b', 'c', 'd']

# usually

for i in range(len(x)):
    print(i, x[i])

# we can do this better with enumerate

for i, v in enumerate(x):
    print(i, v)
