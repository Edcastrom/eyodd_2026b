#Importando el modulo arrays de
#la biblioteca array y renombrando como arr
from array import array as arr

def print_array(input):
    print("[",end="")
    for element in input:
        print(element,end=",")
    print("\b]")

array_01 = arr('i',[5,10,15,20])
print_array(array_01)

#Buscar el elemento 15
number_to_search = 100
counter = 0
print(f"Se busca {number_to_search} en el arreglo.")
for integer in array_01:
    if integer == number_to_search:
        print("🎊 Número encontrado")
        #Sirve para terminar el ciclo
        break
    #Incrementamos contador
    counter += 1
    if counter == len(array_01):
        print("❌ Número no necontrado")
