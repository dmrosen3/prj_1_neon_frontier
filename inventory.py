from type_out import type_out
from weapon import Weapon, Consumable, nova_sword, fists, blaster


class Inventory:
    def __init__(self) -> None:
        self.weapons = []
        self.consumables = []



    def add_item(self, item):


        inv_list = self.weapons if isinstance (item, Weapon) else self.consumables
        for inv_item in inv_list:
            if inv_item.name == item.name:
                inv_item.quantity += 1
                return
            
        item.quantity = 1
        inv_list.append(item)

        

    def view_inventory(self):
        type_out("Weapons: \n")

        if len(self.weapons) == 0:
            type_out("---None---")

        elif len(self.weapons) > 0:
            for w in self.weapons:
                type_out(f" -  {w.name} x{w.quantity} \n")

        type_out("Consumables: \n")

        if len(self.consumables) == 0:
            type_out("---None---")
            
        elif len(self.consumables) > 0:
            for c in self.consumables:
                type_out(f" -  {c.name} x{c.quantity} \n")

    def view_weapons(self):
        type_out("Weapons: \n")

        if len(self.weapons) == 0:
            type_out("---None---")

        elif len(self.weapons) > 0:
            for w in self.weapons:
                type_out(f" -  {w.name} \n")


    def view_weapons_for_use(self):    
        type_out("Which weapon would you like to equip?")
        type_out("Weapons: \n")
        if len(self.weapons) == 0:
            type_out("---None---")
            
        elif len(self.weapons) > 0:
            for i, item in enumerate(self.weapons, start=1):
                type_out(f"[{i}] {item.name}")

    def view_consumables_for_use(self):    
        type_out("Which item would you like to use?")
        type_out("Consumables: \n")
        
    

        if len(self.consumables) == 0:
            type_out("---None---")
            
        elif len(self.consumables) > 0:
            for i, item in enumerate(self.consumables, start=1):
                type_out(f"[{i}] {item.name} (x{item.quantity})")

   
        