#Imprimir las treinta primeras potencias de 10, es decir, 10 elevado a 1, 10 elevado a 2, etc. además sumar las potencias calculadas

suma = 0 

for numero in range(1,31):
    suma = suma + (numero ** 10)

print(suma)
    