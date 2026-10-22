from array import array as arr

#Parametros de la cuadricula
rows = 8
columns = 2 * rows - 1

#Creando el grid 2D
matriz = []
#Construyendo el grid (rejilla)
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matriz.append(new_row)

#Validando la construcción del grid
print(f"Cantidad de filas: {len(matriz)}")
print(f"Cantidad de columnas: {len(matriz[0])}")

for row in matriz:
    print(list(row))