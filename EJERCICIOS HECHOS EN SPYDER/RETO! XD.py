# Lectura de archivos tipo excel
# Importar librerías
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt 

# Leer archivo excel

archivoexcel = pd.read_excel("C:/Users/Usuario/Desktop/COSAS EXCEL/POBLACIÓN Y AREA DEPART-COLOMBIA.xlsx")

# Imprimir los datos


# DESARROLLAR LO QUE NOS PIDEN

# 2.1 ARE TOTAL DE TODO EL PAÍS (km^2)
area_total=0
cantidad_datos=0
area=archivoexcel["Area_km_al_cuad"]
for x in area:
    area_total = area_total + (x)
    cantidad_datos=cantidad_datos+1
print("2.1 el Area total de todo el país es: ",area_total+cantidad_datos-33)

#2.2 PROMEDIO DE AREA X DEPARTAMENTO(km^2)
suma_poblacion=0
numero_departamentos=0
poblacion=archivoexcel["Area_km_al_cuad"]
for x in poblacion:
    suma_poblacion = suma_poblacion + (x)
    numero_departamentos=numero_departamentos+1
   
print("2.2 el Promedio de Area x Departamento es: ",suma_poblacion/numero_departamentos)

#2.3 DEPARTAMENTO CON MAYOR POBLACIÓN y 2.4 DEPARTAMENTO CON MENOR POBLACIÓN
menoramayor=archivoexcel.sort_values(by=['Poblation'],ascending=[True])
print("ORDEN DE MENOR A MAYOR Y VICEVERSA",menoramayor)


#2.5 PROMEDIO DE POBLACIÓN 
suma_poblacion=0
departamentos=0
poblacion=archivoexcel["Poblation"]
for x in poblacion:
    suma_poblacion = suma_poblacion + (x)
    departamentos=departamentos+1
   
print("2.5 el Promedio de población es: ",suma_poblacion/numero_departamentos)

#2.6
print("HABITANTES X KILÓMETRO AL CUADRADO: ")
print(area*poblacion)

#3.1,2,3,4,5,6
fig, ax = plt.subplots()
ax.set_title("Departament and Poblation")
ax.set_ylabel("Departament")
ax.set_xlabel("Poblation")

#crear el gráfico
plt.barh(archivoexcel['Department'],archivoexcel['Poblation'])
plt.show()
plt.pie(archivoexcel['Poblation'],labels=archivoexcel['Departament'])
plt.show()