n = input("Digite um número: ")
tamanho = len(n)
controle = False
primeiro = 0
segundo = 0

while not controle:
	primeiro = int(n) // (10 ** (tamanho - 1))
	n = int(n) % (10 ** (tamanho - 1))
	tamanho = tamanho - 1
	segundo =  n // 10 ** (tamanho - 1)
	if primeiro == segundo and tamanho > 0:
		controle = True
		print("sim")
	elif tamanho == 0:
		controle = True
		print("não")



