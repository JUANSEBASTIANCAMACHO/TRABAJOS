# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:54:58 2021

@author: Usuario
"""

import random

cantidadnumeros=1
contadorepetidores=0
numero=0
acumuladorsumatodosnumeros=0
acumuladorsumanumerospositivos=0
acumuladorsumanumerosnegativos=0

cantidadnumeros=int(input("cantidad de numeros: "))

while contadorepetidores<cantidadnumeros:
    numero=random.randint(-100, 100)
    print("numero: ",numero)
    acumuladorsumatodosnumeros=acumuladorsumatodosnumeros+numero
    if numero>0:
        acumuladorsumanumerospositivos=acumuladorsumanumerospositivos+numero
    else:
        acumuladorsumanumerosnegativos=acumuladorsumanumerosnegativos+numero
    contadorepetidores=contadorepetidores+1
    
print("suma todos: ", acumuladorsumatodosnumeros)
print("suma positivos: ", acumuladorsumanumerospositivos)
print("suma negativos: ", acumuladorsumanumerosnegativos)