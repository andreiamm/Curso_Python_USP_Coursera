def insertion_sort(lista):
    for i in range(1, len(lista)):
        elemento = lista[i]
        j = i
        while j > 0 and lista[j - 1] > elemento:
            lista[j] = lista [j - 1]
            j = j - 1
            lista[j] = elemento
    return lista
