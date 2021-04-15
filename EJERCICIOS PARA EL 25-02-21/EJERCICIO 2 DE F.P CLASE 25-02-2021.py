#Escribir un programa que acepte dos números reales de un usuario y un código de selección. Si el código 
# introducido de selección es 1, entonces el programa suma los dos números introducidos previamente y se 
# visualiza el resultado; si el código de selección es 2, los números deben ser multiplicados y visualizado
# el resultado; y si el código seleccionado es 3, el primer número se debe dividir por el segundo número y visualizarse el resultado.
x=float(input("ingresar valor de numero1: "))
y=float(input("ingresar valor de numero2: "))
print("los procesos de calculación: ")
print("1 suma")
print("2 multiplicacion")
print("3 division")
codigo_seleccion=int(input("ingrese el numero de proceso:"))
if codigo_seleccion==1:
    operacion=x+y
elif codigo_seleccion==2:
    operacion=x*y
elif codigo_seleccion==3:
    operacion=x/y
print("el resultado de la operacion es: ",operacion)

