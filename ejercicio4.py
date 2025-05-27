# a. Solicitar el ingreso de n y m, según las restricciones indicadas.
while True:
    n = int(input("Ingrese el número de filas (1-9): "))  # Solicitar número de filas
    m = int(input("Ingrese el número de columnas (1-9): "))  # Solicitar número de columnas
    # Validar que n y m estén entre 1 y 9
    if 1 <= n < 10 and 1 <= m < 10:  
        break  # Salir del bucle si los valores son válidos
    print("Por favor, ingrese números entre 1 y 9.")  # Mensaje de error

# b. Ingresar cada uno de los valores de la matriz
matriz = []  # Inicializar la matriz
for i in range(n):  # Iterar sobre cada fila
    fila = []  # Inicializar la fila
    for j in range(m):  # Iterar sobre cada columna
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))  # Pedir valor
        fila.append(valor)  # Agregar el valor a la fila
    matriz.append(fila)  # Agregar la fila a la matriz

# c. Mostrar, para cada fila, la suma de sus valores
print("\nSuma por fila:")
for i in range(n):  # Iterar sobre cada fila
    suma_fila = sum(matriz[i])  # Calcular la suma de la fila
    print(f"Suma de la fila {i}: {suma_fila}")  # Imprimir la suma

# d. Mostrar, para cada columna, el promedio de sus valores
print("\nPromedio por columna:")
for j in range(m):  # Iterar sobre cada columna
    suma_columna = sum(matriz[i][j] for i in range(n))  # Calcular la suma de la columna
    promedio_columna = suma_columna / n  # Calcular el promedio
    print(f"Promedio de la columna {j}: {promedio_columna:.2f}")  # Imprimir el promedio

# e. El mayor valor almacenado en toda la matriz, indicando en qué fila y columna se encuentra
mayor = matriz[0][0]  # Inicializar mayor con el primer elemento
fila_mayor = 0  # Inicializar fila del mayor valor
columna_mayor = 0  # Inicializar columna del mayor valor
for i in range(n):  # Iterar sobre cada fila
    for j in range(m):  # Iterar sobre cada columna
        if matriz[i][j] > mayor:  # Comparar con el mayor actual
            mayor = matriz[i][j]  # Actualizar mayor
            fila_mayor, columna_mayor = i, j  # Actualizar posición
# Imprimir el mayor valor encontrado y su posición
print(f"\nEl mayor valor en la matriz es: {mayor} en la posición [{fila_mayor}][{columna_mayor}]")
