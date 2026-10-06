# Creamos una lista de estudiantes 
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # O(4)

def random_function(students): 
    first = students[0] # O(1)
    total = 0 # O(1)
    new_list = [] # O(1)

    for student in students: 
        total += 1 # O(n)
        new_list.append(student) # O(n)

        print(new_list) # O(1)
        return total # O(1)

print(random_function(student_list_01)) 

# Calcular O(?)
# O(n+4+5) = O(n) <--Simplificación total