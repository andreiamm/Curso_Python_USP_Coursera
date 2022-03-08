def remove_repetidos(lista):
	lista.sort()
	duplicado = []
	for i in range(len(lista) - 1):
		j = i + 1
		if lista[i] == lista[j]:
			duplicado.append(lista[j])

	for i in range(len(duplicado)):
		lista.remove(duplicado[i])

	return lista
		