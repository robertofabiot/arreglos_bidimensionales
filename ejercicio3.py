# Dos filas y cuatro columnas
matriz = [[1, 2, 3, 7],
          [4, 5, 6, 8],
]

# Linealizar la matriz por columnas
linealizada = [] # lista vacia para almacenar los elementos linealizados
for i in range(len(matriz[0])): #Bucle que itera el numero de columnas (Por medio del len)
    for j in range(len(matriz)): #Bucle que itera el numero de filas
        linealizada.append(matriz[j][i]) # Se agrega el elemento i (columna) y j (fila) a la lista linealizada

# Imprimimos la matriz original y la matriz linealizada
print("Matriz original:")
for fila in matriz:
    print(fila)

print("Matriz linealizada por columnas:")
for i in range(len(matriz) * len(matriz[0])): # Se multiplica el numero de filas por el numero de columnas
    print(linealizada[i], end=" ")
