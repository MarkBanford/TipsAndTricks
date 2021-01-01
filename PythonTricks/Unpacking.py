def print_vector(x, y, z):
    print('<%s,%s,%s>' % (x, y, z))


tuple_vec = (0, 1, 0)
print(print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2]))

# We can use unpacking

print(print_vector(*tuple_vec))

gen_expr = [x * x for x in range(3)]
print(print_vector(*gen_expr))

##########################################################################################################


dict_vec = {'x': 100, 'y': 20, 'z': 10}
print(print_vector(*dict_vec))  # gets keys
print(print_vector(**dict_vec))  # gets values
