class consumables:
    def __init__(self,input_info):
        self.name = (input_info)
        print(self.name)
        self.heal = consumables_dict["healing consumables"][self.name]["hp"]
    def give_status(self,hero_obj):
        hero_obj.status = consumables_dict["healing consumables"][self.name]["time"]
        hero_obj.inventory.remove(self.name)
        return hero_obj
    def const_heal(self,hero_obj):
        hero_obj.hp += consumables_dict["healing consumables"][self.name]["hp"]
        hero_obj.inventory.remove(self.name)
        return hero_obj
    def delayed_heal(self,hero_obj):
        if hero_obj.status > 0:
            hero_obj.hp += consumables_dict["healing consumables"][self.name]["hp"]
            hero_obj.status -= 1
        else:
            hero_obj.status.remove(self.name)
        return hero_obj
consumables_dict = {
    "healing consumables":{
    "Mushrooms":{"hp":25,"time":1},
    "Healing potion":{"hp":10,"time":5}
    }
}