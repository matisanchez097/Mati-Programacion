"""
FUNCIONES:
    Una funcion es un conjunto de instrucciones agrupadas bajo
    un nombre concreto que puede reutilizarse invocando a la
    funcion tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)

"""

#Ejemplo 1
"""
print("##### EJEMPLO 1 #####")

def muestraNombre():
    print("Matias")
    print("Paco")
    print("Franco")
    print("Aitor")
    print("Francisco")
    print("\n")

# INVOCAR FUNCION

muestraNombre()
muestraNombre()


"""

# Ejemplo 2: Parametros
"""
print("######## EJEMPLO 2 ########")


def mostrarTuNumbre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Que edad tenes?: "))

mostrarTuNumbre(nombre, edad)

"""
# Ejemplo 3
"""
print("######## EJEMPLO 3 ########")


def tabla(numero):

    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

numero = int(input("Introduce el numero que quieres la tabla!: "))

tabla(numero)

# Ejamplo 3.1
print("------------------------")
for numero_tabla in range(1,11):
    tabla(numero_tabla)
"""
# Ejemplo 4
"""
print("######## EJEMPLO 4 ########")

# Parametros Opcionales

def getEmpleado(nombre, dni = None):
    print("Empleado")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

nombre = input("Introduzca nombre del empleado: ")
dni = int(input("Introduzca el DNI del empleado"))

getEmpleado(nombre, dni)
"""
# Ejemplo 5: Return o devolver datos
"""
print("######## EJEMPLO 5 ########")

def saludame(nombre):
    saludo = (f"Hola, saludos {nombre}")

    return saludo

print(saludame("victor robles"))
"""
# Ejemplo 6

print("######## EJEMPLO 6 ########")
"""
def calculadora(num1, num2, basicas = False):

    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    div = num1 / num2
    
    cadena = ""
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta " + str(resta)
        cadena += "\n"
    else:
        cadena += "multiplicacion " + str(multi)
        cadena += "\n"
        cadena += "Division " + str(div)

    return cadena

print(calculadora(5, 5, True))
"""

# Ejemplo 7 "FUNCION DENTRO DE OTRA FUNCION"

"""
print("\n######## EJEMPLO 7 ########")

def getNombre(nombre):
    texto = (f"El nombre es: {nombre}")
    return texto

def getApellidos(apellidos):
    texto = (f"Los apellidos son: {apellidos}")
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("matias", "sanchez"))
"""
# Ejemplo 8: FUNCIONES LAMBDA O ANONIMA

print("\n######## EJEMPLO  ########")

dime_el_año = lambda año: f"El año es {año * 50}"

print(dime_el_año(2019))
