# a. Pedir tamaño de la matriz
while True:
    n = int(input("Filas (1-9): "))  # Solicitar al usuario el número de filas de la matriz
    m = int(input("Columnas (1-9): "))  # Solicitar al usuario el número de columnas de la matriz
    # Validar que el número de filas y columnas esté entre 1 y 9
    if 1 <= n < 10 and 1 <= m < 10:  
        break  # Si los valores son válidos, salir del bucle
    print("Solo números entre 1 y 9.")  # Mensaje de error si los valores no son válidos

# b. Ingresar los valores de la matriz
matriz = []  # Inicializar una lista vacía para almacenar la matriz
for i in range(n):  # Iterar sobre cada fila de la matriz
    fila = []  # Inicializar una lista vacía para la fila actual
    for j in range(m):  # Iterar sobre cada columna de la fila
        # Pedir al usuario que ingrese un valor para la posición [i][j] de la matriz
        fila.append(int(input(f"Valor [{i}][{j}]: ")))  
    matriz.append(fila)  # Agregar la fila completa a la matriz

# c. Suma de cada fila
print("\nSuma por fila:")  # Imprimir un encabezado para la suma de filas
for i in range(n):  # Iterar sobre cada fila de la matriz
    # Calcular la suma de los elementos de la fila actual y mostrarla
    print(f"Fila {i}: {sum(matriz[i])}")  

# d. Promedio de cada columna
print("\nPromedio por columna:")  # Imprimir un encabezado para el promedio de columnas
for j in range(m):  # Iterar sobre cada columna de la matriz
    # Calcular la suma de los elementos de la columna actual
    suma = sum(matriz[i][j] for i in range(n))  
    # Calcular el promedio dividiendo la suma por el número de filas y mostrarlo
    print(f"Columna {j}: {suma/n:.2f}")  

# e. Mayor valor y su posición
mayor = matriz[0][0]  # Inicializar la variable mayor con el primer elemento de la matriz
f = c = 0  # Inicializar las variables para la posición del mayor valor
for i in range(n):  # Iterar sobre cada fila de la matriz
    for j in range(m):  # Iterar sobre cada columna de la fila
        # Comparar el elemento actual con el mayor encontrado hasta ahora
        if matriz[i][j] > mayor:  
            mayor = matriz[i][j]  # Actualizar el mayor si se encuentra un nuevo valor
            f, c = i, j  # Actualizar la posición del mayor valor
# Imprimir el mayor valor encontrado y su posición en la matriz
print(f"\nMayor valor: {mayor} en [{f}][{c}]")  

# f. Mostrar la matriz como cuadro simple
print("\nMatriz:")  # Imprimir un encabezado para mostrar la matriz
for fila in matriz:  # Iterar sobre cada fila de la matriz
    # Imprimir cada fila, uniendo los valores con un espacio
    print(" ".join(str(valor) for valor in fila))  
