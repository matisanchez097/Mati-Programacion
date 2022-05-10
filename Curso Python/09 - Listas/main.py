"""
Listas (arrays)
    son colecciones o conjuntos de tados/valores, bajo un unico
    nombre.
    Para acceder a esos valores podemos usar un indice numerico.

"""

# pelicula = "batman"


# Definir Listas
#   DEFINIR CON CORCHETES
peliculas = ["batman","spiderman","Señor de los anillos"]

#   DEFINIR LISTA CON LIST + TUPLA
cantantes = list(("2pac","drake","jennifer lopez"))
print(cantantes)

years = list(range(20,2050))
variada = ["victor", 200, True, "texto"]

print(years)

print(variada)

# Indices mofidicar array
peliculas[1] = "Gran torino"
peliculas[2] = "El hobbit"
print(peliculas[0:])
print(peliculas[-2])
print(cantantes[1:3])
print(cantantes[0:1])
print(cantantes[1:])

# Añadir elemento a lista

cantantes.append("Kase O")
cantantes.append("ricky martin")
print(cantantes[0:])

# Como recorrer lista

print("********* LISTA PELICULAS **********")
"""
nueva_pelicula = ""

while nueva_pelicula != "parar":
    nueva_pelicula = input("introduce la nueva pelicula: ")
    peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+ 1}. {pelicula}")

"""
#  Listas multidimensionales

print("\n******** LISTADO DE CONTACTOS ********")

contactos = [
    [
        "antonio",
        "antonio@gmail.com"
    ],
    [
        "luis",
        "luis@gmail.com"
    ],
    [
        "salvador",
        "salvador@gmail.com"
    ]
]

print(contactos)
print(contactos[1][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: "+ elemento)
        else:
            print("Email: "+ elemento)
    print("\n")