class Person:
    def __init__(self, first, last, address):
        self.first = first
        self.last = last
        self.address = address

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'

    @property  # We dont have to use instance.fullname(), we can now drop the parenthesis (per.fullname)
    def fullname(self):
        return self.first + ' ' + self.last


    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('Full name deleted')


per = Person('Sam', 'Edison', 'USA')

# lets change first name

per.first = 'Samuel'
print(per.email)  # This still displays Sam.Edison@email.com because email is in the init method
print(per.fullname)
per.fullname = 'David Jones'
print(per.fullname)
print(per.email)
del per.fullname
print(per.first)

