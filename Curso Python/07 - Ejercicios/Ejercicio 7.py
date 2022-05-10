"""
Ejercicio 7:
    Hacer un programa que muestre todos los numeros impares entre dos numeros que decida el usuario.

"""

num1 = int(input("Introduzca su primer numero: "))
num2 = int(input("Introduzca su segundo numero: "))

if num1 < num2:
    for x in range (num1, num2 + 1):
        if x%2 == 0:
            print(f"El numer {x} es PAR!")
        else:
            print(f"El numero {x} es IMPAR")



else:
    print("El primer numero debe ser menor")