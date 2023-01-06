file = open('rosalind_revp.txt','r')
complement = ""
result = []

for line in file:
    if '>' in line:
        label = line.rstrip()
        dna = ""
    else:
        dna = dna + line.rstrip()

for i in dna:
    if (i == 'A'):
        complement += "T"
    if (i == "T"):
        complement += "A"
    if (i == "C"):
        complement += "G"
    if (i == "G"):
        complement += "C"

for i in range(len(dna)):
    for tam in range (4, 13, 2):
        if (tam + i) > len(dna):
            break
        new_complement = complement[i:i+tam]
        relist = list(new_complement)
        relist.reverse()
        reverse = ''.join(relist)
        if dna[i:i+tam] == reverse:
            result.append ([i+1,tam])

for i in range(len(result)):
    resposta = str(result[i][0]) + ' ' + str(result[i][1])
    print(resposta)