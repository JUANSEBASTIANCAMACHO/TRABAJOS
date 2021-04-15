#Leer 100 números. Determinar la media de los números positivos y la media de los números negativos
contador_par=0
contador_inpar=0
contador_numeros_pares=0
contador_numeros_inpares=0
for x in range(1,101):
    if x%2 == 0:
        contador_par = contador_par + x 
        contador_numeros_pares = contador_numeros_pares + 1
    if x%2 == 1:
        contador_inpar = contador_inpar + x
        contador_numeros_inpares = contador_numeros_inpares + 1

print(contador_par/contador_numeros_pares)
print(contador_inpar/contador_numeros_inpares)
