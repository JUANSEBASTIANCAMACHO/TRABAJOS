"""
Menu:
1. Sumar
2. Promedio
3. Mayor dato y su ubicacion 
4. Menor dato y su ubicacion
5. Cuantos estudiantes aprobaron
6. Cuentos estudiantes reprobaron
7. Cuantos estudiantes tuvieron el rango de (0-1) (1-2)
8. Salir
"""

def sumar(no_notas):
    suma = 0
    for i in range(1, no_notas + 1):
        while True:
            nota = int(input("Digite la nota " + str(i) + ": "))
            if nota >= 0 and nota <= 5:
                suma = suma + nota
                break
            else:
                print("Nota no valida")
                
    return suma

def mayor_menor_nota(condicion, no_notas):
    notas = []
    for i in range(1, no_notas + 1):
        while True:
            nota = int(input("Digite la nota " + str(i) + ": "))
            if nota >= 0 and nota <= 5:
                notas.append(nota)
                break
            else:
                print("Nota no valida")
                
    if condicion == "mayor":
        data = max(notas)
    elif condicion == "menor":
        data = min(notas)
    
    return data

def estudiantes_aprobados_reprobados(condicion, no_notas):
    aprobados = 0
    reprobados = 0
    for i in range(1, no_notas + 1):
        while True:
            nota = int(input("Digite la nota " + str(i) + ": "))
            if nota >= 0 and nota <= 5:
                if nota >= 3:
                    aprobados = aprobados + 1
                else:
                    reprobados = reprobados + 1
                break
            else:
                print("Nota no valida")
            
    if condicion == "aprobado":
        data = aprobados
    elif condicion == "reprobado":
        data = reprobados
    
    return data

def rango_notas(no_notas):
    rango1 = 0
    rango2 = 0
    rango3 = 0
    rango4 = 0
    rango5 = 0
    for i in range(1, no_notas + 1):
        while True:
            nota = float(input("Digite la nota " + str(i) + ": "))
            if nota >= 0 and nota <= 5:
                if nota >= 0 and nota <= 1:
                    rango1 = rango1 + 1
                elif nota >= 1.1 and nota <= 2:
                    rango2 = rango2 + 1
                elif nota >= 2.1 and nota <= 3:
                    rango3 = rango3 + 1
                elif nota >= 3.1 and nota <= 4:
                    rango4 = rango4 + 1
                elif nota >= 4.1 and nota <= 5:
                    rango5 = rango5 + 1
                break
            else:
                print("Nota no valida")
                
    print("El numero de almunos entre 0 y 1 es : ", rango1)
    print("El numero de almunos entre 1.1 y 2 es : ", rango2)
    print("El numero de almunos entre 2.1 y 3 es : ", rango3)
    print("El numero de almunos entre 3.1 y 4 es : ", rango4)
    print("El numero de almunos entre 4.1 y 5 es : ", rango5)
            
# ya esta el codigo sino que el micro ta malo
# chao

while True:
    print("------------------") 
    print("1. Sumar")
    print("2. Promedio")
    print("3. Mayor dato y su ubicacion")
    print("4. Menor dato y su ubicacion")
    print("5. Cuantos estudiantes aprobaron")
    print("6. Cuentos estudiantes reprobaron")
    print("7. Cuantos estudiantes tuvieron el rango de (0-1) (1-2)")
    print("8. Salir")
    print("------------------")
    opcion = int(input("Digite el numero correspondiente: "))
    no_notas = int(input("Digite la cantidad de notas: "))
    if opcion == 1:
        total_suma = sumar(no_notas)
        print("La suma da: " + str(total_suma))
    elif opcion == 2:
        promedio = float(sumar(no_notas) / no_notas)
        print("El promedio da: " + str(promedio))
    elif opcion == 3:
        nota_mayor = mayor_menor_nota("mayor", no_notas)
        print("La mayor nota es: " + str(nota_mayor))
    elif opcion == 4:
        nota_menor = mayor_menor_nota("menor", no_notas)
        print("La menor nota es: " + str(nota_menor))
    elif opcion == 5:
        aprobados = estudiantes_aprobados_reprobados("aprobado", no_notas)
        print(str(aprobados) + " estudiantes aprobaron")
    elif opcion == 6:
        reprobados = estudiantes_aprobados_reprobados("reprobado", no_notas)
        print(str(reprobados) + " estudiantes reprobaron")
    elif opcion == 7:
        rango_notas(no_notas)
    elif opcion == 8:
        print("Cerrar")
        break
    elif opcion <= 0 and opcion >= 8:
        print("Opcion no valida")
    
