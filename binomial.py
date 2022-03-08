n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

def fatorial(numero):
	i = 1
	fat = 1

	while i <= numero:
		fat = fat * i
		i = i + 1

	return fat

binomial = fatorial(n) / (fatorial(k) * fatorial(n - k))

print("Coeficiente binomial =", binomial)