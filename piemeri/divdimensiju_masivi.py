#1)Sastādīt programmu, kas ģenerē nejaušu skaitļu masīvu A(n×m). Atrast pāru skaitļu skaitu. Skaitļu masīvu izvadīt uz ekrāna. 
"""
import random

rows = (random.randrange(0, 5)) #ģenerē nejaušus skaitļus rindām
cols = (random.randrange(0, 5)) #ģenerē nejaušus skaitļus kolonnām
arr = [] #masīva nosaukums
sum = []
o = 0
for i in range(rows):
    col = []
    for j in range(cols):
        sk = random.randrange(0,20)
        col.append(sk)
        if sk % 2 == 0:   
           o+=1  #0 piesksita 1 un beigās parāda pāra skaitļu skaitu o=pāra skaitļi
    arr.append(col)

for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end="\t")
    print()
print(o) #izvada pāra skaitļu skaitu

#2)Sastādīt programmu, kas ģenerē nejaušu skaitļu masīvu A(n×m). Atrast negatīvo elementu skaitu katrā kolonā. Skaitļu masīvu izvadīt uz ekrāna. 

import random

rows = (random.randrange(0, 5))
cols = (random.randrange(0, 5))
arr = []
sum = []
s = 0
for i in range(rows):
    col = []
    for j in range(cols):
        sk = random.randrange(-14,20)
        col.append(sk)
        if sk < 0:   #izvada negatīvo skaitļu skaitu
           s+=1  
    arr.append(col)


for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end="\t")
    print()
print("Negatīvo skaitļu skaits sarakstā:",s)
"""
#3)Sastādīt programmu, kas ģenerē nejaušu skaitļu masīvu A(n m). Atrast to rindiņu skaitu, kurās ir kaut vai viens elements, kas ir vienāds ar nulli. Skaitļu masīvu izvadīt uz ekrāna. 
import random

rows = (random.randrange(0, 7)) #ģenerē nejaušus skaitļus rindām
cols = (random.randrange(0, 7)) #ģenerē nejaušus skaitļus kolonnām
arr = [] #masīva nosaukums
sum = []
p = 0
for i in range(rows):
    col = []
    for j in range(cols):
        sk = random.randrange(0,5)
        col.append(sk)
        if sk == 0:   
           p+=1
           i+=1  

for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end="\t")
    print()
print("Rindiņu skaits, kurās ir cipars, kas vienāds ar 0:",p)
print()
#4)Sastādīt programmu, kas ģenerē nejaušu skaitļu masīvu A(n m) un izvada atbildi “jā” vai “nē” atkarībā no tā, vai dotajā matricā A[n m.] ir sastopams skaitlis 7 vai nav. Skaitļu masīvu izvadīt uz ekrāna. 