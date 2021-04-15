#Realice un programa que obtenga el índice de masa corporal de una persona, ingresando la estatura en centímetros y el peso en kilos.
estatura=int(input("ingresar valor de estatura en centimetros: "))
peso=int(input("ingresar valor de peso en kilos: "))
estatura=estatura/100
masa=peso/(estatura*estatura)
print("el IMC de esta persona es: ",masa)