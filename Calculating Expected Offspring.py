file = open('rosalind_iev.txt','r')
valores = file.read().split()
lista = [int(val) for val in valores]
fenotipoDominante = 0
print (lista)

for i in range(len(lista)):
    if lista[i] > 0:
        offspring = 2*lista[i]
        if i == 0 or i == 1 or i == 2:
            fenotipoDominante += offspring
        elif i == 3:
            fenotipoDominante += offspring*(3/4)
        elif i == 4:
            fenotipoDominante += offspring*(1/2)
            
print (fenotipoDominante)

