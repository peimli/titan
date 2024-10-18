#1. Feladat: Osztás nullával
print("1. feladat:\n")
a = int(input("Adjon meg egy számot!"))
b = int(input("Adjon meg egy másik számot!"))
try:
    print(f"{b // a}")
except ZeroDivisionError:
    print("Nem lehet elvégezni a műveletet")

#2. Feladat: Helytelen adattípus
print("\n2.feladat:\n")
a = input("Adjon meg egy számot!")
try:
    print(int(a) ** 2)
except ValueError:
    print("helytelen adattípust adott meg")
#3. Feladat: Fájl olvasása
print("\n3.feladat:\n") 
try:
    f = open("demofile.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Fájl nem létezik!")

#4. Feladat: Lista elem lekérése index alapján
'''
Leírás: Készíts egy programot, amely egy listából kér le elemeket egy megadott index alapján.
	Kérj be egy indexet a felhasználótól, és próbáld meg kiolvasni az
	adott indexű 	elemet a listából. Ha az index kívül esik a lista határain, kezelje a program a hibát.
'''
print("\n4.feladat:\n")
a = ["alma", "kígyó", "banán", "körte"]
indeksz = int(input("Adja meg az indexet"))
try:
    print(a[indeksz])
except IndexError:
    print("nincs ilyen index")
    