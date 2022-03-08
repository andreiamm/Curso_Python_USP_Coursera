n = int(input("Digite primeiro número: "))
lista = []

while n != 0:
	lista.append(n)
	n = int(input("Digite outro número: "))

tamanho = len(lista)
i = 1
while i <= tamanho:
	print(lista[-i])
	i = i + 1

