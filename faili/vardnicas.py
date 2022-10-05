"""
Vārdnīcas
"""
suns = {
    "Šķirne" : "Laika",
    "Krāsa" : "Melna",
    "Svars" : "27 kg",
    "Vecums" : "3 gadi",
    "Vārds" : "Čaika",
    "Dzimums" : "Zēns"
    }

print(suns)
#print(type(suns))
print(suns["Šķirne"])
print(suns.keys())
print(suns.get("Širne"))
print("\n")

for key, value in suns.items():
    print(f"{key} - {value}")

for key in suns.keys():
    print(f"{key}")

print(f"Manu suni sauc ")
