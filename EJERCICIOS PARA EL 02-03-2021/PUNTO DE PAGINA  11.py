#Calcular: E(x) = 1 + x = x2 2! + ... + nn n! a) Para N que es un entero leído por teclado.
#b) Hasta que N sea tal que xn /n < E (por ejemplo, E = 10–4).
n=int(input("ingrese el valor de dato: "))
for x in range(1,10):
    dato = (x^n) / n
    if dato < 1:
        break 
    else:
        continue
    print(dato)

