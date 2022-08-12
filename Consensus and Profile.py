dataset = open('rosalind_cons.txt', 'r')
symbol = '>'
matrix = []
profileA = []
profileC = []
profileG = []
profileT = []
profile = []
consensus = ""
content = {}
line = dataset.readlines()
linhas = []

# funções para criar e atualizar profile
def criarProf(a,b,c,d):
    profileA.append(a)
    profileC.append(b)
    profileG.append(c)
    profileT.append(d)
def atualizarProf(a,b,c,d,j):
    profileA[j] += a 
    profileC[j] += b
    profileG[j] += c
    profileT[j] += d

#for para criar matriz de fitas de DNA
for i in range(len(line)):
    if symbol in line[i]:
        dicio = line[i].rstrip()
        content [dicio] = ""
    else:
        content [dicio] = content [dicio] + line[i].rstrip()
for key in content.keys():
    dna = content[key]
    matrix.append(list(dna))

#for para criar profile
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 0:
            if matrix[i][j] == "A":
                criarProf (1,0,0,0)
            elif matrix[i][j] == "C":
                criarProf (0,1,0,0)
            elif matrix[i][j] == "G":
                criarProf (0,0,1,0)
            elif matrix[i][j] == "T":
                criarProf (0,0,0,1)
        else:
            if matrix[i][j] == "A":
                atualizarProf (1,0,0,0,j)
            elif matrix[i][j] == "C":
                atualizarProf (0,1,0,0,j)
            elif matrix[i][j] == "G":
                atualizarProf (0,0,1,0,j)
            elif matrix[i][j] == "T":
                atualizarProf (0,0,0,1,j)

for i in range(len(profileA)):
        if profileA[i] >= max(profileC[i], profileG[i], profileT[i]):
            consensus += "A"
        elif profileC[i] >= max(profileA[i], profileG[i], profileT[i]):
            consensus += "C"
        elif profileG[i] >= max(profileC[i], profileA[i], profileT[i]):
            consensus += "G"
        elif profileT[i] >= max(profileC[i], profileG[i], profileA[i]):
            consensus += "T"

print(consensus)
print("A: "+" ".join(map(str, profileA)))
print("C: "+" ".join(map(str, profileC)))
print("G: "+" ".join(map(str, profileG)))
print("T: "+" ".join(map(str, profileT)))
        

