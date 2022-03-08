def primeiro_lex(lista):
    menor_caractere = lista[0]
    for i in range(1,len(lista)):
        if lista[i] < menor_caractere:
                menor_caractere = lista[i]
    
    return menor_caractere
                       
                       
