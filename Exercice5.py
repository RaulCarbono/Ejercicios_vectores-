# Dado un Vector v de longitud par, divida en 2 partes, en la primera parte 
# realice la productoria y en la segunda la sumatoria. Entregue los valores 
# resultantes.
vector = []
productive = 1
summation = 0
list=int(input(' Enter size to vector´s '))

while list !=0: 
    if list % 2 ==0:  
        div = int(list/2)
        for i in range (0,list): 
            numbers =int(input(' Enter numbers the vector \n'))
            vector.append(numbers) 
        for i in range(div,len(vector)) :
            summation += vector[i]
        for i in range(div) : 
            productive *= vector[i]
        print(vector)
        print('///////////////////////////////////////////')
        print(productive)
        print(summation)
        break
    else:
        list=int(input(' Enter size to vector validate '))
    


