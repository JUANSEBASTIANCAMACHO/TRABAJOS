#Escribir un programa que calcule la suma de los cuadrados de los 100 primeros números enteros.
suma100numeros= 0
for numero in range(1,101):
    suma100numeros = suma100numeros + (numero ** numero)
    print(numero ** numero)