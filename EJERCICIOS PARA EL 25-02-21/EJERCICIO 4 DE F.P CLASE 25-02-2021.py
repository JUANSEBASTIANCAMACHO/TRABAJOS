#Escriba un programa que simule el funcionamiento normal de un ascensor (elevador) moderno con 25 
# pisos (niveles) y que posee dos botones de SUBIR y BAJAR, excepto en el piso (nivel) inferior, que sólo 
# existe botón de llamada para SUBIR y en el último piso (nivel) que sólo existe botón de BAJAR.
piso = 1

while True:

    if piso == 1:
        input("Digite 1 para subir: ")
        piso = piso + 1
    elif piso == 25:
        input("Digite 1 para baje: ")
        piso = piso - 1
    elif piso >= 2 and piso <= 24:
        caso = int(input("Digite 1 para subir Digite 2 para bajar: "))
        if caso == 1:
            piso = piso + 1
        elif caso == 2:
            piso = piso - 1

    print(piso)
            

        


