dataset = open('input.txt', 'r')
content = {}

for line in dataset:
    if '>' in line:
        dicio = line.rstrip().replace(">","")
        content [dicio] = ""
    else:
        content [dicio] = content [dicio] + line.rstrip()

for i in content.keys():
    fita = content[i]
    motif = fita[-3:-1]
    for j in content.keys():
        if i != j:
            fita1 = content[j]
            motif1 = fita1[0:2]
            if motif == motif1:
                print (i+" "+j)