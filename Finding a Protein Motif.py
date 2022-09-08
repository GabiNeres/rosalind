import urllib.request

characters = "b', []"

file = open('rosalind_mprt_1.txt', 'r')

for id in file:
    location = ""
    id_uniprot = ""
    control = False
    uniprot = id.rstrip()
    uniprot_id = uniprot [0:6]
    protein = urllib.request.urlopen("http://uniprot.org/uniprot/"+uniprot_id+".fasta").read()

    pre_proteina = protein.splitlines()
    proteina = ''.join(str(pre_proteina[1:]))
    
    for x in range(len(characters)):
        proteina = proteina.replace(characters[x],"")
    
    for i in range (len(proteina)):
        if len(proteina) - (i+3) >= 3:
            if proteina[i] == 'N' and proteina[i+1] != 'P' and (proteina[i+2] == "T" or proteina[i+2] == "S") and proteina[i+3] != 'P':
                control = True
                location += str(i+1)+" "
                id_uniprot = uniprot
    if control == True:
        print (id_uniprot)
        print (location)
            




    

