class area:
    def __init__(self, altura, base):
        self.base = base
        self.altura = altura

    def total_area(self):
        return (self.base + self.altura)

def caluculos():
    base = float(input("Ingrese la base "))
    altura = float(input("Ingrese la altura "))
    total = area(base, altura)
    print("el area es ", total.total_area())

caluculos()