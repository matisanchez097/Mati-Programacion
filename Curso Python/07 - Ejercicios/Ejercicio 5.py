"""
Ejercicio 5:
    Hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario.

"""

num1 = int(input("Introduce el numero menor: "))
num2 = int(input("Introduce el numero mayor: "))

while num1 <= num2:
    print(num1)
    num1 += 1
    print(num1)
    if num1 == num2:
        break

