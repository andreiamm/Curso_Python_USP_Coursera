def éPrimo(k):
	primo = True
	i = 2
	while i < k and primo:
		if k % i == 0:
			primo = False
		i = i + 1
	return primo

def n_primos(n):
	qtde = 0
	while n >= 2:
		if éPrimo(n) == True:
			qtde += 1
		n = n - 1
	return qtde