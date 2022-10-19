# 1. Definēsim jaunu sarakstu un aizpildīsim to ar n nejaušiem skaitļiem no 1-20, n jāpajautā ievadīt lietotājam

import random
sk = []
n=int(input("Ievadiet, cik elementu būs sarakstā!:"))
for i in range (n):
    sk.append(random.randrange(1,20))

# 2. Izvadīsim iegūto sarakstu

print(sk)

# 3. Izvadīsim 1-mo saraksta elementu

print(sk[0])                                                                                                   

# 4. Izvadīsim pēdējo saraksta elementu

print(sk[-1])

# 5. Izvadīsim iepriekšpēdējo saraksta elementu

print(sk[-2])

# 6. Pievienosim sarakstam lietotāja ievadītu skaitli X

x=int(input("Ievadiet skaitli!:"))
sk.append(x)

# 7. Izvadīsim iegūto sarakstu ar jauno skaitli

print(sk)

# 8. Izdzēsīsim no saraksta pirmo elementu

sk.pop(0)

# 9. Izvadīsim tagad iegūto sarakstu 

print(sk)

# 10. Izvadīsim katru trešo saraksta elementu
i = 2
while i < len(sk):
    print(sk[i])
    i = i + 3
    
# 11. Izveidosim jaunu sarakstu, kur ir tikai pāra skaitļi no sākuma saraksta un beigās izvadīsim to summu 
# 12. Izveidosim jaunu sarakstu, kur ir tikai nepāra skaitļi no sākuma saraksta un beigās izvadīsim to summu 
# 13. Izvadīsim tikai tos skaitļus, kas dalās ar 3 
# 14. Visu saraksta skaitļu summu
# 15. Visu saraksta skaitļu vidējo aritmētisko, noapaļotu līdz 2 zīmēm aiz komata
# 16. Cik reizes sarakstā ir sastopams skaitlis `7`
# 17. Izvadīsim visus saraksta elementus sakārtotā augošā secībā 
# 18. Izvadīsim visus saraksta elementus sakārtotā dilstošā secībā