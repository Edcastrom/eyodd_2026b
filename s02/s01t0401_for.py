"""
Escribir un programa que calcule
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa
calculara la suma del 1 al 100.
42
"""
#Importamos biblioteca time
import time

#función que suma los
#primeros "n" números naturales
def sum_of_n(n):
    total_sum = 0
    #Sumando los "n" números
    #Ciclo for
    for number in range(1,n+1):
        total_sum = total_sum + number
    #Retornando el total de la suma
    return total_sum

#Varialbe para guardar
#el data set
dataset = [] #[(n,time,sum),(n,time,sum)]

#Generando el contenido del Dataset
for repetition in range(1,11):
    # ⏱️ Tomo el tiempo 1 (Inicial)
    timestamp_01 = time.time()

    #Sumo los "n" números
    n = repetition * 500
    #Gueardo el resultado en result
    result = sum_of_n(n)

    # ⏱️ Tomando el tiempo final
    timestamp_02 = time.time()

    #Calculando el tiempo
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6,2)

    #Agregar la tripleta de los
    #datos al dataset
    dataset.append( (n,elapsed_time,result) )

#Imprimir el dataset
for tup in dataset:
    print(tup)

