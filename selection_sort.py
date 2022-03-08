def ordena(lista):
    tamanho = len(lista)
    for i in range(tamanho - 1):
        posicao_menor = i
        for j in range(i + 1, tamanho):
            if lista[j] < lista[posicao_menor]:
                posicao_menor = j
        lista[i], lista[posicao_menor] = lista[posicao_menor], lista[i]

    return lista
