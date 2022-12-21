
#1.uzd
katrina = 2023 #10.08.2005 = 10 + 8 + 2005 = 2023
print(katrina)

#2.uzd
import random
kalva = []
katrina=int(input("Ievadiet, cik elementu būs sarakstā!:"))
for i in range (katrina):
    kalva.append(random.randrange(-150,150))
print(kalva)
ar = 0
for i in range(katrina):
    ar = ar + kalva[i]
print("Skaitļu vidējā aritmētiskā vērtība ir", ar/katrina)
po =0
ne=0
no = 0
for i in range(katrina):
    if kalva[i] < 0:
        ne+=1
    if kalva[i] > 0:
        po+=1
    if kalva[i] == 0:
        no+=1
print(f"{ne} skaitļi ir negatīvi")
print(f"{po} skaitļi ir pozitīvi")
pāra=0
nepāra=0
for i in range(1,katrina+1):
    a=random.randrange(1,100)
    kalva.append(a)
if a%2==0:
    pāra+=1
else:
    nepāra+=1
    print(kalva)

for ē in range(2, katrina):
    if katrina % ē == 0: 
        print(ē)

    

#9.uzd
import random
rows, cols = (10, 8)
kalva = []
for i  in range(rows):
    col=[]
    for j in range(cols):
        col.append(random.randrange(0,2))
    kalva.append(col)
for i in range(rows):
    for j in range(cols):
        print(kalva[i][j], end=" ")
    print()

