def sumar(num1, num2):
    """Función que suma dos números y devuelve el resultado."""
    return num1 + num2

def main():
    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        
        resultado = sumar(numero1, numero2)
        print(f"La suma de {numero1} + {numero2} es: {resultado}")
    except ValueError:
        print("Error: Debes ingresar solo números.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()