#Importando clase Node
from s02t0201_linked_list import Node

#Creando la clase de una lista enlazada
class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #Método de incerción de Nodo de la lista
    def append(self, data):
        #Creo el nodo
        new_node = Node(data)

        #Si la lista esta vacia
        #apuntamo el head al nuevo nodo
        #que se creo
        if not self.head:
            self.head = new_node
            return

        #Si la lista no esta vacia, hay
        #que recorrer el nodo hasta llegar
        #al final de la lista.
        #Estableciendo el nodo acutal
        #como el primero de la lista
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        #Que hacemos ahora
        current_node.next = new_node

def main():
    #Creando una instancia de una lista enlazada
    my_list = SinglyLinkedList()
    #Agregar elementos a la lista
    my_list.append(30)
    my_list.append(59)
    my_list.append(80)
    my_list.append(100)

    #Recorrer la lista
    for value in my_list.head.iter():
        print(f"{value},", end="")
    print()

#Evaluo el valor de __name__
if __name__ == "__main__":
    main()