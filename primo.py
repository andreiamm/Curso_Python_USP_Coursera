n = int(input("Digite um número inteiro: "))

if n == 2 or n == 3 or n == 5 or n == 7:
	print("primo")
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
	print("não primo")
else:
	print("primo")