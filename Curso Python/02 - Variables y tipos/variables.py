"""
Una  varoable es un contenedor de informacion que dentro guardará un dato, se pueden crear muchas variables
y que cada una tenga un dato distinto.
"""

texto = "Master en Python"
texto2 = 3 / 3

print(texto)
print(texto2)

texto = "Mati godeto"
texto2 = "Anasheeeei"

print(texto)
print(texto2)

# Concatenación 
nombre = "victor"
apellido = "Robles"
web = "victorrobles.es"

print(nombre + " " + apellido + " " + web)
print(f"{nombre} {apellido} {web}")
print("hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web))