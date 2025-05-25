# 2. Se desea realizar un programa en donde se capture el nombre y tres calificaciones para 
# 5 estudiantes de la facultad de Ingeniería, y después se pueda procesar dándonos el 
# promedio final de cada uno de los alumnos, el resultado se mostrará en pantalla. 

#Se crea una matriz 5x4
calificaciones_estudiantes = []

for fila in range(5):
    nueva_fila = []
    for columna in range(4): #Si es la columna 0, pide y agrega el nombre, si no, la calificación
        if columna == 0:
            nombre = input("Ingrese el nombre del estudiante: ")
            nueva_fila.append(nombre)
        else:
            calificacion = float(input(f"Ingrese la calificación {columna}: "))
            nueva_fila.append(calificacion)
    calificaciones_estudiantes.append(nueva_fila) #Agrega la fila creada a la matriz

#Evaluar cada fila y obtener el promedio, sumando del índice 1 al 3 de cada una y dividiendo entre 3
for fila in calificaciones_estudiantes:
    print(f"El estudiante {fila[0]} tiene un promedio de {(sum(fila[1:4])/3):.2f}")
