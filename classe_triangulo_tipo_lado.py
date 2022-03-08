def main():
    t = Triangulo(1, 1, 1)
    u = Triangulo(3, 4, 5)
    x = Triangulo(4, 4, 5)

    t.tipo_lado()
    u.tipo_lado()
    x.tipo_lado()

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return "equilátero"
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return "escaleno"
        else:
            return "isósceles"

main()
