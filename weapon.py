from type_out import type_out
from character import Hero
from health_bar import HealthBar

class Weapon:
    def __init__(self, 
                 name: str, 
                 weapon_type: str, 
                 damage: int, 
                 value: int
                 ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


nova_sword = Weapon(name = "Nova sword",
                    weapon_type = "sharp",
                    damage = 5,
                    value = 10)

blaster = Weapon(name = "Blaster",
                    weapon_type = "ranged",
                    damage = 4,
                    value = 8)

fists = Weapon(name = "fists",
                    weapon_type = "blunt",
                    damage = 2,
                    value = 0)

class Consumable:
    def __init__(self,
                 name: str,
                 consumable_type: str,
                 damage: int,
                 quantity: int = 1
                 ) -> None:
        self.name = name
        self.consumable_type = consumable_type
        self.damage = damage
        self.quantity = quantity
    
    def use(self, user, target = None):

        if self.quantity <= 0:
            type_out(f"No {self.name}s are left in your inventory!") 

        elif self.consumable_type == "Healing":
            user.health = min(user.health_max, user.health + self.damage)
            type_out(f"({user.name} used a {self.name} and restored {self.damage} health!)\n{user.name} now has {user.health}/{user.health_max} health.")
            #hero.health_bar.update()  redraw hero's health bar when a healing item is used
           # hero.health_bar.draw()

        elif self.consumable_type == "Damaging":
            if target is None:
                type_out("Error: No target specified")
                return
            else:
                target.health -= self.damage
                type_out(f"{user.name} used a {self.name} and dealt {self.damage} to {target.name}!")
                target.health_bar.update()
                target.health_bar.draw()

        self.quantity -= 1
        
        if self.quantity == 0:
            type_out(f"No more {self.name}s are left in your inventory!")

stim_pack = Consumable(name = "Stim Pack",
                       consumable_type = "Healing",
                       damage = 5,
                       quantity = 1)

plasma_grenade = Consumable(name = "Plasma Grenade",
                            consumable_type = "Damaging",
                            damage = 10,
                            quantity = 1)