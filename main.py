import random
import clases.classes as classes 
import something.shop as shop
import something.fight as fight
stage = 0
hero_info = classes.hero.info()
hero_obj = classes.hero(hero_info)
while True:
    monster_in_batle = random.choice(classes.monsters_list)
    info_monster = classes.monster.info(monster_in_batle)
    monster_obj = classes.monster(info_monster,monster_in_batle,stage)
    stage += 1
    fight.battle(hero_obj,monster_obj)
    if hero_obj.hp <= 0:
        print("Game over")
        break
    if hero_obj.xp > 100.00 + (50 * hero_obj.lvl):
        classes.hero.lvl_up(hero_obj)
        print(f"LVL up now your lvl is {hero_obj.lvl}")
        hero_obj.xp = 0
    if stage % 10 == 0:
        shop.shop(hero_obj)
        for i in len(hero_obj.inventory):
            print(f"{hero_obj.inventory[i]} X {hero_obj.inventory.count(hero_obj.inventory[i])}")