file = open('rosalind_iprb.txt', 'r')

lista = file.read().split()
k = int(lista [0]) #homozigoto dominante
m = int(lista [1]) #heterozigoto
n = int(lista [2]) #homozigoto recessivo  

soma = k+m+n

escolha_um = k/soma
escolha_dois = m/soma
escolha_tres = n/soma

#quando escolhe k primeiro
prob_domin = (escolha_um * m/(soma-1)) + (escolha_um * n/(soma-1)) + (escolha_um * (k-1)/(soma-1))    

#quando escolhe m primeiro
prob_het = ((escolha_dois * n/(soma-1)) * (1/2)) + (escolha_dois * k/(soma-1)) + ((escolha_dois * (m-1)/(soma-1)) * (3/4))

#quando escolhe n primeiro
prob_rec = ((escolha_tres * m/(soma-1)) * (1/2)) + (escolha_tres * k/(soma-1))

prob_total = prob_domin + prob_het + prob_rec

print(prob_total)

