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
