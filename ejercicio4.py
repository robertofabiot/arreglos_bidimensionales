# a. Pedir tamaño de la matriz
while True:
    n = int(input("Filas (1-9): "))
    m = int(input("Columnas (1-9): "))
    if 1 <= n < 10 and 1 <= m < 10:
        break
    print("Solo números entre 1 y 9.")

# b. Ingresar los valores de la matriz
matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append(int(input(f"Valor [{i}][{j}]: ")))
    matriz.append(fila)

# c. Suma de cada fila
print("\nSuma por fila:")
for i in range(n):
    print(f"Fila {i}: {sum(matriz[i])}")

# d. Promedio de cada columna
print("\nPromedio por columna:")
for j in range(m):
    suma = 0
    for i in range(n):
        suma += matriz[i][j]
    print(f"Columna {j}: {suma/n}")

# e. Mayor valor y su posición
mayor = matriz[0][0]
f = c = 0
for i in range(n):
    for j in range(m):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            f, c = i, j
print(f"\nMayor valor: {mayor} en [{f}][{c}]")