"""
 4. Kārlim ir m lati. Viņš vēlas nopirkt n kg konfektes par c EUR/kg. Vai viņam pietiks naudas?

m = float(input("Ievadi cik naudas ir Kārlim? "))
n = float(input("Cik kg konfekšu pirks Kārlis? "))
c = float(input("Cik maksā 1 kg konfekšu ko pirks Kārlis? "))

konf = n * c
if konf < n:
    print("Kārlim naudas nepietiks! ")
else:
    print(f"Kārlim ir {m} EUR. Naudas nepietiks {n} kg konfekšu, kas maksā {c} EUR/kg, pietrūkst {konf - n} Eur! ")
    
print("Paldies par darbu!")


i = 1
while i < 10:
  print(i)
  i += 1
  
for x in range(1, 10):
  print(x, end=", ")
print("10.")

1. Uzrakstiet programmu, kas izvada pirmos 10 naturālos skaitļus.
"""
#for x in range(1, 10):
#    print(x, end=",")
#print("10.")

# 2. Uzrakstiet programmu, kas aprēķina un izvada pirmo 10 naturālo skaitļu summu. 
"""
summa = 0 # definējam mainīgo, kurā tiks saskaitīti skaitļi

for x in range(1, 1001):
    if x != 1000:
        print(x, end="+")
    else:
        print(x, end=" = ")
    summa = summa + x
print(summa, end=".")
"""
# 3. Uzrakstiet programmu, kas izvada pirmos N naturālos skaitļus un to summu. 
"""
n = int(input("Ievadi līdz kuram naturālam skaitlim rēķināt summu!"))
summa = 0        
for x in range(1, n + 1):
    if x != n:
        print(x, end="+")
    else:
        print(x, end=" = ")
    summa += x # ir tas pats, kas summa = summa + x
print(summa, end=".")
"""
# 4. Uzrakstiet programmu, kas pārbauda vai ievadītais skaitlis ir pirmskaitlis vai nav.
"""
sk = int(input("Ievadi skaitli lieāku par 1: ")) # int parveido automatiski par skaitli
ir = True

for ē in range(2, sk):
    if sk % ē == 0:
        print(f"Skaitlis {sk} nav pirmskaitlis")
        ir = False
        break
if ir:
    print(f"Skaitlis {sk} ir pirmskaitlis!")
""" 
# 9. Uzrakstiet programmu, kas aprēķina skaitļu virknes summu 1 + 1/2^2 + 1/3^3 + …..+ 1/n^n, n ievada lietotājs.


# 1. izmantojot for

sk = int(input("Ievadi skaitli lielāku par 0: "))
s = 0
for i in range (1, sk + 1):
    s += 1 / (i ** i)
print("Summa ar for ciklu ir:", s)

# 2. izmantojot while

s = 0
i = 1
while i <= sk:
    s += 1 / (i ** i)
    i += 1
    
print("Summa ar while ciklu ir:", s)
