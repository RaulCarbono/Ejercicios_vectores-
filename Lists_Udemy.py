# Ejercicio 1
# En la siguiente lista, debes hacer un programa que muestre los valores al usuario, 
# a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el 
# primer y segundo lugar: [20, 50, "Curso", 'Python', 3.14]
# list = [20, 50, "Curso", 'Python', 3.14]

# print(list)
# date = (input('Enter new date '))
# date2 = (input('Enter new date '))
# list[0] = date
# list[1] = date2

# print(list)

#Escribe una lista que tenga los numeros del 1 al 10, luego debes hacer que los datos que estan 
#en la posicion 4, 7, 9 sean multiplicados por 2; por ultimo mostrar la lista con los nuevos datos 
from typing import List


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

list[3] *=  2
list[6] *= 2
list[8] *= 2
print(list)
