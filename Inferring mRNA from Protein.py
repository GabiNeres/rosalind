dataset = open('rosalind_mrna.txt', 'r')
table = open('aminoacidos.txt', 'r')
protein = dataset.read().strip()
content = {}
fitas = 1

for line in table:
    amino = line.strip().split(" ")
    if amino[1] in content:
        content [amino[1]] += 1
    else:
        content [amino[1]] = 1

for aa in protein:
    fitas = (fitas*content[aa])%1000000

print((fitas*3)%1000000)
