#Imprimir las treinta primeras potencias de 10, es decir, 10 elevado a 1, 10 elevado a 2, etc. además sumar las potencias calculadas

suma = 0 

numero = 1
while numero < 31:
    suma = suma + (numero ** 10)
    numero = numero + 1

print(suma)