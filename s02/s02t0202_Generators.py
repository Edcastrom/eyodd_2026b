"""
Generators

Los generadores son funciones que pueden
pausar su ejecución.

Cuándo se invoca una función generadora
devuelve un objeto generador (aka Iterador)

El código dentro de la función no se ejecuta
de inmediato, solo se compila.

La función se ejecuta únicamente cuando
iteras sobre el generador.

"""

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4

#Se invoca función generadora
my_iterator = my_generator()

#Se itera manualmente sobre el generador
# print(next(my_iterator)) #Imprime 1
# print(next(my_iterator)) #Imprime 2
# print(next(my_iterator)) #Imprime 3
# print(next(my_iterator)) #Imprime 4
# print(next(my_iterator)) #Imprime ?

#Los iteradores se pueden iterar con for
for value in my_iterator:
    print(value)
    