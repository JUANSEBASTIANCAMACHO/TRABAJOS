#Calcular el enésimo término de la serie de Fibonacci definida por: A1 = 1 A2 = 2 A3 = 1 + 2 = A1 + A2 An = An – 1 + An – 2 (n >= 3)
print("Teclee un número: ")
n=int(input())
A1 = 1
A2 = 2
i=3
if (n == 1):
    print(A1)
else:
    if (n == 2):
        print(A2)
    else:
        for i in range(i, n):
            aux = A2
            A2 = A1 + A2
            A1 = aux
        print(A2)
