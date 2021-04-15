#Leer las notas de una clase de informática y deducir todas aquellas que son NOTABLES (>= 7 y < 9).
notas=0
print("Ingrese numero de notas: ")
numero_notas=int(input())
for x in range(0, numero_notas):
    print("Ingrese nota del estudiante: ")
    nota=float(input())
    if  nota >= 7.0 and nota < 9.0:
        notas= notas + 1
print("la cantidad de estudiantes con notas NOTABLES son : ",notas)