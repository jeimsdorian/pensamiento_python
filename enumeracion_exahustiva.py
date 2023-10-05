objetivo = int(input('elige un numero: '))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta +=1
if respuesta**2 == objetivo:
    print(f'la raiz cuadrada exacta de {objetivo} es {respuesta}')
else:
    print(f'el numero {objetivo} no tiene una raiz cuadrada exacta')