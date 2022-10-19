#vārdnīca angļu - latviešu (dzīvnieki)
vārdnīca = {
    "Zirgs" : "Horse",
    "Suns" : "Dog",
    "Kaķis" : "Cat",
    "Zivs" : "Fish",
    "Putns" : "Bird",
    "Lauva" : "Lion",
    "Tīģeris" : "Tiger",
    "Ponijs" : "Pony",
    "Skudra" : "Ant",
    "Delfīns" : "Dolphin",
    "Lācis" : "Bear",
    "Liāna" : "Liana",
    "Pēriķis" : "Monkey",
    "Govs" : "Cow",
    "Kaza" : "Goat",
    "Vista" : "Hen",
    "Vilks" : "Wolf",
    "Lapsa" : "Fox",
    "Vāvere" : "Squirrel",
    "Pele" : "Mouse",
    "Krokodils" : "Crocodile"
}


print("No kuras valodas vēlaties tulkot?")
c = int(input("Atbilžu varianti: 1-Latviešu; 2-Angļu: " ))
if c == 1:
    print("Dotie vārdi: ") #ja atbilde bija 1, tad izmet latv. val vardus
    for key in vārdnīca.keys():
        print(f"{key}")
else:
    print("Dotie vārdi: ") #ja atbilde bija 2, tad izmet anglu val. vardus
    for value in vārdnīca.values():
        print(f"{value}")


"""
print("Dotie vārdi: ")
for value in vārdnīca.values():
    print(f"{value}")




v = str(input("Ievadiet vienu no dotajiem vārdiem, kuru vēlaties iztulkot: "))
print(vārdnīca[v])

print("Vai vēlaties iztulkot vēl kādu vārdu?")
k = int(input("Atbilžu varianti: 1-Jā; 2-Nē: " ))

if k == 1:
    m = int(input("Cik vārdus vēlaties vēl iztulkot? ")) 
    for i in range (m):
        v = str(input("Ievadiet vienu no dotajiem vārdiem, kuru vēlaties iztulkot: "))
        print(vārdnīca[v])
    print("Paldies, ka izmantojāt tulkotāju! ")
else:
    print("Paldies, ka izmantojāt tulkotāju! ")
"""