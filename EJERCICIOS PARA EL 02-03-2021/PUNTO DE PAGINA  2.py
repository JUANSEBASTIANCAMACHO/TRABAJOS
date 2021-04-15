#HECHO EN CLASE
Tabla = 0
multiplicador = 1
resultado = 0
sumaresultado = 0
conrepciclo = 1
tabla = int(input("tabla: "))
multiplicador = int(input("Multiplicador: "))
while(conrepciclo <= multiplicador):
    resultado = tabla * conrepciclo
    sumaresultado = sumaresultado + resultado
    print(tabla, "*", conrepciclo, "=", resultado)
    conrepciclo = conrepciclo + 1
print("la suma de los resultados es: ", sumaresultado)

