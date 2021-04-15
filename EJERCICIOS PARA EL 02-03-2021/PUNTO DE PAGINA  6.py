#Se desea leer las calificaciones de una clase de informática y contar el número total de aprobados (5 o mayor que 5).
calificaciones=0
print("Ingrese numero de estudiantes: ")
numero_estudiantes=int(input())
for x in range(0, numero_estudiantes):
    print("Ingrese nota del estudiante: ")
    nota=float(input())
    if nota >= 5.0:
        calificaciones= calificaciones + 1
print("la cantidad de estudiantes aprovados es : ",calificaciones)