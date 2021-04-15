#Imprimir todos los números primos entre 2 y 1.000 inclusive.
n_primos = [2]
m = 1000
for x in range(3, m):
    for i in range(2, x):
        if x%i != 0:
            continue
        else:
            break
    else:
        print ('%d es primo'%x)
        n_primos.append(x)
F = open('numerosprimos.txt', 'w')
for data in n_primos:
    F.write('%d\n'%data)
