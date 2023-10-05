my_tuple = ()
type(my_tuple)

my_tuple = (1, 'dos')

print(my_tuple[1])

my_tuple = (1,)

print(type(my_tuple))

my_other_tuple = (2,3,4)

my_tuple += my_other_tuple

print(my_tuple)

x, y, z = my_other_tuple

print(f'x = {x} y = {y} z = {z}')

def cordenadas():
    return (4,5)

x, z = cordenadas()
print(f'x = {x} y = {y} z')