import random

def lista_grande(n):
    lista = []
    valor = 0
    numero = 0
    for i in range(n):
        valor = n + 1000
        numero = random.randrange(1,valor)
        lista.append(numero)
    return lista
    
