def conta_letras(frase, contar="vogais"):
    contagem = 0
    frase = frase.lower()
    if contar == "vogais":
        for i in range(len(frase)):
            if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
                contagem += 1
    elif contar == "consoantes":
        for i in range(len(frase)):
            if frase[i] != "a" and frase[i] != "e" and frase[i] != "i" and frase[i] != "o" and frase[i] != "u" and frase[i] != " ":
                contagem += 1

    return contagem
        
                
                
