n = 5
k = 3
contador = 0
preAnt = 1
ant = 1

for i in range(n-2):
    contador = preAnt*3 + ant
    preAnt = ant
    ant = contador
    print (ant)