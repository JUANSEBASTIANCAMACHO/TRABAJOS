# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:49:06 2021

@author: Usuario
"""
# 1
matriznumeros=[[12,32,56,48],[8,48,18,58],[2,4,6,8]]


#2
print(matriznumeros)

#3
print("posición especifica:", matriznumeros[0][2])

#4
fil=int(input("fila: "))
col=int(input("columna: "))
print("posición leida por teclado: ", matriznumeros[fil-1][col-1])


#5
print("fila 0:", matriznumeros[0])
print("fila 1:", matriznumeros[1])
print("fila 2:", matriznumeros[2])

#6
for f in range(3):
    print(matriznumeros[f][1])

#7    
col=int(input("columna que desea imprimir: "))
for f in range(3):
    print(matriznumeros[f][col])
    
#8
sumelemat=0
for f in range(3):
    for c in range(4):
        sumelemat=sumelemat+matriznumeros[f][c]
print("la suma de los elementos es: ",sumelemat)




#9
print("sumar e imprimir los elementos de cada fila")
sumelemat=0
for f in range(3):
    for c in range(4):
        sumelemat=sumelemat+matriznumeros[f][c]
    print("la suma de los elementos es: ",sumelemat)
    sumelemat
    
   
        