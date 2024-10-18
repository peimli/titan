import random
class Warrior:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def attack(self, other_warrior):
        return other_warrior.health - self.atttack_power
    def is_alive(self):
        if self.health > 0:
            True
        else:
            False
harcos1 = Warrior(input('Adja meg az egyes számú játékos a nevét'), 100, random.randint(0,100))
harcos2 = Warrior(input('Adja meg az kettes számú játékos a nevét'), 100, random.randint(0,100))

while harcos1.is_alive() and harcos2.is_alive():
    print(a)