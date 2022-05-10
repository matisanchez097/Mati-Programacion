"""
Ejercicio 4:
    Pedir dos numeros al usuario y hacer todas las operaciones basicas de una calculadora y mostrarlo en pantalla.

"""
print("########## CALCULADORA ##########")

print("Ingresa el tipo de operacion que deseas realizar:")
print("Suma: 1 | Resta: 2 | Multiplicacion: 3 | Division: 4")

calculo = int(input("Introduce el numero que corresponda al tipo de operacion que deseas realizar : "))

if calculo == 1:
    num1 = int(input("Escribe el primer numero que quieres sumar: "))
    num2 = int(input("Escribe el segundo numero que quieres sumar: "))
    resultado = num1+num2
    print(f"El resultado de tu suma es {resultado}")
elif calculo == 2:
    num1 = int(input("Escribe el primer numero que quieres restar: "))
    num2 = int(input("Escribe el segundo numero que quieres restar: "))
    resultado = num1-num2
    print(f"El resultado de tu resta es {resultado}")
elif calculo == 3:
    num1 = int(input("Escribe el primer numero que quieres multiplicar: "))
    num2 = int(input("Escribe el segundo numero que quieres multiplicar: "))
    resultado = num1*num2
    print(f"El resultado de tu multiplicacion es {resultado}")
elif calculo == 4:
    num1 = int(input("Escribe el primer numero que quieres dividir: "))
    num2 = int(input("Escribe el segundo numero que quieres sumar: "))
    resultado = num1/num2
    print(f"El resultado de tu división es {resultado}")
else:
    print("El numero ingresado es incorrecto, vuelva a introducir un numero!!")