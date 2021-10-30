# 3. Dado un Vector v y un Vector v1 de cómo resultado un Vector resultante de 
# las siguientes operaciones:
# a. Suma
# b. Resta
vector1 = []
vector2 = []
vector_summation = []
vector_subtraction = [] 
list = int(input("Please, enter a number to add to the list, enter 0 to close the list: \n"))
for i in range(0,list): 
    elements = int(input("enter a number to add to the list one, \n"))
    vector1.append(elements)
    
for i in range(0,list):
    elements = int(input("enter a number to add to the list two, \n"))
    vector2.append(elements)
print(f'List one  {vector1}')
print(f'List Two {vector2}')
for i in range(0,list): 
    vector_summation.append(vector1[i] + vector2[i])

for i in range(0,list):
    vector_subtraction.append(vector1[i] - vector2[i])

print(vector_summation)
print(vector_subtraction)
    

