 def éPrimo(k):
	primo = True
	i = 2
	while i < k and primo:
		if k % i == 0:
			primo = False
		i = i + 1
	return primo

def maior_primo(k):
	primo = False
	maior = 0
	while k > 1 and not primo:
		if éPrimo(k) == True:
			maior = k
			primo = True
		k = k - 1
	return maior