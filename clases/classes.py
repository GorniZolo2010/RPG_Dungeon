import random
class hero:
    def __init__(self):
        self.hp = 100
        self.atk_multiplier = 1
        self.lvl = 0
        self.xp = 0
        self.gold = 0
        self.inventory = []
        self.status = 0
        self.weapon = "Fists" 
        self.time_atk = 1
    def lvl_up(self):
        self.lvl += 1
        self.hp = round(self.hp * 1.1)
        self.atk += 0.1
        print(f"You are now lvl {self.lvl}!")
        print(f"Your hp is now {self.hp}!")
        print(f"Your atk min is now {self.atk_min}!")
        print(f"Your atk max is now {self.atk_max}!")
class monster:
    def __init__(self,info_list,name,stage):
        self.hp_monster = round(int(info_list[0])* (1 + 0.1 * stage))
        self.atk_max = round(int(info_list[2]) * (1 + 0.1 * stage))
        self.atk_min = round(int(info_list[1]) * (1 + 0.1 * stage))
        self.xp_min = info_list[3]
        self.xp_max = info_list[4]
        self.gold = info_list[5]
        self.name = name
    def monster_atacks(self,hp_hero):
        damage = random.randint(int(self.atk_min),int(self.atk_max))
        print(f"{self.name} atacks you with {damage} amount of damage!")
        hp_hero = hp_hero - damage
        return hp_hero
    def info(monster_in_batle):
        hp_monster = monsters_stats[monster_in_batle]["hp"]
        atk_min = monsters_stats[monster_in_batle]["atk_min"]
        atk_max = monsters_stats[monster_in_batle]["atk_max"]
        xp_min = monsters_stats[monster_in_batle]["xp_min"]
        xp_max = monsters_stats[monster_in_batle]["xp_max"]
        gold = monsters_stats[monster_in_batle]["gold"]
        name = monster_in_batle
        info = [hp_monster,atk_min,atk_max,xp_min,xp_max,gold,name]
        return info
    def monster_gets_hurt(self,hero_obj,weapon_obj):
        if hero_obj.time_atk < weapon_obj.time:
            hero_obj.time_atk += 1
            return self.hp_monster
        if hero_obj.time_atk > 1:
            damage = weapon_obj.atk
            self.hp_monster = self.hp_monster - damage
            print(f"You atack {self.name} with {damage} amount of damage!")
            return self.hp_monster
        else:
            times_to_attack = 1 / weapon_obj.time
            damage = times_to_attack * weapon_obj.atk
            self.hp_monster = self.hp_monster - damage
            print(f"You atack {self.name} with {damage} amount of damage!")
            return self.hp_monster
monsters_stats = {
    "Slime": {"hp":20, "atk_min": 2,"atk_max": 2, "xp_min" : 10, "xp_max" : 15,"gold" : 5},
    "Mouse": {"hp":17, "atk_min": 1,"atk_max": 1, "xp_min" : 9, "xp_max" : 10,"gold" : 5},
    "Bee": {"hp":14, "atk_min": 6,"atk_max": 10, "xp_min" : 8, "xp_max" : 13,"gold" : 5},
    "Frog": {"hp":17, "atk_min": 1,"atk_max":3, "xp_min" : 10, "xp_max" : 15,"gold" : 5}
}
monsters_list = ["Slime","Mouse","Bee","Frog"]