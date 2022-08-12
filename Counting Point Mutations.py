dataset = open('rosalind_hamm.txt', 'r')
s = dataset.readline().rstrip()
t = dataset.readline().rstrip()
mutation = 0
for i in range(len(s)):
    if s[i] != t[i]:
        mutation += 1
print (mutation)