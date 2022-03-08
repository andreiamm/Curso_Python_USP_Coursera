def fatorial(n):
	fat = 1
	i = 1
	while i <= n:
		fat = fat * i
		i += 1
	return fat

n = int(input("Digite o primeiro número inteiro: "))

while n >= 0:
	print(f"{n}! = {fatorial(n)}")
	n = int(input("Digite outro número inteiro: "))
	