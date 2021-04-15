#HECHO EN CLASE
suma = 0
med = 0.0
cantele = 0
contrep = 0
salida = False
while(salida==False):
    num = int(input("digite su valor de acuación: "))
    if(num>0):
        suma=suma+num
        cantele = cantele + 1
    else:
        salida = True
med = suma/cantele
print("el promedio es: ",med)
