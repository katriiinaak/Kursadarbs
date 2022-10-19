#Patstāvīgā darba uzdevumi programmēšanā stundai:

# 1) pildam Snakify uzdevumus par tēmām, kuras ir stundās risinātas: https://snakify.org,
# 2) studējam W3schools materiālus par List: https://www.w3schools.com/python/python_lists.asp
# 3) atsūtīt Slackčatā iepriekšējās stundas temperatūru uzdevuma risinājumu,

# 4) klases un mājas uzdevums līdz nākamai stundai:
# a) sastādīt programmu, kas ģenerē sarakstu, kas satur n nejaušus skaitļus (skaitļu diapazons no -50 līdz +50, n ievada lietotājs 0<n<100),
import random
sk = []
n =-1

while n < 0 or n > 100:
    n=int(input("Ievadi, cik skaitļu būs sarakstā?(ievadi skaitli intervālā no 1 līdz 100): "))  
    print("Šis skaitlis neder!")
    if n < 0:
        print("Šis skaitlis neder, jo ir mazāks par 0. Ievadi vēlreiz!")
    elif n > 100:
        print("Šis skaitlis neder, jo ir lielāks par 100. Ievadi vēlreiz!")
    

for i in range (n):
    sk.append(random.randrange(-50,50))
print(sk)

# b) iegūto sarakstu izvadīt, 
# c) lietotājam tiek pajautāts ievadīt skaitli x un programmai jāatrod pirmo saraksta elementu, kas ir mazāks par x un jāizvada to, kā arī jāizvada šī elementa kārtas numurs sarakstā, 
x = int(input("Ievadiet skaitli no -50 līdz 50: "))
for i in range(n):
    if x > sk[i]:
        print(f"Pirmais mazākais par {x} ir, {sk[i]}, tas ir {i} . ais saraksta elements." )
        break

# d) izmest no saraksta visas nulles, ja tādas ir, un iegūto sarakstu izvadīt,
while 0 in sk:
    sk.remove(0)
print(sk)

# e) izmest no saraksta visus skaitļus, kas atkārtojas un iegūto sarakstu izvadīt.
for i in range(-50, 51):
    if sk.count(i) > 1:
        while sk.count(i) > 1:
            sk.remove(i)

print(sk)
# f) papildināt sarakstu ar tādu skaitli no intervāla -50 līdz +50, kurš nav atrodams esošajā sarakstā un izvadīt šo pievienojamo skaitli un iegūto sarakstu.
while s in sk:
    s = random.randrange(-50,50)
if s not in sk:
    print(f"Skaitlis {s} nav sarakstā! Pievienojam to!" )
    sk.append(s)

print("Ar papildināto skaitli:")
print(sk)
