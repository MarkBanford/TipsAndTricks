
# Client Portfolio

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91},
    {'name': 'MSFT', 'shares': 50, 'price': 45},
    {'name': 'FB', 'shares': 105, 'price': 100}

]

# collect all name

names = [s['name'] for s in portfolio]

# find all entries with more than 75 shares

more75 = [s['name'] for s in portfolio if s['shares'] > 75]

# find the total position value (shares* price)

value = sum([s['shares'] * s['price'] for s in portfolio])
