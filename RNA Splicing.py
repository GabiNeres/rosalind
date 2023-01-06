file = open('rosalind_splc.txt','r')
table = open('aminoacidos.txt', 'r')
content = {}
aminoacido = {}
introns = []
protein = ""
rna = ""

for line in file:
    if '>' in line:
        dicio = line.rstrip()
        content [dicio] = ""
    else:
        content [dicio] = content [dicio] + line.rstrip()

for line in table:
    amino = line.strip().split(" ")
    aminoacido [amino[0]] = amino [1]

dna = content['>Rosalind_8982']

for i in content.keys():
    if (content[i] == dna):
        continue
    else:
        introns.append(content[i])

for i in introns:
    num_motif = len(i)
    for j in range(len(dna)-num_motif):
        if dna[j:(j+num_motif)] == i:
            dna = dna[:j] + dna[(j+num_motif):]

for i in dna:
    if i == 'A':
        rna = rna + 'A'
    elif i == 'G':
        rna = rna + 'G'
    elif i == 'C':
        rna = rna + 'C'
    elif i == 'T':
        rna = rna + 'U'

for i in range(len(rna)):
    if i % 3 == 0:
        aa = rna[i:(i+3)]
        if (len(aa) == 3):
            if aminoacido[aa] != "Stop":
                protein += aminoacido[aa]
print (protein)