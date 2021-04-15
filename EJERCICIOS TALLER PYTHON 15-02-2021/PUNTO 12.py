#Calcular el sueldo total a recibir de un empleado.  El usuario deberá ingresar el número de horas trabajadas y el valor por cada hora. 
# Considere en los cálculos el descuento de seguridad social y una bonificación del 2% para aquellos cuyo sueldo no supere los 300 dólares.
horas=float(input("ingresar numero de horas trabajadas: "))
valor_hora=float(input("ingresar valor por cada hora en dolares: "))
sueldo=(horas*valor_hora)
descuento_seguridad=(sueldo*6/100)
sueldo=sueldo-descuento_seguridad
if sueldo < 300:
    sueldo=sueldo+(sueldo*2/100)
print("el sueldo total a recibir por el empleado es:",sueldo)