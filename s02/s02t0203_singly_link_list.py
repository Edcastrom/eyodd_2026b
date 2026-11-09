#Importando clase Node
from s02t0201_linked_list import Node

#1. Creo función principal
def main():
    #2. Coloco el código ejecutable
    test_node = Node("Prueba")
    print(f"Valode del nodo: {test_node.data}")

#3. Evaluo el valor de __name__
if __name__ == "__main__":
    main()