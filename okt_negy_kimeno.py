"""Feladat: Diákjegyek Kezelése
Leírás: Készíts egy programot, amely diákok neveit és jegyeit kezeli! A program a következő funkciókat fogja ellátni:
"""
#1. Diákok hozzáadása:
diakok = []
#-Kérdezd meg a felhasználót, hogy hány diákot szeretne hozzáadni.
diakok_szama = int(input(f"\nHány diákot szeretnél hozzáadni? "))
#-Használj for ciklust, hogy a megadott számú diák nevét és jegyét bekérd.
for i in range(diakok_szama):
    nev = input(f"\nAdd meg az {i + 1} diák nevét.")
    jegy = input(f"\nAdd meg {nev}. jegyét.")
#-Tárold a neveket és a jegyeket egy listában, ahol minden diákot egy tuple-ként tárolsz (név, jegy).
    diakok.append((nev,jegy))

#2. Diákok kiírása:
#-Kérdezd meg a felhasználót, hogy szeretné-e megtekinteni az összes diákot.
diak_megtekintes = input(f"\nSzeretnéd látni az összes diákot? (igen/nem)")
if diak_megtekintes == "igen":
    print("\nDiákok listája:")
#-Ha igennel válaszol, írd ki a diákok nevét és jegyeit egy szépen formázott táblázatban.
    print("\n{:<15} | {:<10}".format("Név", "Jegy"))
    print("-" * 35)
    for nev, jegy in diakok:
        print("{:<15} | {:<10}".format(nev, jegy))

#3. Átlagos jegy számítása:
#Kérdezd meg a felhasználót, hogy szeretné-e tudni az összes diák átlagos jegyét.
atlag_megtekintes = input(f"\nSzeretnéd tudni az átlagos jegyet? (igen/nem)")
if atlag_megtekintes == "igen":
#-Használj for ciklust az átlagos jegy kiszámításához, és írd ki az eredményt.
        osszeg = sum(int(jegy) for nev, jegy in diakok)
        atlag = osszeg / len(diakok)
        print(f"Az átlagos jegy: {atlag:.1f}")
#4. Legmagasabb és legalacsonyabb jegy:
minmaxmegtekintes = input(f"\nSzeretnéd tudni a legmagasabb és legalacsonyabb jegyet? (igen/nem)")
if minmaxmegtekintes == "igen":
    print(f"Legmagasabb jegy: {max(int(jegy) for nev, jegy in diakok)} \nLegalacsonyabb jegy: {min(int(jegy) for nev, jegy in diakok)}")
    
#5. Diák eltávolítása:
#-Kérdezd meg a felhasználót, hogy szeretne-e eltávolítani egy diákot.
diak_torles = input("Szeretnél eltávolítani egy diákot? (igen/nem)")
if diak_torles == "igen":
    torles_nev = input("Add meg a diák nevét, akit el szeretnél távolítani:")
    vandiak = False
    for diak in diakok:
        if diak[0] == torles_nev:
            diakok.remove(diak)
            vandiak = True
            print(f"\n{torles_nev} eltávolítva.")
            break
    if not vandiak:
        print(f"\n{torles_nev} nevű diák nem található.")
            
diak_megtekintes = input(f"\nSzeretnéd látni az összes diákot? (igen/nem)")
if diak_megtekintes == "igen":
    print("\nDiákok listája:")
#-Ha igennel válaszol, írd ki a diákok nevét és jegyeit egy szépen formázott táblázatban.
    print("\n{:<15} | {:<10}".format("Név", "Jegy"))
    print("-" * 35)
    for nev, jegy in diakok:
        print("{:<15} | {:<10}".format(nev, jegy))      
            
            
            
            
            
            
            
            
            
            
            
        
        
