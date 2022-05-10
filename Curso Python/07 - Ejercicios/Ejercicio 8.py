"""
Ejemplo 8
    ¿Cuanto es el x por ciento de x numero?
    |   |   |   |   |20% de 150

"""

from unittest import result


print("Calculá el porcentaje de numero que quieras!")

num1 = int(input("Escribe el numero al que le quieres sacar un porcentaje: "))
num2 = int(input("Escribe el porcentaje que quieres calcular: "))

resultado = int((num1 * num2 / 100))

print(f"El {num2} de {num1} es: {resultado}")