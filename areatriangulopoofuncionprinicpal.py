class area_triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

def calculos():
    try:
        base = float(input("Pon la base del triángulo: "))
        altura = float(input("Pon la altura del triángulo: "))
        total = area_triangulo(base, altura)
        print("El área del triángulo es:", total.calcular_area())
    except:
        print("ERROR")

if __name__ == "__main__":
    calculos()
