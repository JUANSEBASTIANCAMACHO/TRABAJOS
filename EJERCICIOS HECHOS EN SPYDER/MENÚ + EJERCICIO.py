

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
        print(" " + str(total_suma))
    elif opcion == 2:
        promedio = float(sumar(no_notas) / no_notas)
        print("" + str(promedio))
    elif opcion == 3:
        nota_mayor = mayor_menor_nota("mayor", no_notas)
        print("" + str(nota_mayor))
    elif opcion == 4:
        nota_menor = mayor_menor_nota("menor", no_notas)
        print("" + str(nota_menor))
    elif opcion == 5:
        aprobados = estudiantes_aprobados_reprobados("", no_notas)
        print(str(aprobados) + " ")
    elif opcion == 6:
        reprobados = estudiantes_aprobados_reprobados("", no_notas)
        print(str(reprobados) + " ")
    elif opcion == 7:
        rango_notas(no_notas)
    elif opcion == 8:
        print("Cerrar")
        break
    elif opcion <= 0 and opcion >= 8:
        print("Opcion no valida")
        
        
        
    
