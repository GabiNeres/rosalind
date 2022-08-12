dataset = open('input.txt', 'r')
table = open('aminoacidos.txt', 'r')
strand = dataset.read()
content = {}
protein = ""
for line in table:
    amino = line.strip().split(" ")
    content [amino[0]] = amino [1]

for i in range(len(strand)):
    if i % 3 == 0:
        aa = strand[i:(i+3)]
        if content[aa] != "Stop":
            protein += content[aa]
print (protein)
        