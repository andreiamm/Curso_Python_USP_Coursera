def main():
    t1 = Triangulo(2, 3, 5)
    t2 = Triangulo(4, 6, 10)

    t1.semelhantes(t2)

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def semelhantes(self, triangulo):
        razao_a = self.a / triangulo.a
        razao_b = self.b / triangulo.b
        razao_c = self.c / triangulo.c
        if razao_a == razao_b and razao_b == razao_c:
            return True
        else:
            return False

main()
