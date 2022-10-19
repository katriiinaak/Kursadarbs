import random
n=int(input("Cik skaitļus ievadīsim?:"))
sk=[]
p=0
k=0
for i in range(1,n+1):
    a=random.randrange(1,100)
    sk.append(a)
if a%2==0:
    p+=1
else:
    k+=1
    print(sk)
    print(f"Sarakstā ir {p} pāra skaitļi un {k} nepāra skaitļi.")
if p>k:
    print("Sarakstā ir vairāk pāra skaitļu.")
elif p==k:
    print("Sarakstā ir vienāds skaits pāra un nepāra skaitļu.")
else:
    print("Sarakstā ir vairāk nepāra skaitļu.")