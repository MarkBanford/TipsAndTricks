import string

d = dict.fromkeys(string.ascii_lowercase, 0)

some_string = str(input("Enter words: "))
some_string = some_string.lower()
for char in some_string:
    if char in d.keys():
        d[char] += 1
print(d)



