class Suma:
        def __init__(self, num1, num2):
                self.num1 = num1
                self.num2 = num2
        def calculr_suma(self):
                return self.num1 + self.num2
        
num1 = float (input("ingrese num1:"))
num2 =  float (input("ingrese num2:"))

suma = Suma(num1, num2)
resultado = suma.calculr_suma()
print ("la suma es:", resultado ) 