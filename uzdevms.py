"""
1. Atbildēt uz jautājumiem par savu zirgu

"""
MAPE = "faili/"
fails = MAPE + "aptauja.txt"
f = open(fails, 'a', encoding="UTF-8")

print()
print("Sveiki! Atbildot uz jautājumiem, uzzināsi, vai disciplīna, kuru šobrīd trenējies, der tavam zirgam?")
f.write("Sveiki! Atbildot uz jautājumiem, uzzināsi, vai disciplīna, kuru šobrīd trenējies, der tavam zirgam?" + "\n")
print()

ko = 0
ie = 0
kr = 0

for i in range(12):   
    print("1.Kādā disciplīnā šobrīd trenējaties?")
    f.write("1.Kādā discpilīnā šobrīd trenējaties?" + "\n")
    k = int(input("Atbilžu varianti: 1-Konkūrs; 2-Iejāde; 3-Kross: "))
    f.write("Lietotājs ievadīja" + str(k) + "\n")
    if k == 1:
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
    else:
        kr += 1
    print("6.Kāda ir zirga ķermeņa masa?")
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







print("Vai ir nepieciešams izstrādāt treniņu plānu mēnesim?")
f.write("Vai ir nepieciešams izstrādāt treniņu plānu mēnesim?" + "\n")
y = int(input("Atbilžu varianti: 1-Jā; 2-Nē: " ))






