#Importando el modulo arrays de
#la biblioteca array y renombrando
#como arr
from array import array as arr

#Importando una funcion desde otro
#archivo
from s02t0102_1d import print_array

array_01 = arr('i',[5,10,15,20])

print("--- ANTES DE LA INSERCIÓN ---")
print_array(array_01)

#Inserción
array_01.insert(1,90)
print("--- DESPUES DE LA INSERCIÓN ---")
print_array(array_01)

print("--- DESPUES DE APPEND ---")
array_01.append(1000)
print_array(array_01)

print("--- SIMULAR UN APPEND CON INSERT ---")
array_01.insert(len(array_01),90000)
print_array(array_01)
