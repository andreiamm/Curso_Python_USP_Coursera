import math

print("Informe as duas coordenadas do primeiro ponto do plano cartesiano:")
x1 = float(input())
y1 = float(input())

print("Informe as duas coordenadas do outro ponto do mesmo plano cartesiano:")
x2 = float(input())
y2 = float(input())

distancia = math.sqrt(((x1 - x2) ** 2) + (y1 - y2) ** 2)

if distancia >= 10:
	print("longe")
else:
	print("perto")