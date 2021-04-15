#Un comercio dispone de dos tipos de artículos en fichas correspondientes a diversas sucursales con los siguientes campos:
#• código del artículo A o B, • precio unitario del artículo, • número de artículos. 
# La última ficha del archivo de artículos tiene un código de artículo, una letra X. Se pide: 
# • el número de artículos existentes de cada categoría, • el importe total de los artículos de cada categoría.
articulo_a=0
articulo_b=0
total_a=0
total_b=0

articulo_a=input("ingrese el código del artículo a: ")
articulo_b=input("ingrese el código del artículo b: ")

codigo_articulo_a=articulo_a[-1]
codigo_articulo_b=articulo_b[-1]

if codigo_articulo_a == "x" and codigo_articulo_b == "x":
    precio_unitario=int(input("ingrese el precio unitario: "))
    numero_articulos=int(input("ingrese el numero de articulo: "))