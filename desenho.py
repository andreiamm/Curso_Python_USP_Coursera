colunas = int(input("digite a largura: "))
linhas = int(input("digite a altura: "))

i = 0
while i < linhas:
	j = 0
	while j < colunas:
		print("#", end="")
		j += 1
	print()
	i += 1