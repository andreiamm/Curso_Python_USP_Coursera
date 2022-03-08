import math

def é_hipotenusa(x, y, z):
	if (x ** 2) == math.sqrt((y ** 2) + (z ** 2)):
		return True
	else:
		return False

def soma_hipotenusas(n):
	m = 1
	soma = 0
	while m <= n:
		i = 1
		while i <= n:
			j = 1
			while j <= n:
				if é_hipotenusa(m, i, j) == True: 
					soma = soma + m
				j += 1
			i += 1
		m += 1
	return soma

n = int(input("numero = "))

print(soma_hipotenusas(n))
