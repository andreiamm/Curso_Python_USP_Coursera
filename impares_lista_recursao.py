def encontra_impares(lista, lista_impares=[]):
    if lista_impares == None:
        lista_impares = []

    if len(lista) == 0:
        lista_impares = []
    else:
        if lista[0] % 2 != 0:
            lista_impares.extend([lista[0]])
        encontra_impares(lista[1:], lista_impares)
        return lista_impares

print(encontra_impares([2,4,6]))
