from Bio import SeqIO

input_file = open('rosalind_cons.txt', 'r')

nucl = ["A","C","G","T"]

profile = {"A":[], "C":[], "G":[], "T":[]}
count = []

fasta_sequences = SeqIO.parse(open(input_file),'fasta')

# first record:
fasta = next(fasta_sequences)
seq = str(fasta.seq)
seqLen = len(seq)
for i in range(len(seq)):
    profile["A"].append(0)
    profile["C"].append(0)
    profile["G"].append(0)
    profile["T"].append(0)
    count.append({"maxCount":0, "maxNucl":""})
    
    profile[seq[i]][i] += 1
    count[i]["maxCount"] = 1
    count[i]["maxNucl"] = seq[i]

# analyse the other sequences
for fasta in fasta_sequences:
    sequence = str(fasta.seq)
    for i in range(len(sequence)):
        profile[sequence[i]][i] += 1
        if profile[sequence[i]][i] > count[i]["maxCount"]:
            count[i]["maxCount"] = profile[sequence[i]][i]
            count[i]["maxNucl"] = sequence[i]
cons = ""
for i in range(seqLen):
    cons += count[i]["maxNucl"]
print(cons)
    
for i in nucl:
    result = [i+":"]
    for j in range(seqLen):
        result.append(str(profile[i][j]))
    print(" ".join(result))
