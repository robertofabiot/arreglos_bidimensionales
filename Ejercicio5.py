# Definimos el arreglo bidimensional
# Filas: Vendedores (3)
# Columnas: Zonas (4)
ventas = [
    [10, 20, 30, 40],  # Vendedor 1
    [15, 25, 35, 5],   # Vendedor 2
    [20, 10, 5, 15]    # Vendedor 3
]

# a. Encontrar la zona en la que más computadores se vendieron
suma_zonas = [sum(ventas[vendedor][zona] for vendedor in range(3)) for zona in range(4)]
zona_maxima = suma_zonas.index(max(suma_zonas)) + 1  # +1 para mostrar la zona en formato 1, 2, 3, 4
max_ventas = max(suma_zonas)

# b. Encontrar el vendedor que menos computadores vendió
suma_vendedores = [sum(ventas[vendedor]) for vendedor in range(3)]
vendedor_minimo = suma_vendedores.index(min(suma_vendedores)) + 1  # +1 para mostrar el vendedor en formato 1, 2, 3
min_ventas = min(suma_vendedores)

# c. Calcular la cantidad total de computadores vendidos
total_ventas = sum(suma_vendedores)

# Mostrar resultados
print(f"La zona en la que más computadores se vendió es la zona {zona_maxima} con {max_ventas} ventas.")
print(f"El vendedor que menos computadores vendió es el vendedor {vendedor_minimo} con {min_ventas} ventas.")
print(f"La cantidad total de computadores vendidos por todos los vendedores en todas las zonas es {total_ventas}.")
