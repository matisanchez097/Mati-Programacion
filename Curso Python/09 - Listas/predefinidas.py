cantantes = ["2pac", "Drake", "Bad Bunny", "Julio Iglesias"]
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar una lista
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos
cantantes.append("Alex Ubago")
cantantes.insert(1,"david bisbal")

print(cantantes)

# Eliminar Elementos
cantantes.pop(1)
cantantes.remove("Bad Bunny")
print(cantantes)

# Dar la vuelta
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print("Drake" in cantantes)

# Contar elementos
print(len(cantantes))

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("Drake"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)