#Realice un programa que resuelva lo siguiente: Si "n" Empleados  realizan una actividad en k horas, 
#¿cuántos empleados se necesitarán para realizar la misma actividad en k1 horas?
empleados=float(input("ingresar el numero de empleados: "))
horas=float(input("ingresar numero de horas trabajadas: "))
horasne=float(input("ingresar el numero de horas necesarias para realizar su actividad: "))
n=empleados/horas*horasne
print("cantidad de empleados necesarios: ",n)


