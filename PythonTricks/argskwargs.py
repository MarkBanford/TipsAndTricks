a, b, c = '4,5,6'.split(',')

my_list = [8, 9, 10]

x, y, z = my_list


##################################
# if we dont know how many arguments will be passed, we use *args and packs them

def pack_it(*args):
    print(args)
    print(type(args))


x1 = 'Forest'
y1 = 'Hill'
z1 = 'High'

pack_it(x1, y1, z1)


#############################

def unpack_it(p, t):
    print(p)
    print(t)


args = ['a', 'b']
unpack_it(*args)


###########################
# kwargs - used if we are receiving a dictionary

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))


func(q='Some', w='Thing', e='Here')
