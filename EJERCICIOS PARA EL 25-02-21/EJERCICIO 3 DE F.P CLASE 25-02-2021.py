#Escribir un algoritmo que visualice el siguiente doble mensaje Introduzca un mes (1 para Enero, 2 para Febrero,…) 
# Introduzca un día del mes El algoritmo acepta y almacena un número en la variable mes en respuesta a la primera pregunta y 
# acepta y almacena un número en la variable dia en respuesta a la segunda pregunta. Si el mes introducido 
# no está entre 1 y 12 inclusive, se debe visualizar un mensaje de información al usuario advirtiéndole de que el número introducido no es válido como mes; de 
# igual forma se procede con el número que representa el día del mes si no está en el rango entre 1 y 31. 
# Modifique el algoritmo para prever que el usuario introduzca números con decimales. Nota: como los años bisiestos, febrero tiene 29 
# días, modifique el programa de modo que advierta al usuario si introduce un día de mes que no existe (por ejemplo, 30 o 31). Considere también el hecho de que
# hay meses de 30 días y otros meses de 31 días, de modo que nunca se produzca error de in troducción 
# de datos o que en su defecto se visualice un mensaje al usuario advirtiéndole del error cometido.
mes = int(input("Introduzca el mes: "))
dia = int(input("Digite el dia: "))
year = int(input("Introduzca el año: "))

if mes >= 1 and mes <= 12:
    if year % 4 == 0:
        if mes == 2:
            if dia >= 1 and dia <= 29:
                print("dia valido")
            else:
                print("dia no valido")
        if mes % 2 == 1:
            if dia >= 1 and dia <= 31:
                print("dia valido")
            else:
                print("dia no valido")
        else:
            print("dia valido")
    else:
        print("el mes no es bisiestro")
else:
    print("mes no valido")