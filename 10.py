'''
class User:
    def __init__(self, hp):
        self.hp = hp

def atk(self, target):
    pass

def take_dmg(self, dmg):
    self.hp -= dmg 

class Archer(User):
    def __init__(self, hp, agt):
        super().__init__(hp)
        self.agt = agt

    def atk(self, target):
        dmg = self.agt
        target.take_dmg(dmg)

class Warrior(User):
    def __init__(self, hp, strength):
        super().__init__(hp)
        self.strength = strength

def atk(self, target):
    dmg = self.strength
    target.take_dmg(dmg)

class Mage(User):
    def __init__(self, hp, mana):
        super().__init__(hp)
        self.mana = mana

def cast_spell(self, spell_name, target):
    if self.mana >= spell_name.mana_cost:
        spell_name.cast(target)
        self.mana -= spell_name.mana_cost
    else:
        print("Недостаточно маны")
'''

