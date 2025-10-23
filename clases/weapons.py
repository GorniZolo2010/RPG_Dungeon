import clases
import random
class weapon:
    def __init__(self,info_list):
        self.name = info_list[0]
        self.atk = info_list[1]
        self.time = info_list[2]
    def fists():
        name = "Fists"
        atk = 3
        time = 0.5
        info = [name,atk,time]
        return info
    def sword():
        name = "Sword"
        atk = 13
        time = 1
        info = [name,atk,time]
        return info
    def dagger():
        name = "Dagger"
        atk = 6
        time = 0.5
        info = [name,atk,time]
        return info
    def mace():
        name = "Mace"
        atk = 30
        time = 2
        info = [name,atk,time]
        return info