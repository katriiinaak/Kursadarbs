#7. Pieprasīt (ģenerēt nejaušus skaitļus) masīvu, kas satur N veselus skaitļus, paziņot, kādu skaitļu tajā vairāk: pāra vai nepāra.
import random
n = int(input("Ievadi, cik skaitļu būs sarakstā:"))
sk = []
p = 0
for i in range(1, n+1):
    a = random.randrange(1, 100) #šāda skaitļu ģenerēšana atvieglo testēšanu
    sk.append(a) #pievieno skaitli sarakstam
    if a % 2 == 0: #procents rāda dalījuma atlikumu
       p+=1

print(sk) #izvadam skaitļu masīvu

if n-p > p:
   print("Vairāk ir nepāra skaitļu un to ir", n-p, "no", n, "skaitļiem.")
elif n-p == p:
   print("Pāra skaitļu ir tikpat cik nepāra slaitļu un tie ir". n-p, "skaitļi.")
else:
   print("Vairāk ir pāra skaitļu un to ir", p, "no", n, "skaitļiem.")