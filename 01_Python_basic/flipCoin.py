import random

numeroEsperimenti=100000
flipPerExperiment=100
streakLenght=6
streaks=0
lanciH=0
lanciT=0

for x in range(numeroEsperimenti):
    lista=[]
    for y in range(flipPerExperiment):
        if random.randint(0,1)==0:
           lista.append("H")
        else:
            lista.append("T")
    streakCount=1
    for i  in range(1, len(lista)):
        if lista[i]==lista[i-1]:
            streakCount+=1
            if streakCount==streakLenght:
                streaks += 1
                break
        else:
            streakCount=1
    
    for i in range(len(lista)):
        if lista[i]=="H":
            lanciH+=1
        elif lista[i]=="T":
            lanciT+=1
            

lanciHPercentage= (lanciH/(numeroEsperimenti*flipPerExperiment))*100
lanciTPercentage= (lanciT/(numeroEsperimenti*flipPerExperiment))*100
streakPercentage= (streaks/numeroEsperimenti)*100
print(f"Percentuale di esperimenti con almeno una serie di 6: {streakPercentage}")
print(f"La percentuale di lanci H è: {lanciHPercentage} %")
print(f"La percentuale di lanci T e: {lanciTPercentage} %")
