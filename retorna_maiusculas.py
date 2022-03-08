def maiusculas(frase):
	nova_frase = ""
	for i in range(len(frase)):
		if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
			nova_frase = nova_frase + frase[i]
	return nova_frase


			
