class Customer:
    def __init__(self, name='a', membership_type='b'):
        self.name = name
        self.membership_type = membership_type

    def __repr__(self):
        return f"Customer('{self.name}','{self.membership_type})"


names = ['John', 'Paul', 'Simon']
memb = ['Bronze', 'Silver', 'Gold']

instances = [Customer() for i in range(len(names))]

for i in range(len(names)):
    instances[i].name = names[i]
    instances[i].membership_type = memb[i]





