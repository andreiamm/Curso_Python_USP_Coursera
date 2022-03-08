def soma_lista(lista):
    n = len(lista)
    if n == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])

print(soma_lista([1,2,3,4,5]))
