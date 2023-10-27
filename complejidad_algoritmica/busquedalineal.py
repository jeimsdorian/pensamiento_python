import random
def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    
    return match


if __name__ == '__main__':
    tamaño_de_lista = int(input('¿de que tamaño sera la lista? '))
    objetivo = int(input('¿que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]

    encontrado = busqueda_lineal(lista,objetivo)
    print(lista)
    print(f'El elmento {objetivo} {"esta" if encontrado else "no esta"} en esta lista')