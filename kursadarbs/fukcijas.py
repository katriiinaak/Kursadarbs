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