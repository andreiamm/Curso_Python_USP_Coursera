def fizzbuzz(n):
	if n % 3 == 0 and n % 5 != 0:
		resultado = "Fizz"
	elif n % 3 != 0 and n % 5 == 0:
		resultado = "Buzz"
	elif n % 3 == 0 and n % 5 == 0:
		resultado = "FizzBuzz"
	else:
		resultado = n
	return resultado

