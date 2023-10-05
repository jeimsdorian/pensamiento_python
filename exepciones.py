def divicion_de_una_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = range(1,11)
divisor = 2

print(divicion_de_una_lista(lista,divisor))