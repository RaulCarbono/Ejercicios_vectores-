# 6. Dado un vector v, indique si es simétrico, un vector es simétrico si siendo 
# longitud par los números de la primera mitad son iguales al inverso de la 
# otra mitad por ejemplo: X=[1,2,3,3,2,1], en el ejemplo x es un vector 
# simétrico, en caso que la longitud del vector sea impar, se ignorará el 
# elemento central y se seguirá la misma lógica anterior, por ejemplo: 
# Y=[3,5,7,8,7,5,3], en este ejemplo Y es simétrico

vector = []
list=int(input(' Enter size to vector´s '))
for i in range (0,list): 
    numbers =int(input(' Enter numbers the vector  \n'))
    vector.append(numbers)
if vector == vector[::-1]: 
        
        print('es simetrico')
else :
        print('no es simetrico')