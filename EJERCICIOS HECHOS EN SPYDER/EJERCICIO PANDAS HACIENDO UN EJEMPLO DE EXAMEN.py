# librerías
import matplotlib
import matplotlib.pyplot as plt

# Generar datos
# Interactuar con listas
nombreproductos=["Arroz","Azucar","Vino","Leche"]
ventaproductos=[100,50,30,20]

# Funciones que resuelven las preguntas

def totalventas():
    sumtotven=0
    for pos in range(4):
        sumtotven=sumtotven+ventaproductos[pos]
    print("El total de venta es: ",sumtotven)
    return sumtotven

def promventot():
    promven=0.0
    promven=(totalventas()/len(ventaproductos))
    return(promven)
        
# Llamar a la función
totalventas()
print("Promedio de Ventas: ",promventot())
# Generar el gráfico
fig, ax = plt.subplots()
ax.set_title("VENTAS DE LA EMPRESA")
ax.set_ylabel("Valor")
ax.set_xlabel("Nombre Producto")
#crear el gráfico
plt.bar(nombreproductos,ventaproductos)
plt.show()