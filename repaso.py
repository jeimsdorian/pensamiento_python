print('ENUMERACION EXAHUSTIVA')

objetivo = int(input('elige un numero: '))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta +=1
if respuesta**2 == objetivo:
    print(f'la raiz cuadrada exacta de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')

print("APROXIMACION")

objetivo = int(input('elige un numer: '))
epsilon = 0.01
pasos = epsilon**2
respuesta = 0.0

while abs(respuesta**2 -objetivo) >= epsilon and respuesta<= objetivo:
    print(respuesta)
    respuesta += pasos
if abs(respuesta**2 -objetivo) >= epsilon:
    print(f'no se puedo encontrar una raiz para{objetivo}')
else:
    print(f'la raiz cuadrada de {objetivo} es {respuesta}')

print("busqueda binaria")

objetivo = int(input("eliga un numero: "))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) /2

while abs(respuesta**2 -objetivo) >= epsilon:
    print(respuesta)
    if respuesta**2 > objetivo:
        alto = respuesta
    else:
        bajo = respuesta
    respuesta = (alto + bajo) /2
print(f'la raiz cuadrada de {objetivo} es {respuesta}')