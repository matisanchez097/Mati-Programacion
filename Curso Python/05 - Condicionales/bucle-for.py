"""

# FOR
for variable in elemento_iterable (array, range, etc)
    BLOQUE DE INSTRUCCIONES
"""
contador = 0
resultado = 0

for contador in range (0, 5):
    print("Voy por el "+ str(contador))

    resultado = resultado + contador

print(f"El resultado es {resultado}") 

# Ejemplo tablas de multiplicar
print("######## EJEMPLO ########")

numero_usuario = int(input("¿De que numero quieres la tabla? : "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"#### Tabla de multiplicar del numero {numero_usuario}####")

for numero_tabla in range(1, 11):

    if numero_usuario == 45:
        print("No se pueden numeros prohibidos !!")
        break #Se utiliza para finalizar el bucle y muestra lo que indiquemos arriba!!

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada")