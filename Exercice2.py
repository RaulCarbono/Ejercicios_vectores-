# 2. De los n elementos de un vector dado calcule:
# a. Cantidad de elementos pares
# b. Cantidad de elementos impares
# c. Cantidad de elementos primos
def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

vector = []
even = 0 
odd = 0 
prime = 0

elements = int(input("Please, enter a number to add to the list, enter 0 to close the list: \n"))
while elements !=0:
    vector.append(elements)
    elements = int(input("enter a number to add to the list, \n")) 

print(f"this the list {vector} : ")
for i in vector:
    if es_primo(i):
        prime += 1
    if i % 2 == 0:
        even +=1
    else:
        odd += 1

print(f"There are {prime} prime number")
print(f"There are {even} even number")
print(f"There are {odd} od number")