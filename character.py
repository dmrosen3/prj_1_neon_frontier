from weapon import fists, blaster, nova_sword, Consumable, plasma_grenade, stim_pack
from health_bar import HealthBar
from type_out import type_out
from inventory import Inventory

class Character:
    def __init__(self,
                  name: str, 
                  health: int,
                  speed: int,
                  ) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.speed = speed
        self.inventory = Inventory()
        self.weapon = None

    def equip (self, weapon) -> None:
        self.weapon = weapon
        type_out(f"{self.name} equipped a(n) {self.weapon.name}!")


    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        type_out(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with a(n) {self.weapon.name}")

class Hero(Character):
    def __init__(self, 
                 name: str, 
                 health: int, 
                 speed: int,
                 ) -> None:
        super().__init__(name=name, health=health, speed=speed)
        self.inventory = Inventory()

        self.inventory.add_item(nova_sword)
        self.inventory.add_item(fists)
        self.weapon = self.inventory.weapons[0]
        self.health_bar = HealthBar(self, color="green")
        self.inventory = Inventory()
        

class Enemy(Character):
    def __init__(self, 
                 name: str, 
                 health: int, 
                 speed: int
                 ) -> None:
        # Call parent constructor with the expected parameters
        super().__init__(name=name, health=health, speed=speed)
        self.health_bar = HealthBar(self, color="red")

class Drone(Enemy):
    def __init__(self,
                 name: str = "Drone",
                 health: int = 50,
                 speed: int = 75
                 ) -> None:
        super().__init__(name=name, health=health, speed=speed)
        self.weapon = blaster
