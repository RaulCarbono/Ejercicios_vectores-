# siguientes ejercicios:
# 1. De los n elementos de un vector dado calcule:
# a. La sumatoria
# b. La productoria
# c. El Mayor Elemento
# d. El menor Elemento
vector=[]
summation = 0
product = 1
major = 0
minor = 0 
list=int(input("enter to zice to vector ")) 

for i in range (0,list):
    number = int(input(" Enter number "))
    vector.append(number)
for i in vector : 
    summation += i  
    product *=i
    major = max(vector)
    minor = min(vector)

print(vector)
print(f" The summation the vector is {summation}")
print(f" The product the vector is {product}")
print(f' The number major is {major}')
print(f' The number major is {minor}')
    
