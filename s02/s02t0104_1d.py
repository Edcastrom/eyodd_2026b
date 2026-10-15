#Eliminación
#Importando el modulo arrays de
#la biblioteca array y renombrando
#como arr
from array import array as arr

#Importando una funcion desde otro
#archivo
from s02t0102_1d import print_array

array_01 = arr('i',[5,10,15,20,10])

print("--- ANTES DE LA ELIMINACIÓN ---")
print_array(array_01)

#Eliminación
try:
    array_01.remove(100)
except:
    print("No se encuentra en el arreglo")

print("--- DESPUES DE LA ELIMINACIÓN ---")
print_array(array_01)

