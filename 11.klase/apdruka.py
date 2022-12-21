"""
Draugiem jāaprēķina, cik izmaksās apdrukātu T-kreklu pasūtīšana un piegāde, ņemot vērā, ka cena ir
atkarīga no apdrukas veida un kreklu skaita, bet piegādes maksa ir atkarīga no pasūtījuma summas.
"""
"""
def aprekins(a, c):
    s = a * c
    print(“Summa: ” + s)

def f(a, b, c, d):
    r = a * b / d
    print(r)
    return r

def ievarijums(aboli_svars, cukurs_cena, cukurs_uz_kg):
    izmaksa_kg = cukurs_cena * cukurs_uz_kg
    izmaksas = izmaksa_kg * aboli_svars
    print(izmaksas)

def izmaksas_receptei(recepte, cena):
# Funkcija aprēķina izmaksas dotai receptei
# summējot visu sastāvdaļu izmaksas
    summa = 0
    for sastavdala in recepte:
      daudzums = recepte[sastavdala]
      summa += daudzums * cena[sastavdala]
      return summa

def izmaksas_kopa(aboli_svars, recepte, cenas):
# Funkcija aprēķina izmaksas dotam daudzumam ābolu
# izmantojot dotu recepti un cenu sarakstu
# Izmaksas uz vienu kilogramu ābolu
    izmaksas_kg = izmaksas_receptei(recepte, cenas) / recepte[“aboli”]
# Izmaksas uz doto daudzumu ābolu
ievarijuma_izmaksas = aboli_svars * izmaksas_kg
print(“Uz {} kg ābolu izmaksas būs {:.2f} EUR”.format(abolu_svars,
ievarijuma_izmaksas))
# Piemērs lietošanai
# recepte1 = {“cukurs”: 0.6, “kanelis”: 0.008, “aboli”: 2.0, “udens”: 0.2}
cenas1 = {“cukurs”: 0.75, “kanelis”: 30.0, “aboli”: 0.0, “udens”: 0.0}
izmaksas_kopa(15.0, recepte1, cenas1)
"""