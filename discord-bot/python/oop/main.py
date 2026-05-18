#committed: 27/11/2025
#---

import random

class Player: #class

    def __init__(self): #constructor. everything inside this function will automatically be inherited by the object created
        self.hp = 10
        self.atk = 10

    def statistics(self):
        print(f"HP: {self.hp}, ATK: {self.atk}")

    def attack(self):
        damage = random.randint(1, 10)
        print(f"You dealt {damage} damage!")

eruka = Player()
eruka.attack()
eruka.statistics()