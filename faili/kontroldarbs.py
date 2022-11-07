vārdnīca = {
    "ASV" : "331,9 miljoni",
    "Latvija" : "1,883 miljoni",
    "Zviedrija" : "10,42 miljoni",
    "Īrija" : "5,028 miljoni",
    "Dānija" : "5,857 miljoni",
    "Ķīna" : "1,412 miljardi",
    "Somija" : "5,542 miljoni",
    "Austrālija" : "25,74 miljoni",
    "Lielbritānija" : "67,33 miljoni",
    "Japāna" : "125,7 miljoni",
    }

print(vārdnīca)

print(vārdnīca["ASV"])
print(vārdnīca.keys())
print(vārdnīca.get("ASV"))
print("\n")

for key, value in vārdnīca.items():
    print(f"{key} - {value}")

for key in vārdnīca.keys():
    print(f"{key}")

def funkcija(k, l):
  print(" Valsts ar lielāko iedzīvotāju skaitu ir " + k)
  print(" Valsts ar mazāko iedzīvotāju skaitu ir " + l)
funkcija(k = "Ķīna", l = "Latvija")


dotie = {
    "Ukraina - 43,81 miljoni" : "Turcija - 85,04 miljoni",
    }
print("Izvēlaties valsti, kuras iedzīvotāju skaitu vēlaties uzzināt: ")
c = int(input("Atbilžu varianti: 1-Turcija; 2-Ukraina: " ))
if c == 1:
    print("Ievadiet valsts nosaukumu no dotajiem: ") 
    for key in dotie.keys():
        print(f"{key}")
else:
    print("Dotie vārdi: ") 
    for value in vārdnīca.values():
        print(f"{value}")