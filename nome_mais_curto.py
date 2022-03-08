def menor_nome(lista_de_nomes):
    for i in range(len(lista_de_nomes)):
        lista_de_nomes[i] = lista_de_nomes[i].strip().capitalize()
    #print("Lista arrumada = ", lista_de_nomes)

    numero_caracteres = []
    for i in range(len(lista_de_nomes)):
        numero_caracteres.append(len(lista_de_nomes[i]))
    #print("Número de caracteres = ", numero_caracteres)

    menor_caractere = numero_caracteres[0]
    posicao_menor = 0
    for i in range(1,len(lista_de_nomes)):
        if numero_caracteres[i] < menor_caractere:
            menor_caractere = numero_caracteres[i]
            posicao_menor = i

    menor_nome = lista_de_nomes[posicao_menor]
    #print("Menor nome =", menor_nome)
    return menor_nome

def teste_menor_nome():
    print('************ Começando testes *******************')
    lista1 = [' Ana', ' maria Julia', ' eriberto ', 'sandoval', ' mario', 'sabrina', 'paulo ']
    if mais_curto(lista1) != "Ana":
        print("Teste 1 apresentou erro. Resultado", mais_curto(lista1), "em vez de Ana.")

    lista2 = [' Udo', ' Paola', ' Ana ', 'Jussara ', ' Astrogildo', 'Josias', ' Juca ']
    if mais_curto(lista2) != "Ana":
        print("Teste 2 apresentou erro. Resultado", mais_curto(lista2), "em vez de Ana.")
    print('************ Finalizando testes *******************')

#lista = [' Ana', ' maria Julia', ' eriberto ', 'sandoval', ' mario', 'sabrina', 'paulo ']
#mais_curto(lista)

#teste_menor_nome()
