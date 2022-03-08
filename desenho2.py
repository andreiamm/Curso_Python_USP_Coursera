colunas = int(input("digite a largura: "))
linhas = int(input("digite a altura: "))

i = 1
while i <= linhas:
	if i == 1 or i == linhas:
		j = 1
		while j <= colunas:
			print("#", end="")
			j += 1
	else:
		j = 3
		print("#", end="")
		while j <= colunas:
			print(" ", end="")
			j += 1
		print("#", end="")			
	print()
	i += 1