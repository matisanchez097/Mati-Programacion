"""
Diccionario:
    Un tipo de dato que almacena un conjunto de datos.
    En formato clave > Valor.
    Es parecido a un array asociativo o un objeto Json.

"""

persona = {
    "nombre": "Victor",
    "apellidos": "Robles",
    "Web": "victorRobles.es"
}

print(persona["Web"])

# Lista con diccionarios

contactos = [
    {
        "nombre": "Antonio",
        "email": "antonio@hotmail.com"
    },
    {
        "nombre": "Luis",
        "email": "luis@hotmail.com"
    },
    {
        "nombre": "Salvador",
        "email": "salvador@hotmail.com"
    }
]

print(contactos[0]["nombre"])

print("\nListado de contactos: ")
print("-----------------------------")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("-----------------------------")
