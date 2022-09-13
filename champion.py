import random


class Champion:

    def __init__(self, name, hp, ad, crt, ap, armor, mr, land):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.crt = crt
        self.ap = ap
        self.armor = armor
        self.mr = mr
        self.land = land

    def auto_attack(self, other_champion):
        other_champion.hp -= self.damage_multi(other_champion)

    def damage_multi(self, other_champion):
        if other_champion.armor >= 0:
            return self.crt_multi() * (self.ad * (100 / (100 + other_champion.armor)))
        else:
            return self.crt_multi() * (self.ad * (2 - (100 / (100 - other_champion.armor))))

    def crt_multi(self):
        if random.randrange(0, 100) <= self.crt:
            return 2
        else:
            return 1

    def add_item(self, item):
        self.hp += item.hp
        self.ad += item.ad
        self.crt += item.crt
        self.ap += item.ap
        self.armor += item.armor
        self.mr += item.mr