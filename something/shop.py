def shop(hero_obj):
    while True:
        info = ["Write See to see asortiment of shop","Write Exit to leave shop"]
        for i in info:
            print(i)
        input_info = input()
        input_info = input_info.lower().capitalize()
        if input_info == "Exit":
            return hero_obj
        elif input_info == "See":
            print(category_list)
            while True:
                print("Choose category that you want to buy, or print Exit to go back to field")
                input_info = input()
                input_info = input_info.lower().capitalize()
                if input_info == "Exit":
                    break
                elif input_info == "Weapons":
                    print(shop_asortiment["Weapons"])
                    print("Choose weapon that you want to buy")
                    input_info = input()
                    input_info = input_info.lower().capitalize()
                    if hero_obj.gold < shop_asortiment["Weapons"][input_info]:
                        print("You don`t have enough gold")
                    elif hero_obj.weapon == input_info:
                        print("You already have this weapon")
                    else:
                        hero_obj.gold = hero_obj.gold - shop_asortiment["Weapons"][input_info]
                        number = shop_list.index(input_info)
                        hero_obj.weapon = shop_list[number]
                elif input_info == "Consumables":
                    print(shop_asortiment["Consumables"])
                    print("Choose consumable that you want to buy")
                    input_info = input()
                    input_info = input_info.lower().capitalize()
                    if hero_obj.gold < shop_asortiment["Consumables"][input_info]:
                        print("You don`t have enough gold")
                    else:
                        hero_obj.gold = hero_obj.gold - shop_asortiment["Consumables"][input_info]
                        number = shop_list.index(input_info)
                        hero_obj.inventory.append(shop_list[number])
        else:
            print("Try again pls")
category_list = ["Consumables","Weapons"]
shop_list = ["Mushrooms","Healing potion","Sword","Mace","Dagger"]
shop_asortiment = {
    "Consumables":{ "Mushrooms": 50,"Healing potion": 100,},
    "Weapons":{"Sword":150,"Mace":125,"Dagger":120}
    }
