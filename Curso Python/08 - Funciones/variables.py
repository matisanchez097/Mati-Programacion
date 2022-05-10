"""
Variable locales: Se definen dentro de la funcion y no se puede
usar fuera de ella, solo estan disponibles dentro.
A no se que hagamos un return.

Variables globales: Son als que se declaran fuera de una funcion
y estan disponibles dentro de y fuera de ellas.

"""

# Variable global

frase = "ni los genios son dasdasd"

print(frase)

def holaMundo():
    frase = "hola mundo"
    print("Dentro de la funcion")
    print(frase)

    year = str(2021)
    print(year)

    global website
    website = "Matitito.com"
    return year

print(holaMundo())
print(website)
