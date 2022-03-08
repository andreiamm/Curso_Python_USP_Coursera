def soma_matrizes(m1, m2):
	if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
		return False
	else:
		m3 = []
		for i in range(len(m1)):
			linha = []
			for j in range(len(m1[0])):
				valor = m1[i][j] + m2[i][j]
				linha.append(valor)
			m3.append(linha)
		return m3

m1 = input()
m2 = input()
soma_matrizes(m1, m2)