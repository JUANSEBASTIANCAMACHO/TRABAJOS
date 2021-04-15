a=int(input("ingresar valor de entero: "))
b=int(input("ingresar valor de entero: "))
c=int(input("ingresar valor de entero: "))
print("seleccione la organización que quiere para los numeros")
print("1 mayor a menor")
print("2 menor a mayor")
x=int(input("seleccione: "))
if(x==1):
    if(a > b and a > c and b > c):
        print(a,b,c)
    elif(b > a and b > c and a > c):
        print(b,a,c)
    elif(a > b and a > c and c > b):
        print(a,c,b)
    elif(b > c and c > a and c > a):
        print(b,c,a)
    elif(c > b and b > a and c > a):
        print(c,b,a)
    elif(c > a and a > b and c > b):
        print(c,a,b)
elif(x==2):
    if(a > b and a > c and b > c):
        print(c,b,a)
    elif(b > a and b > c and a > c):
        print(c,a,b)
    elif(a > b and a > c and c > b):
        print(b,c,a)
    elif(b > c and c > a and c > a):
        print(a,c,b)
    elif(c > b and b > a and c > a):
        print(a,b,c)
    elif(c > a and a > b and c > b):
        print(b,a,c)
else:
    print("comando no reconocido")