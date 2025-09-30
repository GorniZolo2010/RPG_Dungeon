class consumables:
    def __init__(self,input_info):
        self.name = input_info
        self.time = consumables_dict[input_info]["time"]
    def const_heal(self,hero_obj):
        hero_obj.hp += consumables_dict[self.name]["hp"]
        hero_obj.inventory.remove(self.name)
        return hero_obj
    def delayed_heal(self,hero_obj):
        if self.time > 0:
            hero_obj.hp += consumables_dict[self.name]["hp"]
            self.time -= 1
        else:
            hero_obj.inventory.remove(self.name)
        return hero_obj
consumables_dict = {
    "healing consumables":{
    "Mushrooms":{"hp":25,"time":1},
    "Healing potion":{"hp":10,"time":5}
    }
}