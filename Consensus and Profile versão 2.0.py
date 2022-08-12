dataset = open('input.txt', 'r')
profileA = []
profileC = []
profileG = []
profileT = []
consensus = ""
count = 0
content = ""

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
def profile(dna,count):
    for i in range(len(dna)):
        if count == 1:
            if dna[i] == "A":
                criarProf (1,0,0,0)
            elif dna[i] == "C":
                criarProf (0,1,0,0)
            elif dna[i] == "G":
                criarProf (0,0,1,0)
            elif dna[i] == "T":
                criarProf (0,0,0,1)
        else:
            if dna[i] == "A":
                atualizarProf (1,0,0,0,i)
            elif dna[i] == "C":
                atualizarProf (0,1,0,0,i)
            elif dna[i] == "G":
                atualizarProf (0,0,1,0,i)
            elif dna[i] == "T":
                atualizarProf (0,0,0,1,i)

#for para ler fitas de DNA
for line in dataset:
    if '>' in line:
        if content != "":
            count += 1
            profile(content,count)
        content = ""
    else:
        content = content + line.rstrip()
profile (content,count)

#for da fita consenso
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
        

