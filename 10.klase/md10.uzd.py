import random
sk=[]
summa = 0
n = int(input("Cik skaitļus ievadīsim? Līdz 50 skaitļiem: "))
for i in range(1,n+1):
    a = random.randrange(1,1000)
    summa += a
    sk.append(a)
#visus masīva elementus
print(sk)
#visu skaitļu viējo aritmētisko

print("Skaitļu vidējais aritmētiskais ir")
print("Lielākais skaitlis ir,",sk[n-1],"bet mazākais skaitlis ir")
print(f"Sarakstā ir {a} pāra skaitļi un {sk} nepāra skaitļi.")