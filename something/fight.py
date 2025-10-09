import random
import clases.classes as classes
import something.shop as shop
import clases.consumables as consumables
def Turn_based_combat(hero_obj,monster_obj):
    while True:
        input_info = input("Defense Atack Inventory: ")
        input_info = input_info.lower().capitalize()
        if input_info == "Defense":
            info_1 = monster_obj.atk_max - monster_obj.atk_max / 4
            info_2 = monster_obj.atk_min - monster_obj.atk_min / 4
            print(f"Monster ATK has decreasd by {info_1}/{info_2}")
            monster_obj.atk_max /= 4
            monster_obj.atk_min /= 4
            return hero_obj,monster_obj,None
        elif input_info == "Atack":
            monster_obj.hp_monster = classes.monster.monster_gets_hurt(monster_obj,hero_obj)
            return hero_obj,monster_obj,None
        elif input_info == "Inventory":
            if hero_obj.inventory == []:
                print("You don`t have any item")
            else:
                if hero_obj.inventory.count("Healing potion") > 0:
                    print(f"Healing potion X{hero_obj.inventory.count("Healing potion")}")
                if hero_obj.inventory.count("Mushrooms") > 0:
                     print(f"Mushrooms X{hero_obj.inventory.count("Mushrooms")}")
                input_info = input("Write what you want to use: ")
                input_info = input_info.lower().capitalize()
            if hero_obj.inventory.count(input_info) != 0:
                if input_info not in consumables.consumables_dict["healing consumables"]:
                    print("You can`t use that item")
                else:
                    status_obj = consumables.consumables(input_info)
                    consumables.consumables.give_status(status_obj,hero_obj)
                    if hero_obj.status == 1:
                        hero_obj = status_obj.const_heal(hero_obj)
                        print(f"You healed {status_obj.heal} hp")
                    else:
                        hero_obj = status_obj.delayed_heal(hero_obj)
                        print(f"You healed {status_obj.heal} hp, and it will heal you for {hero_obj.status} turns more")
                return hero_obj,monster_obj,status_obj
            else:
                print("You don't have that item")
def battle(hero_obj,monster_obj):
    monster_in_batle = monster_obj.name
    turn = 0
    status = False
    while True:
        if turn == 0:
            print(f"{monster_in_batle} attacking you!")
        if monster_obj.hp_monster > 0:
            if status != False:
                info = Turn_based_combat(hero_obj,monster_obj)
                hero_obj = info[0]
                monster_obj = info[1]
            else:
                hero_obj,monster_obj,status_obj = Turn_based_combat(hero_obj,monster_obj)
                if hero_obj.status > 1:
                    status = True
            if monster_obj.hp_monster >= 0:
                print(f"{monster_in_batle} hp now is {monster_obj.hp_monster}")
            else:
                print(f"{monster_in_batle} hp now is 0")
            if monster_obj.hp_monster > 0:
                hero_obj.hp = classes.monster.monster_atacks(monster_obj,hero_obj.hp)
                if hero_obj.hp >= 0:
                    if hero_obj.status > 0:
                        hero_obj = consumables.consumables.delayed_heal(status_obj,hero_obj)
                        print(f"You healed {status_obj.heal} hp, and it will heal you for {hero_obj.status} turns more")
                    print(f"Hero hp now is {hero_obj.hp}")
                else:
                    print("Hero hp now is 0")
        elif monster_obj.hp_monster <= 0:
            print(f"{monster_in_batle} is dead!")
        if monster_obj.hp_monster <= 0:
            print("You win!")
            hero_obj.xp += random.randint(monster_obj.xp_min,monster_obj.xp_max)
            hero_obj.gold += monster_obj.gold
            print(f"You gold now {hero_obj.gold},and xp now {hero_obj.xp}")
            break
        elif hero_obj.hp <= 0:
            print("You lose =(")
            break
        turn += 1
    return hero_obj
shop_list = ["Mushrooms"]
shop_asortiment = {
    "Mushrooms": {"cost":50,"hp_heal":25}
}