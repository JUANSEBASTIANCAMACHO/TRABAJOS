#Se desea conocer una serie de datos de una empresa con 50 empleados: a) ¿Cuántos empleados ganan 
#más de 300.000 pesetas al mes (salarios altos); b)entre 100.000 y 300.000 pesetas (salarios medios); 
#y c) menos de 100.000 pesetas (salarios bajos y empleados a tiempo parcial)?
empleados_altos=0
empleados_medios=0
empleados_bajos=0
for x in range(1,51):
    salario=int(input("digite el salario del empleado: "))
    if salario >= 300000:
        empleados_altos=empleados_altos + 1
    elif salario >= 100000 and salario <= 300000:
        empleados_medios=empleados_medios + 1
    else:
        empleados_bajos=empleados_bajos + 1

print(str(empleados_altos) + "Tienen el salario alto")

print(str(empleados_medios) + "Tienen el salario medio")

print(str(empleados_bajos) + "Tienen el salario bajo")
