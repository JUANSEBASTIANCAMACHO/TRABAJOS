#Escribir un programa que genere aleatoriamente 100 datos y sume todos los números, los negativos, los positivos y calcule el promedio de todos los números, de los positivos y los negativos; además que calcule el mayor y el menor de todos los números, de los positivos y los negativos

import random

cant_positivos = 0
cant_negativos = 0

positivos = 0
negativos = 0

numeros = []

for numero in range(1,101):
    dato = random.randrange(1, 100)
    numeros.append(dato)
    if dato % 2 == 0:
        positivos = positivos + dato
        cant_positivos = cant_positivos + 1
    else:
        negativos = negativos + dato
        cant_negativos = cant_negativos + 1

promedio_positivos = positivos / cant_positivos
promedio_negativos = negativos / cant_negativos
numero_menor = min(numeros)
numero_mayor = max(numeros)

print("El promedio de los positivos es: " + str(promedio_positivos))
print("El promedio de los negativos es: " + str(promedio_negativos))

print("El numero menor es: " + str(numero_menor))
print("El numero mayor es: " + str(numero_mayor)) 