"""
Ejercicio 10:
    El programa tiene que pedir la nota de 15 alunmos y sacar
    por pantalla cuantos han aprobado y cuantos han suspendido!

"""
contador = 1
desaprobados = 0
aprobados = 0

numero_alumnos = int(input(f"Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    alumno = str(input("Introduzca el Nombre del alumno/a: "))
    nota = int(input(f"Que nota le queres poner al alunmo/a?: "))
    print(f"El alumno {alumno} Se ha agregado con éxito!")
    
    if nota >= 5:
        aprobados += 1
    else:
        desaprobados += 1
    contador += 1

print(f"Alumnos Aprobados: {aprobados}")
print(f"Alumnos desaprobados: {desaprobados}")