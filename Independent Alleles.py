file = open('rosalind_lia.txt', 'r')

lista = file.read().split()
k = int(lista [0]) #geração
n = int(lista [1]) #
N = 2**k
p = 0.25

def factorial(i):
  x = 1
  for j in range(i):
    x *= j+1
  return x

def comb(N, n):
  return factorial(N)/((factorial(n)*factorial(N-n)))

probSum = 0
for i in range(n):
  probSum += comb(N, i)*(p**i)*((1-p)**(N-i))
print(1 - probSum)