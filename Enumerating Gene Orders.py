
n = 5
perm = n
numero = []
matriz = []

def permut(LIST):
    length=len(LIST)
    if length <= 1:
        yield LIST
    else:
        for n in range(length):
            for fim in permut( LIST[:n] + LIST[n+1:] ):
                yield [ LIST[n] ] + fim

for i in range(n):
    if (i != 0):
        perm = perm*i
print (perm)

for i in range(n):
    numero.append(i+1)

for lista in permut(numero):
    print(" ".join(map(str, lista)))


