""""
Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla. 
Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos que 
hay entre un número y uno.  Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.
"""
#Se crea una variable solicitando al usuario un número 
num= int(input("Ingrese un número: "))
#Se decreta que factorial es igual a 1
factorial = 1
if num !=0:
    #Se hace un for range con el número +1 para que incluya el número
    for i in range(1, (num + 1)):
        #Se crea un variable que decreta que factorial es igual a factorial por i(rango)
        factorial = factorial * i
        #Se usa la función print para mostrar resultados
        print("Factorial de {0} es: {1}".format(num, factorial))
#Sí el usuario ingresa un número igual a 0, se señala que debe ser mayor que 0
else:
    print("Debe ser un número mayor a 0")
    