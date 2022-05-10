"""
Ejercicio 3:
    Esciribir un programa que te muestren los cuadrados (un numero multiplicado por si mismo) de los 60 primeros numeros naturales.
    Resolverlo con:
    For y con while

"""

# Resolviendo con bucle While:

contador = 0

while contador <= 60:
    resultado = contador*contador
    print(f"El cuadrado del numero {contador} es {resultado}")
    contador += 1


# Resonlviendo con bucle for:

contador1 = 0

for contador1 in range(0, 61):
    resultado1 = contador*contador
    print(f"El cuadrado del numero {contador1} es {resultado1}")

