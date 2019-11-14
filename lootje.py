import random
namen = ["iris", "katie", "frank", "wouter", "jelmer", "frans", "robin", "bobbie", "nicole", "jos", "frenk", "loel", "martijn", "roos"]

count = 0
for i in range(0, 1000):
    koppelingen = []
    algestoken = []
    for i in namen:
        olifant = True
        while olifant:
            koppel = namen[random.randint(0, len(namen)-1)]
            if koppel != i:
                if koppel not in algestoken:
                    #koppelkoppel = i + " trok " + koppel
                    #koppelingen.append(koppelkoppel)
                    algestoken.append(koppel)
                    olifant = False
        if i == "batie" and koppel == "bobbie":
            count += 1

print(koppelingen)
print("Katie trok bobbie", count, " keer.")