class area_triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura) / 2
def calculos():
    try:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura:"))
        total = area_triangulo(base, altura)
        area_calculada = total.calcular_area()
        print(f"El área calculada del triángulo es: {area_calculada}")
    except ValueError:
        print("ERROR")
calculos()