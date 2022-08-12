dataset = open('rosalind_subs.txt', 'r')
dna = dataset.readline()
motif = dataset.readline()
num_motif = len(motif)

for i in range(len(dna)):
    if dna[i:(i+num_motif)] == motif:
        print (i+1)
