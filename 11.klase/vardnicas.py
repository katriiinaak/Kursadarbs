"""
Vārdnīcas
"""
suns = {
    "Šķirne" : "jauktenis",
    "Krāsa" : "melna",
    "Svars" : "13 kg",
    "Vecums" : "8 gadi",
    "Vārds" : "Regijs",
    "Dzimums" : "zēns"
    }

print(suns)
#print(type(suns))
print(suns["Šķirne"])
print(suns.keys())
print(suns.get("Šķirne"))
print("\n")

for key, value in suns.items():
    print(f"{key} - {value}")

for key in suns.keys():
    print(f"{key}")

print(f"Manu suni sauc {suns['Vārds']}, viņš ir {suns['Dzimums']}. Regija šķirne ir {suns['Šķirne']} um viņa krāsa ir {suns['Krāsa']}. {suns['Vārds']} sver {suns['Svars']}. ")

#print(bariba)
#print(type(bariba))
#print(bariba["Auzas"])
#print(bariba.keys())
#print(bariba.get("Auzas"))
#print("\n")

#for key, value in bariba.items():
#    print(f"{key} - {value}")

#for key in bariba.keys():
#    print(f"{key}")



