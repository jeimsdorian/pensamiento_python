my_dic = {
    'david': 30,
    'juan': 20,
    'jose': 30
}

my_dic['david'] = 40 
print(my_dic)

my_dic ['felipe'] = 65

print(my_dic)

del my_dic ['felipe']
print(my_dic)

for llave in my_dic.keys():
    print(llave)

for valor in my_dic.values():
    print(valor)

for llave, valor in my_dic.items():
    print(f'{llave} tiene {valor} años')

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 1}
print(even_dict)
