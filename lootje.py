import random
def picker(range):
    pick = random.randint(0, len(range)-1)
    return pick

persoon = ["iris", "katie", "frank", "wouter", "jelmer", "frans", "robin", "bobbie", "nicole", "jos", "frenk", "loel", "martijn", "roos"]
kiest = ["iris", "katie", "frank", "wouter", "jelmer", "frans", "robin", "bobbie", "nicole", "jos", "frenk", "loel", "martijn", "roos"]

koppelingen = []
algestoken = []
while persoon != []:
    persoon1 = persoon[0]
    file = persoon1 + ".txt"
    koppel = kiest[picker(kiest)]
    persoon.remove(persoon1)
    kiest.remove(koppel)
    with open(file, 'w') as filetowrite:
        koppelkoppel = persoon1 + " trok " + koppel
        koppelingen.append(koppelkoppel)
        algestoken.append(koppel)
        filetowrite.write(koppelkoppel)
    
#print(koppelingen)
