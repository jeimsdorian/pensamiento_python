objeto = int(input('escoge un numero: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 -objeto) >= epsilon and respuesta <= objeto:
    print(abs(respuesta**2 - objeto), respuesta)
    respuesta += paso
if abs(respuesta**2 - objeto) >= epsilon:
    print(f'no se encontro la raiz cuadrada de {objeto}')
else:
    print(f'la raiz ciadrada de {objeto} es {respuesta}')