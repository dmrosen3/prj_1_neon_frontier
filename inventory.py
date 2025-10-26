from type_out import type_out
from weapon import Weapon, Consumable, nova_sword, fists, blaster


class Inventory:
    def __init__(self) -> None:
        self.weapons = []
        self.consumables = []
    def add_item(self, item):

        if isinstance(item, Weapon):
            self.weapons.append(item)
            #if item in self.weapons: right now, an item added to an inventory DOES NOT increase its quantity
                #item += 1            I need to reprogram the logic so that when a duplicate item is added
                                      # the number next to it in the inventory increses, rather than a duplicate item being added as a new entry
        elif isinstance(item, Consumable):
            self.consumables.append(item)
            #if item in self.consumables:
                #item += 1

        
            


    def view_inventory(self):
        type_out("Weapons: \n")

        if len(self.weapons) == 0:
            type_out("---None---")

        elif len(self.weapons) > 0:
            for w in self.weapons:
                type_out(f" -  {w.name} \n")

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

    def view_consumables_for_use(self):    
        type_out("Which item would you like to use?")
        type_out("Consumables: \n")
        
    

        if len(self.consumables) == 0:
            type_out("---None---")
            
        elif len(self.consumables) > 0:
            for i, item in enumerate(self.consumables, start=1):
                type_out(f"[{i}] {item.name} (x{item.quantity})")
        