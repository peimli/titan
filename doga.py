#1.Állatok hozzáadása:
allatok = []
szam = int(input("Adja meg hány állatot szeretne hozzáadni!"))
for i in range(szam):
    allat = input(f"Adja meg az {i+1}. állat nevét")
    cukisag = input(f"Adja meg hogy a {allat} mennyire cuki.")
    allatok.append((allat, cukisag))
#Állatok megjelenítése:
latni = input("Szeretné látni a állatok és hogy mennyire cukkerek? (igen/nem)")
if latni == "igen":
    print(f"Állat		|  Cukiság")
    print("------------------------------")
    for allat, pontszam in allatok:
        print(f" {allat}		|  {pontszam}")

#A csoport: Átlagos pontszám kiszámítása:
avg_latni = input("\nSzeretnéd tudni az átlagos pontszámot? (igen/nem):")
osszpont = 0
for allat, pont in allatok:
    osszpont += int(pont)
atlag = osszpont / len(allatok)
print(f"\nAz átlagos pontszám: {atlag}")
    
#Legmagasabb és legalacsonyabb pontszám megkeresése:
minmax_latni = input("\nSzeretnéd tudni a legmagasabb és a legalacsonyabb pontszámot? (igen/nem):")
if minmax_latni == "igen":
    print(f"Legalacsonyabb pontszám: {min((int(pontszam)) for allat, pontszam in allatok)}")
    print(f"Legmagasabb pontszám: {max((int(pontszam)) for allat, pontszam in allatok)}")
#eltavolitas
eltavolitas = input("\nSzeretnél eltávolítani egy állatot? (igen/nem):")
if eltavolitas == "igen":
    melyik = input("Melyik állatot szeretnéd eltávolítani?")
    for allat in allatok:
        if allat[0] == melyik:
            allatok.remove(allat)
            
#Állatok listája:
latni = input("Szeretné látni a állatok és hogy mennyire cukkerek? (igen/nem)")
if latni == "igen":
    print(f"Állat		|  Cukiság")
    print("------------------------------")
    for allat, pontszam in allatok:
        print(f" {allat}		|  {pontszam}")     
    