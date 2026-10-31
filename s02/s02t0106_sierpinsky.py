from array import array as arr
from enum import Enum
import os

#Borra pantalla con caracteres ANSI
#dependiendo del sistema operativo
#nt = Windows ; posix = Linux / macOS
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    #print("\033[2J\033[H", end="")

#Encapsulado de los valores ANSI
#para colores en un enumerado
class AnsiColor(Enum):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

#Función para imprimir matriz
def print_matriz(input_matriz):
    for row in input_matriz:
        print(list(row))

#Función para generar triangulo
def generate_triangle(rows = 1):
    #Parametros de la cuadricula
    columns = 2 * rows - 1

    #Creando el grid 2D
    matriz = []
    #Construyendo el grid (rejilla)
    for _ in range(rows):
        new_row = arr('i', [0] * columns)
        matriz.append(new_row)

    #Calcular el centro de la 1° Fila
    center = columns // 2 #División en enteros
    #Estableciendo el centro en 1
    matriz[0][center] = 1

    #Se calcula el resto de la matriz
    #siguiendo la lógica de sierpinsky gasket
    for row in range(1,rows):
        for col in range(0, columns):
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
    #Regresando la matriz
    return matriz

#Dibuja la matriz
def draw_matriz(input_matriz, symbol = "*"):
    for row in input_matriz:
        for cell in row:
            if cell == 1:
                print(AnsiColor.CYAN.value + symbol + AnsiColor.RESET.value, end="")
            else:
                print(AnsiColor.RED.value + " ", end="")
        print()

#Metodo principal
def main():
    #Genera el triangulo de Sierpinsky
    matriz = generate_triangle(8)

    #Limpia la pantalla antes de dibujar la matriz
    clear_screen()

    #Dibuja la matriz en pantalla
    draw_matriz(matriz, symbol = "■")

if __name__ == "__main__":
    main()