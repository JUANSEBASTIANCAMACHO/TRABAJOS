#Calcular el valor a pagar de una compra realizada, cuyo monto neto es ingresado por el usuario. 
# Considere que el valor del IVA (Impuesto al Valor Agregado- puede variar en cada país), 
# y un descuento del 5% para todas las compras.
valor=int(input("ingresar valor de la compra:"))
print("ingrese el país en el que está comprando")
print("0 españa")
print("1 alemania")
print("2 reino unido")
print("3 francia")
print("4 italia")
A=int(input("ingrese numero:"))
descuento=(valor*5/100)
if A==0:
    IVA=(21*valor/100)
    total=valor+IVA-descuento
elif A==1:
    IVA=(19*valor/100)
    total=valor+IVA-descuento
elif A==2:
    IVA=(20*valor/100)
    total=valor+IVA-descuento
elif A==3:
    IVA=(20*valor/100)
    total=valor+IVA-descuento
elif A==4:
    IVA=(22*valor/100)
    total=valor+IVA-descuento
else:
    print("comando no reconocido")
print(total)
 