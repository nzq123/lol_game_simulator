from champion import Champion
from item import Item


ashe = Champion('ashe', 640, 75, 70, 0, 28, 28, 'freljord')

mf = Champion('miss fortune', 640, 80, 15, 0, 100, 28, 'bilgewater')

vlad = Champion('vladimir', 700, 50, 0, 0, 100, 30, 'bilgewater')

ie = Item('infinity edge', ad=75, crt=25)

warmog = Item('warmogs armor', hp=400, armor=30)

ga = Item('guardian angel', ad=50, armor=30)


# champion1.show()

ashe.auto_attack(mf)


print(ashe.crt, ashe.ad)
ashe.add_item(ie)
print(ashe.crt, ashe.ad)
ashe.add_item(ie)
print(ashe.crt, ashe.ad)
