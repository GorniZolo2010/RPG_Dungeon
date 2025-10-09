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
            print(shop_list)
            while True:
                print("Choose thing that you want to buy, or print Exit to go back to field")
                input_info = input()
                input_info = input_info.lower().capitalize()
                if input_info == "Exit":
                    break
                elif shop_list.count(input_info) != 0:
                    if hero_obj.gold < shop_asortiment[input_info]:
                        print("You don`t have enough gold")
                    else:
                        hero_obj.gold = hero_obj.gold - shop_asortiment[input_info]
                        number = shop_list.index(input_info)
                        hero_obj.inventory.append(shop_list[number])
        else:
            print("Try again pls")
shop_list = ["Mushrooms","Healing potion"]
shop_asortiment = {
    "Mushrooms": 50,
    "Healing potion": 100
}