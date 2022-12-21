""""
Sastādīt programmu Python vidē, kas pieprasa ievadīt 2 skaitļus un darbību (+, -, *, /).
Atkarībā no izvēlētās darbības izvada atbildi.
Katrai darbībai uzrakstīt rakstīt savu funkciju ar parametriem, kuras argumenti būs ievadītie skaitļi. 
"""
v = int(input("Īevadiet pirmo skaitli: "))
k = int(input("Ievadiet otro skaitli: "))
print("Ievadiet, kādu darbību vēlaties izpildīt?")
t = int(input("Varianti: 1-saskaitīšana; 2-atņemšana; 3-reizināšana; 4-dalīšana: "))

import funkcijas


if t == 1: #1.variants
    r = funkcijas.saskaitit(v, k)
    print(f"{v} + {k} = {r}")
elif t == 2: #2.variants
    print(f"{v} - {k} = ", funkcijas.atnemt(v, k))
elif t == 3:
    print(f"{v} * {k} = ", funkcijas.reizinat(v, k))
else:
   print(f"{v} / {k} = ", funkcijas.dalit(v, k))

print(u"\u00A9katrina 11A JEPVG 2022")