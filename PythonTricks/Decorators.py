# we want to take a list of strings and camelcase them. mapper will allow us
# to use our camelcase function to a list of strings

def mapper(fnc):
    def inner(list_of_values):
        return [fnc(value) for value in list_of_values]

    return inner


@mapper
def camelcase(s):
    """Turns into StringsLikeThis"""
    return ''.join([word.capitalize() for word in s.split('_')])


names = [
    'rick_ross',
    'snoop_dogg'
]

print(camelcase(names))