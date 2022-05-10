"""
Ejercicio 9:
    Hacer un programa que pida numeros al usuario indefinidamente
    hasta meter el numero 111

"""

from cgi import print_arguments
from contextlib import nullcontext


contador = 1

while contador < 100:
    numUs = int(input("Intruduzca un numero: "))

    if numUs == 111:
        print("El bucle se ha terminado!!")
        break
    else:
        print(f"Has introducido el: {numUs}")