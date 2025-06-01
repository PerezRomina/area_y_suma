class Suma:
    def __init__(self):
        pass
    def numeros_suma (self, msj) :
     while True:
        try : 
            return float(input(msj))
        except ValueError:
            print("error ingresa un num")
            
    def calcular_suma(self, num1, num2):
     return  num1 + num2
    
def main():
    suma = Suma()
    num1= suma.numeros_suma ("inregsa num1")
    num2= suma.numeros_suma ("inregsa num2")
    result = suma.calcular_suma (num1, num2)
    print ("el resultado es", result)
    
if __name__ == "__main__":
    main()