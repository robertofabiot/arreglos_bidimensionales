# a. Pedir tamaño de la matriz
# Bucle para solicitar filas y columnas hasta que se ingresen valores válidos
while True:
    n = int(input("Filas (1-9): "))  # Solicitar número de filas
    m = int(input("Columnas (1-9): "))  # Solicitar número de columnas
    if 1 <= n < 10 and 1 <= m < 10:  # Validar que estén entre 1 y 9
        break  # Salir del bucle si son válidos
    print("Solo números entre 1 y 9.")  # Mensaje de error

# b. Ingresar los valores de la matriz
matriz = []  # Inicializar la matriz
for i in range(n):  # Iterar sobre cada fila
    fila = []  # Inicializar la fila
    for j in range(m):  # Iterar sobre cada columna
        fila.append(int(input(f"Valor [{i}][{j}]: ")))  # Pedir valor y agregar a la fila
    matriz.append(fila)  # Agregar la fila a la matriz

# c. Suma de cada fila
print("\nSuma por fila:")
for i in range(n):  # Iterar sobre cada fila
    print(f"Fila {i}: {sum(matriz[i])}")  # Imprimir la suma de la fila

# d. Promedio de cada columna
print("\nPromedio por columna:")
for j in range(m):  # Iterar sobre cada columna
    suma = 0  # Inicializar suma
    for i in range(n):  # Iterar sobre cada fila
        suma += matriz[i][j]  # Sumar el valor de la columna
    print(f"Columna {j}: {suma/n}")  # Imprimir el promedio

# e. Mayor valor y su posición
mayor = matriz[0][0]  # Inicializar mayor con el primer elemento
f = c = 0  # Inicializar posición
for i in range(n):  # Iterar sobre cada fila
    for j in range(m):  # Iterar sobre cada columna
        if matriz[i][j] > mayor:  # Comparar con el mayor actual
            mayor = matriz[i][j]  # Actualizar mayor
            f, c = i, j  # Actualizar posición
print(f"\nMayor valor: {mayor} en [{f}][{c}]")  # Imprimir el mayor valor y su posición
