''' Is = True when the variables point to the same object. == will tbe true if they look the same'''

a = [1, 2, 3]
b = a

print(hex(id(a)))
print(hex(id(b)))
print(a == b)
print(a is b)

c = a.copy()
print(a == c)
