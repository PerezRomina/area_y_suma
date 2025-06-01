def area_triangulo(base, altura):
    return (base * altura) / 2

def caluclos():
    base = float(input("Ingrese la base  "))
    altura = float(input("Ingrese la altura "))
    area = area_triangulo(base, altura)
    print("El area calculada del triangulo es ", area)

caluclos()