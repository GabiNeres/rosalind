n = 83
m = 19

adult = 1
young = [1,0,1]

for i in range(n-3):
        
        penultAdult = adult
        
        if len(young) >= m:
                adult = young[-1] + adult - (young[-m])
        else:
                adult = young[-1] + adult
        
        young.append(penultAdult)

print (adult + young[-1])

