def main():
    t = Triangulo(1, 3, 5)
    u = Triangulo(3, 4, 5)

    t.retangulo()
    u.retangulo()

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        quada = self.a ** 2
        quadb = self.b ** 2
        quadc = self.c ** 2
        if quada == (quadb + quadc) or quadb == (quada + quadc) or quadc == (quadb + quada):
            return True
        else:
            return False

main()
