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

#Buscar el elemento n
num_a_eliminar = 10
counter = 0

#Eliminación con for
#print(f"Se busca {num_a_eliminar} en el arreglo.")
#for integer in array_01:
#    if integer == num_a_eliminar:
#        array_01.remove(num_a_eliminar)
#    counter += 1
#    if counter == len(array_01):
#        print("❌ Número no necontrado")

#Eliminación con while
while num_a_eliminar in array_01:
    array_01.remove(num_a_eliminar)
    counter += 1

print("--- DESPUES DE LA ELIMINACIÓN ---")
print_array(array_01)

#Comprobando si se elimino algún elemento
if counter > 0:
    print( f"🎊 Se eliminaron {counter} elemento(s)")
else:
    print("❌ Número no encontrado")