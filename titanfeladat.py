import random

# 1.

lista = []
for i in range(10):
    szam = random.randint(0,100)
    lista.append(szam)
print("Lista:") 
print("    1.feladat: ", *lista)

print("    2.feladat: ","legnagyobb:", max(*lista), "legkisebb: ", min(*lista))

novekvo = sorted(lista)

print("    3.feladat: ", *novekvo)
paros = []
for szam in lista:
    if szam % 2 == 0:
        paros.append(szam)
print("    4.feladat: ", *paros)

# 2. set

halmaz1 = {"alma", "körte", "banán", "narancs", "szőlő"}
halmaz2 = {"alma", "eper", "barack", "szilva", "körte"}

print("Set:")
print("    1.feladat: ", *halmaz1, " , " , *halmaz2)

metszet = halmaz1 & halmaz2
print("    2.feladat: ", *metszet)
kulonbseg = halmaz1 - halmaz2
print("    3.feladat: ", *kulonbseg)
egyesites = halmaz1 | halmaz2
print("    4.feladat: ", *egyesites)

# 3. tuple

szavak = ("terem", "kocsi" , "szó", "alma", "banán", "madár", "kuka")

print("Tuple")

print("    1.feladat: ", *szavak)

ujszavak = szavak[:3] + szavak[-2:]

print("    2.feladat: ", *ujszavak)

elemszam = 0

for elemek in szavak:
    elemszam += 1

print("    3.feladat: ", elemszam)

masodikelemek = szavak[::2]

print("    4.feladat: ", *masodikelemek)

atlagok = {
    "Matematika": 4.5,
    "Fizika": 4.2,
    "Kémia": 4.0,
    "Magyar irodalom": 3.8,
    "Történelem": 4.0,
    "Angol nyelv": 4.8,
    "Biológia": 4.3,
    "Földrajz": 3.7,
    "Informatika": 5.0,
    "Zene": 4.1,
    "Testnevelés": 5.0,
    "Művészettörténet": 3.9
}

print("Dictionary")
print("    1.feladat: ")
for tantargy, jegyek in atlagok.items():
    print("        ", tantargy, jegyek)
#Frissítsd az egyik tantárgy átlagos jegyét!    
atlagok["Matematika"] = 4.8
#Adj hozzá egy új tantárgyat a szótárhoz!
atlagok["Filozófia"] = 3.0
legmagasabbjegy = max(atlagok, key=atlagok.get)

print("    5.feladat: ")
for tantargy, atlag in atlagok.items():
    if atlag > 4.5:
        print("        ", tantargy, atlag)








