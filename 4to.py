def sumar_dos_numeros():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        suma = num1 + num2
        print(f"La suma de {num1} + {num2} es: {suma}")
    except ValueError:
        print("Error: Por favor, introduce solo números válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


sumar_dos_numeros()