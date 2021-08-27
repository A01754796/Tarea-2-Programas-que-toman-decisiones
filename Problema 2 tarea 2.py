num1 = int(input("seleccione #1"))
num2 = int(input("seleccione #2"))
num3 = int(input("seleccione #3"))
if num1 == num2+num3:
    print("los números 2 y 3 se suman")
elif num2 == num1+num3:
    print("los números 1 y 3 se suman")
elif num3 == num2+num1:
    print("los números 1 y 2 se suman")
else:
    print("Ninguno")
    