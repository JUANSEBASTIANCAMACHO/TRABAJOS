#Realice un programa que simule una calculadora básica, con las operaciones: suma, resta, multiplicación, división y potencia.
x=int(input("ingresar valor de x: "))
y=int(input("ingresar valor de y: "))
print("los procesos de calculación: ")
print("0 suma")
print("1 resta")
print("2 multiplicacion")
print("3 division")
print("4 potencia_x")
print("5 potencia_y")
A=int(input("ingrese el numero de proceso:")) 
if A==0:
    operacion=x+y
elif A==1:
    operacion=x-y
elif A==2:
    operacion=x*y
elif A==3:
    operacion=x/y
elif A==4:
    operacion=x*x
elif A==5:
    operacion=y*y
else:
    print("comando no reconocido")
print("el resultado de la operacion es: ",operacion)




