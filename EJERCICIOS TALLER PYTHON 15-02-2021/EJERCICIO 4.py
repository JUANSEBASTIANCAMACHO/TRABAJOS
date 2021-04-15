#Realice un programa que obtenga la calificación que debe obtenerse en un examen supletorio, 
#si se conoce que el promedio incluido el supletorio para aprobar debe ser mínimo de 3.5 . 
#El usuario debe ingresar las calificaciones en números enteros del primer y segundo bimestre.
examen=float(input("ingresar valor de calificación: "))
primer=float(input("ingresar valor de primer: "))
segundo=float(input("ingresar valor de segundo: "))
notaf=(examen + primer + segundo)
notaf=(notaf/3)
if(notaf >= 3.5):
    print("gano academicamente ")
elif(notaf < 3.5):
    print("perdió academicamente  ")
print("el promedio de esta persona es: ",notaf)


