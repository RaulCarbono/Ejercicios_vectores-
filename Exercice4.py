# 4. De los n elementos de un vector dado identifique el número que mas se 
# repite e indique cual es.
vector = []
list=int(input(' Enter size to vector´s '))
for i in range (0,list): 
    numbers =int(input(' Enter numbers the vector  \n'))
    vector.append(numbers)

print(vector)
print()

repeated = 0
repeat_number = [0]

for i in vector:
    veces = vector.count(i)
    if veces > repeated:
        repeat_number = i
        repeated = veces

print(f"the number that is repeated the most is : {repeat_number}")
        