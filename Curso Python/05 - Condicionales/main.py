# Condicional IF

# Ejemplo 1 
from ctypes.wintypes import PPOINT


print("######### EJEMPLO 1 #########")

color = "rojo"

if color == "rojo":
    print("Wow rojo tambien es mi color favorito!!")
else:
    print("El mio es el rojo")

# Operadores de comparacion
"""
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores Logicos
and = y
or = o
! = negacion
not = no


"""

print("######### EJEMPLO 2 #########")


#year = int(input("¿En que año te encuentras? : "))
"""
if year >= 2021:
    print("Estamos en 2021 en adelante")
else:
    print("Es un año anterior a 2021")
"""
#Ejemplo 3
print("######### EJEMPLO 3 #########")

"""
nombre = input("Cual es tu nombre? : ")
ciudad = input("Cual es tu cuidad? : ")
continente = input("De cual continente provienes? : ")
edad = int(input("Cual es tu edad? : "))
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} Es mayor de edad")
    if continente != "europa":
        print(f"El usuario {nombre} No es Europeo")
    else :
        print(f"El usuario {nombre} es Europeo y es de {ciudad}")
else:
    print(f"{nombre} No es mayor de edad")
"""

#Ejemplo 4
print("######### EJEMPLO 4 #########")
"""
print("Ingrese los dias de la semana con numeros, donde lunes = 1 , martes = 2, etc.")
dia = int(input("Introduce el dia de la semana! : "))

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

"""

#Ejemplo 5
print("######### EJEMPLO 5 #########")
"""
edad_min = 18
edad_max = 65
edad_real = int(input("Introduce tu edad: "))

if edad_real >= 18 and edad_real <= 65:
    print("Esta en edad de trabajar!!")
else:
    print("no esta en edad de trabajar")

"""

#Ejemplo 6
print("######### EJEMPLO 6 #########")
"""
pais = "alemania"

if pais == "mexico" or pais == "españa" or pais == "colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

"""

#Ejemplo 7
print("######### EJEMPLO 7 #########")
"""
pais = "españa"

if not (pais == "mexico" or pais == "españa" or pais == "colombia"):
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} si es un pais de habla hispana")

"""

#Ejemplo 8
print("######### EJEMPLO 8 #########")

pais = "colombia"

if pais != "mexico" or pais != "españa" or pais != "colombia":
    print(f"{pais} No un pais de habla hispana")
else:
    print(f"{pais} Si es un pais de habla hispana")