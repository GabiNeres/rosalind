file = open('rosalind_lcsm.txt','r')
content = {}
fitas = []
nucl = ['A','T','G','C']
nucl_ = ['A','T','G','C']
sharedMotif = ""

for line in file:
    if '>' in line:
        dicio = line.rstrip()
        content [dicio] = ""
    else:
        content [dicio] = content [dicio] + line.rstrip()

for i in content.keys():
    fitas.append(content[i])

while len(nucl) > 0:
    control = True
    motif = nucl.pop(0)
    for i in range(len(fitas)):
        if motif not in fitas[i]:
            control = False
            break
    if control == True:
        sharedMotif = motif
        for i in range(len(nucl_)):
            nucl.append(motif+nucl_[i])

print (sharedMotif)