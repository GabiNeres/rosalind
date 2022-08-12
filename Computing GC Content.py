dataset = open('rosalind_gc.txt', 'r')
symbol = '>'
content = {}
countcg = 0
valueMax = 0
label = ''
line = dataset.readlines() #se um arquivo for muito grande melhor ler linha por linha
porcent = 0
for i in range(len(line)):
    if symbol in line[i]:
        dicio = line[i].rstrip()
        content [dicio] = ""
    else:
        content [dicio] = content [dicio] + line[i].rstrip()
for key in content.keys():
    dna = content[key]
    for i in range (len(dna)):
        if (dna [i] == "C"):
            countcg = countcg + 1
        elif (dna [i] == "G"):
            countcg = countcg + 1
    porcent = (countcg*100)/len(dna)
    if valueMax < porcent:
        valueMax = porcent
        label = key
    countcg = 0
print (label+"\n", valueMax)
dataset.close()
