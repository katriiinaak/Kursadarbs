"""
1. Atbildēt uz jautājumiem par savu zirgu
"""
MAPE = "faili/"
fails = MAPE + "aptauja.txt"
f = open(fails, 'a', encoding="UTF-8")
MAPE = "faili/" #uztaisu mainīgo, kas ir fails
fails = MAPE + "aptauja.txt" #secība, kā nokļūstt aptaujā
f = open(fails, 'a', encoding="UTF-8") #definē f, pievieno aptaujā to, ko vajag

print()
print("Sveiki! Atbildot uz jautājumiem, uzzināsi, vai disciplīna, kuru šobrīd trenējies, der tavam zirgam?")
f.write("Sveiki! Atbildot uz jautājumiem, uzzināsi, vai disciplīna, kuru šobrīd trenējies, der tavam zirgam?" + "\n")
print() #izveido atstrpi, lai skaistāk
print("Sveiki! Atbildot uz jautājumiem, uzzināsi, kura disciplīna ir piemērotāka tavam zirgam!")
f.write("Sveiki! Atbildot uz jautājumiem, uzzināsi, vai disciplīna, kuru šobrīd trenējies, der tavam zirgam!" + "\n")
print()

ko = 0 #mainīgie, kas skaitīs atbildes
ie = 0
kr = 0
   
for i in range(12):    
    print("1.Kādā disciplīnā šobrīd trenējaties?")
    f.write("1.Kādā discpilīnā šobrīd trenējaties?" + "\n")
    k = int(input("Atbilžu varianti: 1-Konkūrs; 2-Iejāde; 3-Kross: "))
    f.write("Lietotājs ievadīja" + str(k) + "\n")
    if k == 1:
      f.write("1.Kādā discpilīnā šobrīd trenējaties?" + "\n") #pievieno tekstu uz aptaujas failu (\n-pievieno jaunu teikumu nākamajā rindiņā)
    k = int(input("Atbilžu varianti: 1-Konkūrs; 2-Iejāde; 3-Kross: ")) #paprasa aptaujas veicējam ievadīt atbildi
    f.write("Lietotājs ievadīja" + str(k) + "\n") #str(k)-datu tips, kas parāda tekstu, ko ievadīja lietotājs
    if k == 1: #skaita atbildes
        ko += 1
    elif k == 2:
        ie += 1
    else:
        kr += 1
    print("2.Vai tavs zirgs izbauda disciplīnu, kurā trenējaties?")
    f.write("2.Vai tavs zirgs izbauda disciplīnu, kurā trenējaties?" + "\n")
    d = int(input("Atbildžu varianti: 1-Jā; 2-Nē; 3-Nezinu: "))
    f.write("Lietotājs ievadīja" + str(d) + "\n")
    if d == 1:
        ko += 1
    elif d == 2:
        ie += 1
    else:
        kr += 1
    print("3.Kādā šķirnes grupā ir tavs zirgs?")
    f.write("3.Kādā šķirnes grupā ir tavs zirgs?" + "\n")
    e = int(input("Atbilžu varianti: 1-Siltasiņu(piem.Hanoveras, Holšteinas, Latvijas); 2-Aukstasiņu(piem.Frīzs, Šīres); 3-Karstasiņu(piem.Arābs, tīrasiņu): "))
    f.write("Lietotājs ievadīja" + str(e) + "\n")
    if e == 1:
        ko += 1
    elif e == 2:
        ie += 1
    else:
        kr += 1
    print("4.Cik vecs ir zirgs?")
    f.write("4.Cik vecs ir zirgs?" + "\n")
    m = int(input("Atbilžu varianti: 1-3-7 gadi; 2-7-14 gadi; 3-14+ gadi: "))
    f.write("Lietotājs ievadīja" + str(m) + "\n")
    if m == 1:
        ko += 1
    elif m == 2:
        ie += 1
    else:
        kr += 1
    print("5.Zirga dzimums?")
    f.write("5.Zirga dzimums?" + "\n")
    l = int(input("Atbilžu varianti: 1-Ķēve; 2-Kastrāts; 3-Ērzelis: "))
    f.write("Lietotājs ievadīja" + str(l) + "\n")
    if l == 1:
        ko += 1
    elif l == 2:
        ie += 1
@@ -70,27 +70,27 @@
        f.write("6.Kāda ir zirga ķermeņa masa?" + "\n")
    c = int(input("Atbilžu varianti: 1-Ideāli sportiska forma, skaisti muskuļains; 2-Tievs, garām kājām; 3-Apaļīgs, masīvs, lieli muskuļi: "))
    f.write("Lietotājs ievadīja" + str(c) + "\n")
    if c == 1:
        ko += 1
    elif c == 2:
        ie += 1
    else:
        kr += 1
    print("7.Kāds ir zirga raksturs?")
    f.write("7.Kāds ir zirga raksturs?" + "\n")
    r = int(input("Atbilžu varianti: 1-Traks, nepacietīgs, sportisks; 2-Nosvērts, mierīgs, gudrs, graciozs; 3-Ātrs, enerģisks, veikls: "))
    f.write("Lietotājs ievadīja" + str(r) + "\n")
    if r == 1:
        ko += 1
    elif r == 2:
        ie += 1
    else:
        kr += 1
    print("8.Kā tavs zirgs uzvedas aplokā?")
    f.write("8.Kā tavs zirgs uzvedas aplokā?" + "\n")
    b = int(input("Atbilžu varianti: 1-Pastaigājas, lēkā pa aploku; 2-Atkārto kustības, ko esi mācījis; 3-Nepārtraukti skrien: "))
    f.write("Lietotājs ievadīja" + str(b) + "\n")
    try:
    try: #nodrošina datu ievades pareizību
        print(b)
    except:
        print("Atbildes numurs, ko ievadījāt, nav definēts!")
        f.write("Atbildes numurs, ko ievadījāt, nav definēts!" + "\n")
    if b == 1:
        ko += 1
    elif b == 2:
        ie += 1
    else:
        kr += 1
    print("9.Kādā ātrumā tavam zirgam patīk piedalīties treniņos, sacensībās?")
    f.write("9.Kādā ātrumā tavam zirgam patīk piedalīties treniņos, sacensībās?" + "\n")
    s = int(input("Atbilžu varianti: 1-Vidēji; 2-Pielāgojas man; 3-Ātri: "))
    f.write("Lietotājs ievadīja" + str(s) + "\n")
    if s == 1:
        ko += 1
    elif s == 2:
        ie += 1
    else:
        kr += 1
    print("10.Vai zirgs baidās no priekšmetiem, lietām vai citiem zirgiem?")
    f.write("10.Vai zirgs baidās no priekšmetiem, lietām vai citiem zirgiem?" + "\n")
    h = int(input("Atbilžu varianti: 1-Dažreiz; 2-Jā; 3-Nē: "))
    f.write("Lietotājs ievadīja" + str(h) + "\n")
    if h == 1:
        ko += 1
    elif h == 2:
        ie += 1
    else:
        kr += 1
    print("11.Kāda veida treniņus jūsu zirgs vairāk izbauda?")
    f.write("11.Kāda veida treniņus jūsu zirgs vairāk izbauda?" + "\n")
    n = int(input("Atbilžu varianti: 1-Lekšana; 2-Figūru izpilde; 3-Izturības treniņi: "))
    f.write("Lietotājs ievadīja" + str(n) + "\n")
    if n == 1:
        ko += 1
    elif n == 2:
        ie += 1
    else:
        kr += 1
    #if
    break
    break #pabeidz ciklu



if ie < ko > kr:
if ie < ko > kr: #nosaka, kuru atbilžu variantu skaitļu bija visvairāk
    print("Piemērotāka disciplīna tavam zirgam ir konkūrs!")
    f.write("Piemērotāka disciplīna tavam zirgam ir konkūrs!" + "\n")
elif kr < ie > ko:
    print("Piemērotāka disciplīna tavam zirgam ir iejāde!")
    f.write("Piemērotāka disciplīna tavam zirgam ir iejāde!" + "\n")
else:
    print("Piemērotāka disciplīna tavam zirgam ir kross!")
    f.write("Piemērotāka disciplīna tavam zirgam ir kross!" + "\n")



print("Vai ir nepieciešams izstrādāt treniņu plānu divām nedēļām?")
f.write("Vai ir nepieciešams izstrādāt treniņu plānu mēnesim?" + "\n")
print("Vai ir nepieciešams izstrādāt treniņu plānu divām nedēļām un atbilstošo barību?")
f.write("Vai ir nepieciešams izstrādāt treniņu plānu mēnesim un atbilstošo barību?" + "\n")
y = int(input("Atbilžu varianti: 1-Jā; 2-Nē: " ))

rindas, kolonas = 3, 8
kon = [[None] * kolonas for i in range(rindas)]
konk = ["Ieteicamā barība: Augstas kvalitātes siens, granulas, musli, vitamīni-olbaltumvielas, kalcijs, fosfors. "]

rindas, kolonas = 3, 8 #parāda cik rindu un kolonu būs sarakstā
kon = [[None] * kolonas for i in range(rindas)] #uztaisa tukšu tabulu, lai pēctam ievadītu datus tajā

kon[0][0] = " "
kon[0][1] = "Pirmdiena"
kon[0][2] = "Ordiena"
kon[0][3] = "Trešdiena"
kon[0][4] = "Ceturtdiena"
kon[0][5] = "Piektdiena"
kon[0][6] = "Sestdiena"
kon[0][7] = "Svētdiena"
kon[1][0] = "Pirmā nedēļa"
kon[1][1] = "Hordošana 30min"
kon[1][2] = "Rikšu slodze"
kon[1][3] = "Vingrojumi"
kon[1][4] = "Lekšana"
kon[1][5] = "Lēkšu slodze"
kon[1][6] = "Soļu slodze"
kon[1][7] = "Atpūta"
kon[2][0] = "Otrā nedēļa"
kon[2][1] = "Rikšu slodze"
kon[2][2] = "Lēkši, figūras"
kon[2][3] = "Vingrojumi"
kon[2][4] = "Locīšanās"
kon[2][5] = "Lekšana"
kon[2][6] = "Lēkšu slodze"
kon[2][7] = "Maršruts"
"""
for i in range(rindas):
    for j in range(kolonas):
        print(kon[i][j], end="\t")
"""


ieja = ["Ieteicamā barība: Mitrinātas auzas, augstas kvalitātes siens, papildbarība+vitamīni. "]

rindas, kolonas = 3, 8
iej = [[None] * kolonas for i in range(rindas)]

iej[0][0] = " "
iej[0][1] = "Pirmdiena"
iej[0][2] = "Ordiena"
iej[0][3] = "Trešdiena"
iej[0][4] = "Ceturtdiena"
iej[0][5] = "Piektdiena"
iej[0][6] = "Sestdiena"
iej[0][7] = "Svētdiena"
iej[1][0] = "Pirmā nedēļa"
iej[1][1] = "Soļošana"
iej[1][2] = "Hordošana 20min"
iej[1][3] = "Rikši, locīšanās"
iej[1][4] = "Kārtiņas, locīšanās"
iej[1][5] = "Lēkšu slodze"
iej[1][6] = "Lēkši taisnās līnijās"
iej[1][7] = "Gaitas un pārejas"
iej[2][0] = "Otrā nedēļa"
iej[2][1] = "Atpūta"
iej[2][2] = "Hordošana 45min"
iej[2][3] = "Rikši, lēkši, locīšanās"
iej[2][4] = "Taisnas līnijas"
iej[2][5] = "Kārtiņas un uzdevumi"
iej[2][6] = "Locīšanās"
iej[2][7] = "PAstaiga apvidū"



kros = ["Ieteicamā barība: Granulas, augstas kvalitātes siens, zaļbarība+vitamīni. "]

rindas, kolonas = 3, 8
kro = [[None] * kolonas for i in range(rindas)]

kro[0][0] = " "
kro[0][1] = "Pirmdiena"
kro[0][2] = "Ordiena"
kro[0][3] = "Trešdiena"
kro[0][4] = "Ceturtdiena"
kro[0][5] = "Piektdiena"
kro[0][6] = "Sestdiena"
kro[0][7] = "Svētdiena"
kro[1][0] = "Pirmā nedēļa"
kro[1][1] = "Hordošana 20min"
kro[1][2] = "Viegls skrējiens 3km"
kro[1][3] = "Pamata treniņš"
kro[1][4] = "Viegls skrējiens, lecieni"
kro[1][5] = "Locīšanās"
kro[1][6] = "Izturības skrējiens"
kro[1][7] = "Hordošana 20min"
kro[2][0] = "Otrā nedēļa"
kro[2][1] = "Atpūta"
kro[2][2] = "Viegls skrējiens 3km"
kro[2][3] = "Viegls skrējiens, lecieni"
kro[2][4] = "Locīšanās, lecieni"
kro[2][5] = "Hordošana 20min"
kro[2][6] = "Viegls skrējiens, lecieni"
kro[2][7] = "Izturības skrējiens"



if y == 2:
if y == 2: #ja atbildēja 'nē', tad pabeidz aptauju
    print("Paldies, ka izpildījāt šo aptauju!")
    f.write("Paldies, ka izpildījāt šo aptauju!" + "\n")
elif y == 1:
    if ie < ko > kr:
        for i in range(rindas):
elif y == 1: #ja atbildēja 'jā', tad izvada atbilstošo sarakstu
    if ie < ko > kr: 
        for i in range(rindas): #sarakstu izvada kā tabulu
            for j in range(kolonas):
                print(kon[i][j], end="\t")
            print()
        print()
        print(konk, end=" ")

    elif kr < ie > ko:
        for i in range(rindas):
            for j in range(kolonas):
                print(iej[i][j], end="\t")
            print()
        print()
        print(ieja, end=" ")
    else:
        for i in range(rindas):
            for j in range(kolonas):
                print(kro[i][j], end="\t")
            print()
        print()
        print(kros, end=" ")


