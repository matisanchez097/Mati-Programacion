"""
EJERCICIO 1.
    Hacer un programa que tenga una lista de 8 numeros y haga
    lo siguiente:
    - Recorrer la lista y mostrarla
    - Hacer funcion
    - Ordenarla y mostrarla
    -Mostrar su Longitud
    -Buscar algun elemento (Que el usuario pida por teclado)
"""
lista = [2,5,41,4,9,8,45,6]
lista.sort()

# RECORRER Y MOSTRAR
print("########## recorrer y mostar ############")

# CREAR FUNCION QUE RECORRA LISTA Y DEVUELVA STRING

def mostrarLista(listas):
    resultado = ""

    for elemento in listas:
        resultado += str(elemento)
        resultado += "\n"
    return resultado

"""
# RECORRER Y MOSTRAR
for numero in lista:
    print(numero)

print("la longitud de la listas es de: " + str(len(lista)) + " Caracteres")
"""

print(mostrarLista(lista))