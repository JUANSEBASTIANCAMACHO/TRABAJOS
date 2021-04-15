# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("sistema de notas de un curso de programación")

#entrada

numeroestudiantes=int(input("digite la cantidad de estudiantes del grupo : "))


#declarar la variable que controla el ciclo
contadorrepeticiones = 0
cantidadestudiantesaprobaron = 0
cantidadestudiantesreprobaron = 0
sumadefintivaestudiantes = 0

sumadefinitivaestudiantesaprobaron = 0
sumadefinitivaestudiantesreprobaron = 0

promediodefinitivaestudiantesaprobaron = 0.0
promediodefinitivaestudiantesreprobaron = 0.0

promediodefinitivaestudiantes = 0.0

#proceso
#iniciar el ciclo


while contadorrepeticiones < numeroestudiantes:
    #
    notaunoestudiante = float(input("digite la nota del primer parcial : "))
    notadosestudiante = float(input("digite la nota del segundo parcial : "))
    notatresestudiante = float(input("digite la nota del tercer parcial : "))
    #calcular la definitiva de cada estudiante
    notadefinitiva = (notaunoestudiante+notadosestudiante+notatresestudiante)/3
    
    sumadefintivaestudiantes=sumadefintivaestudiantes+notadefinitiva
    print("la definitiva es: ", notadefinitiva)
    
    if(notadefinitiva>=3.0):
        cantidadestudiantesaprobaron = cantidadestudiantesaprobaron+1
        #sumar las notas de los que aprobaron
        sumadefintivaestudiantesaprobaron = sumadefinitivaestudiantesaprobaron+notadefinitiva
    else:
        cantidadestudiantesreprobaron = cantidadestudiantesreprobaron+1 
        sumadefintivaestudiantesreprobaron = sumadefinitivaestudiantesreprobaron+notadefinitiva
    #incrementar la variable que controla el ciclo
    contadorrepeticiones = contadorrepeticiones+1
    
#ciclo
#promedios
promediodefinitivaestudiantes = sumadefintivaestudiantes/numeroestudiantes

if(cantidadestudiantesaprobaron>0):
    promediodefinitivaestudiantesaprobaron = sumadefinitivaestudiantesaprobaron/cantidadestudiantesaprobaron
if(cantidadestudiantesreprobaron>0):
    promediodefinitivaestudiantesreprobaron = sumadefinitivaestudiantesreprobaron/cantidadestudiantesreprobaron
print ("otros calculos")
print("2. cantidad de estudiantes que aprobaron : ", cantidadestudiantesaprobaron)
print("3. cantidad de estudiantes que reprobaron : ", cantidadestudiantesreprobaron)
print(f"4  promedio del grupo : {promediodefinitivaestudiantes: .2f} ")
print("5  promedio de las notas de los estudiantes que aprobaron : ",promediodefinitivaestudiantesaprobaron)
print(f"6  promedio de las notas de los estudiantes que reprobaron :{promediodefinitivaestudiantesreprobaron: .1f} ")