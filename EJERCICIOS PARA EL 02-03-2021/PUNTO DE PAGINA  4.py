#Determinar la media de una lista de números positivos terminada con un número no positivo después del último número válido.
suma = 0
cont = 0
print("Introduzca un número positivo (número negativo para terminar): ")
x=int(input())
while x >= 0:
    suma = suma + x
    cont = cont + 1
    print("Introduzca un número positivo (número negativo para terminar): ")
    x=int(input())
media = suma / cont
print("La media de los números introducidos es: ", media)
