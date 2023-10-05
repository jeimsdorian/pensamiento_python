objetivo = int(input("escoga un nummero: "))
epsilon = 0.01
pasos = epsilon**2
respuesta = 0.0

while abs(respuesta**2 -objetivo) >= epsilon and respuesta <= objetivo:
    print(f'objetivo= {abs(respuesta**2 -objetivo)} respuesta= {respuesta}')
    respuesta += pasos
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'no se pudo encontras la raiz cuadrada de {objetivo}')
else:
    print(f'la raiz cuadrada de {objetivo} es {respuesta}')