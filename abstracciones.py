numero = int(input('ponga un num: '))
def enumeracion_exahustiva(numero):
    respuesta = 0
    while respuesta**2 < numero:
        respuesta +=1
    if respuesta**2 == numero:
        print(f'la raiz cuadrada de {numero} es {respuesta}')
    else:
        print(f'{numero} no tiene una raiz cuadrada exacta')
    return numero

print(enumeracion_exahustiva(numero))

objetivo = int(input(' eliga un numero: '))
def aproximacion(objetivo):
    epsilon = 0.01
    pasos = epsilon**2
    respuesta_A = 0.0

    while abs(respuesta_A**2 -objetivo) >= epsilon and respuesta_A <= objetivo:
        respuesta_A += pasos
    if abs(respuesta_A**2 -objetivo) >= epsilon:
        print(f'no se puedo encontrar la raiz cuadrada de {objetivo}')
    else:
        print(f'la raiz cuadrada de {objetivo} es {respuesta_A}')
    return objetivo
print(aproximacion(objetivo))

obj = int(input('eliga un numero: '))
def busqueda_binaria(obj):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, obj)
    respuesta = (alto + bajo )/2

    while abs(respuesta**2 - obj) >= epsilon:
        if respuesta**2 < obj:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) /2
    print(f'la raiz cuadrada de {obj} es {respuesta}')
    return obj
print(busqueda_binaria(obj))