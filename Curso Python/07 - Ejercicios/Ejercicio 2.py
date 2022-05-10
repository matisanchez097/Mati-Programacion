"""
Ejercio 2:
    Escribir un script que nos muestre por pantalla todos los numeros pares del 1 a 120
"""

numeros = 1

for numeros in range(1, 121):
    if numeros%2 == 0:
        print(numeros)
    