from array import array as arr

#Borra pantalla con caracteres ANSI
def clear_screen():
    print("\033[2J\033]H", end="")

#ANSI color codes
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

#Parametros de la cuadricula
rows = 15
columns = 2 * rows - 1

#Función para imprimir la matriz
def print_matriz(input_matriz):
    for row in matriz:
        print(list(row))

#Creando el grid 2D
matriz = []
#Construyendo el grid (rejilla)
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matriz.append(new_row)

#Validando la construcción del grid
print(f"Cantidad de filas: {len(matriz)}")
print(f"Cantidad de columnas: {len(matriz[0])}")

#Calcular el centro de la 1° Fila
center = columns // 2 #División en enteros
#Estableciendo el centro en 1
matriz[0][center] = 1

#print_matriz(matriz)

#Se calcula el resto de la matriz
#siguiendo la lógica de sierpinsky gasket

for row in range(1,rows):
    for col in range(columns):
        left_upper_cell = 0
        right_upper_cell = 0

        #Si la columna donde estamos
        #es mayor a 0, es decir esta un elemento
        #despues del borde izquierdo
        if col > 0:
            left_upper_cell = matriz[row-1][col-1]

        #Si la columna esta un elemento antes
        #del borde derecho
        if col < columns - 1:
            right_upper_cell = matriz[row-1][col+1]
        
        #Guardando el arreglo
        if left_upper_cell != right_upper_cell:
            matriz[row][col] = 1
        else:
            matriz[row][col] = 0

def draw_matriz(input_matriz, symbol = "■"):
    for row in input_matriz:
        for cell in row:
            if cell == 1:
                print(CYAN + symbol + RESET, end="")
            else:
                print(RED + " ", end="")
        print()

draw_matriz(matriz)