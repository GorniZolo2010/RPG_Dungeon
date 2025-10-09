import random
import clases.classes as classes 
import something.shop as shop
import something.fight as fight
stage = 0
hero_info = classes.hero.info()
hero_obj = classes.hero(hero_info)
while True:
    hero_obj.inventory.append("Healing potion")
    hero_obj.inventory.append("Mushrooms")
    hero_obj.gold = 100000000
    monster_in_batle = random.choice(classes.monsters_list)
    info_monster = classes.monster.info(monster_in_batle)
    monster_obj = classes.monster(info_monster,monster_in_batle,stage)
    stage += 1
    fight.battle(hero_obj,monster_obj)
    print(f"hero hp: {hero_obj.status}")
    if hero_obj.hp <= 0:
        print("Game over")
        break
    if hero_obj.xp > 100.00 + (50 * hero_obj.lvl):
        classes.hero.lvl_up(hero_obj)
        print(f"LVL up now your lvl is {hero_obj.lvl}")
        hero_obj.xp = 0
    if stage % 1 == 0:
        shop.shop(hero_obj)
        if hero_obj.inventory.count("Healing potion") > 0:
            print(f"Healing potion X{hero_obj.inventory.count("Healing potion")}")
        if hero_obj.inventory.count("Mushrooms") > 0:
            print(f"Mushrooms X{hero_obj.inventory.count("Mushrooms")}")