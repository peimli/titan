import json
from bonyolult import beolvas

class Harcos:
    def __init__(self, nev, hp, inventory=None):
        self.nev = nev
        self.hp = hp
        self.inventory = inventory
    def __str__(self):
        return self.nev
    def __add__(self, masik):
        return self.hp + masik

adat = beolvas("harcosok.json")
harcosok = []
for harcos in adat["harcos"]:
    harcosok.append(Harcos(harcos["nev"], harcos["hp"], harcos["inventory"]))