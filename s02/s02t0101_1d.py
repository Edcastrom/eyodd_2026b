#Importando el modulo Arrays
from array import array as arr

#Creando un arreglo

#i = Entero con signo
#I = Entero sin signo
#f = Número decimal
#d = Número decimal doble
#u = Carácteres unicode
array_01 = arr('i',[10,22,300,3,7,40,55,80,700,654,34])

#Iterando automáticamente
# for data in array_01:
#    print(data,end=",")
#print()

#Acceso individual a los elementos
#print(array_01[0]) #Primer elemento
#print(array_01[1]) #Segundo elemento
#print(array_01[2]) #Tercer elemento

#Tamaño de un arreglo
#Length
#print(len(array_01))

#Iteración por indices
for i in range(len(array_01)):
    if array_01[i] % 2 == 0:
        print(f"Elemento num: {i+1}: {array_01[i]}") #Números pares
    #print(f"Elemento {i+1}: {array_01[i]}")