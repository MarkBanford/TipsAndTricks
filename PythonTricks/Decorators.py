def mapper(fnc):
    def inner(list_of_values):
        return [fnc(val) for val in list_of_values]

    return inner


@mapper
def camelcase(s):
    '''Turns strings_like_this into StringsLikeThis'''
    return ''.join([word.capitalize() for word in s.split('_')])


names = ['rick_ross', 'snoop_dogg']

print(camelcase(names))
