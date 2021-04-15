#Escribir un programa que calcule la suma de los cuadrados de los 100 primeros números enteros.
suma100numeros= 0

numero = 1
while numero < 101:
    suma100numeros = suma100numeros + (numero ** numero)
    numero = numero + 1