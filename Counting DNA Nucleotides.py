dna = 'CTTAGGGCGGGGTTCACCGAGCTACCGACCACGCAGATGAGCATTATTTTGCTATGAAATTCGGAACTATCCGCTTGAGTACTTTAGGCTGTACGAGTAAGGAAATACAATTGTGTGAAGGGTAGACCCACAGCCAATCTCATCTAGGCTTCTCGTATTCACCCTCGACTCACATGCTAGACGTGTGAAAGCATTCAAACGTAGTTCACTGGATAAGTCGAGGACCGTGAAAGGTACGGTCTAAGGTCATTGCCTTACCATCTAGCTGTAGAGGCATATTAGAAAGCTGCTAAGCACATGGTAGGCCTAACTTTCGACGTGAACTGGACCGAAGGAAAGCCGCTTGGTCCGAGTCCCCCCTCTCTTCCCTATACATTGAGTACGGTACACCTGTGTAGGTTACTTTTAGCGGTGTCAACGAAACAAGGGGGGTTACATATAGGGCTCCCGTTGTTCTCATAAGAGTGACCCGTCAGTGAAAACGTAGCATGTCCACGGGCAGAATTAATTTGGCGCGAGGGGCCAGACTGCAATAGAGGCCGAGTACATGTCTTATCATCCCGCGGGGCCCAATTTTACAGGTACTGATCTGCAAGGCGCTGGCATACTGGTGAGTGAGGCTATGCGGCTACCAAAAGATGCAAACGGGGGCTAGGATTCGTCTATGCCTTGGAGACGCAGCTAGGCAAGCGCTAAACATTACAGAACTCGGAGTGTACTGCTCATGCGGCAGTTGGCTTCACCCCCATATCCCCCTACAATTAGAGGGTGCACTTAACACGTCCAGAGGTTGGATGCAACCATTAAGCAATCATGTAGT'
a = 0
g = 0
c = 0
t = 0
for i in range (len(dna)):
    if dna[i] == 'A':
        a = 1 + a
    elif dna[i] == 'G':
        g = 1 + g
    elif dna[i] == 'C':
        c = 1 + c
    elif dna[i] == 'T':
        t = 1 + t
print (a, c, g, t)