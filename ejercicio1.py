# 1. La Abarrotera ABSA tiene 4 sucursales en las cuales se realizaron diferentes ventas en los 
# meses de Julio a diciembre del año 2022, se le ha solicitado a usted realizar un programa en 
# donde pueda capturar la siguiente tabla de datos
# y nos presente los siguientes resultados: 
# a. Venta total por todas las tiendas 
# b. Venta total por tienda 
# c. Tienda que más vendió en los 6 meses 
# d. Tienda que menos vendió 

#Crear arreglo
estado_de_cuenta = [
    ["Tienda/Mes", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    ["ABSA 1", 50000, 60000, 65000, 62000, 78000, 95000],
    ["ABSA 2", 89000, 90000, 98000, 80000, 85000, 90000],
    ["ABSA 3", 65000, 72000, 85000, 72000, 83000, 98000],
    ["ABSA 4", 92000, 88000, 90000, 76000, 82000, 93000]
]

#Venta total por todas las tiendas
venta_total = 0

for fila in range(1, len(estado_de_cuenta)): #Evalúa para cada fila a partir de la 1
    for columna in range(1, len(estado_de_cuenta[1])): #Evalúa para cada columna a partir de la 1
        venta_total += (estado_de_cuenta[fila])[columna]

#Venta total por tienda
venta_por_tienda = [0]*4 #Crea una lista para almacenar los valores

for fila in range(1, len(estado_de_cuenta)): #Evalúa para cada fila a partir de la 1
    for columna in range(1, len(estado_de_cuenta[1])): #Evalúa para cada columna a partir de la 1
        venta_por_tienda[fila-1] += (estado_de_cuenta[fila])[columna] #Suma a la lista

#Tienda que más vendió en los 6 meses
tienda_mayor_venta = f"ABSA {venta_por_tienda.index(max(venta_por_tienda)) + 1}" #Obtiene el índice del valor máx + 1 y lo almacena junto con ABSA

#Tienda que menos vendió
tienda_menor_venta = f"ABSA {venta_por_tienda.index(min(venta_por_tienda)) + 1}" #Obtiene el índice del valor min + 1 y lo almacena junto con ABSA

#Imprimir resultados
print(f"La venta total fue {venta_total}")

for i in range(len(venta_por_tienda)): #Imprime la venta total por tienda
    print(f"La tienda ABSA {i+1} vendió {venta_por_tienda[i]}")

print(f"La tienda que más vendió en los 6 meses fue {tienda_mayor_venta}")
print(f"La tienda que menos vendió en los 6 meses fue {tienda_menor_venta}")