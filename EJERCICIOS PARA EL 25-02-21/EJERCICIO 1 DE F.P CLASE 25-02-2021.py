#Escribir un programa que seleccione la operación aritmética a ejecutar entre dos números dependiendo
# del valor de una variable denominada seleccionOp
x=int(input("ingresar valor de numero1: "))
y=int(input("ingresar valor de numero2: "))
print("los procesos de calculación: ")
print("0 suma")
print("1 resta")
print("2 multiplicacion")
print("3 division")
print("4 potencia_x")
print("5 potencia_y")
seleccionOp=int(input("ingrese el numero de proceso:")) 
if seleccionOp==0:
    operacion=x+y
elif seleccionOp==1:
    operacion=x-y
elif seleccionOp==2:
    operacion=x*y
elif seleccionOp==3:
    operacion=x/y
elif seleccionOp==4:
    operacion=x*x
elif seleccionOp==5:
    operacion=y*y
else:
    print("comando no reconocido")
print("el resultado de la operacion es: ",operacion)