my_list = [1,2,3]
my_list.append(4)
print(my_list)
print(my_list.pop())
my_list[1] = 'dos'
print(my_list)

a = [1,2,3]
b = a
print(id(a))
print(id(b))

c = a,b
a.append(5)
print(c)

a =[1,2,3]
b = a
c =a[::]
print(f'id a={id(a)} id b= {id(b)} id c ={id(c)} ')


doblue = [i*2 for i in range(0,100)]
print(doblue)
par = [i for i in range(100) if i % 2 == 0]
print(f'par{par}')

impar = [i for i in range(100) if i % 2 == 1]
print(f'impar{impar}')