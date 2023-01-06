N = 4
n = 2
letras = ['A', 'C', 'G', 'T']
numero = []

def combin(lista,i,str='',res=[]):
    if i == 0:
        res.append(str)
    else:
        for n in lista:
            combin (lista,i-1,str+n,res)
    return res

for j in combin (letras,n):
    print (j)

