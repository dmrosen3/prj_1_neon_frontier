from character import Character, Hero, Enemy, Drone
from type_out import type_out
from inventory import Inventory
from weapon import Consumable

def combat(hero, enemy):
    while hero.health > 0 and enemy.health > 0:
        combat_order = []
        if hero.speed > enemy.speed:
            combat_order.append(hero)
            combat_order.append(enemy)
        else:
            combat_order.append(enemy)
            combat_order.append(hero)
        for character in combat_order:
            if character == hero:
                action_taken = False
                while action_taken == False:
                    type_out(f"Choose an action:\n\n[1]: Attack with equipped weapon\n[2]: Defend\n[3]: Use item\n[4]: Swap weapon\n[5]: View inventory\n[6]: Retreat\n\n\n")

                    try:
                        choice = int(input(""))
                    except ValueError:
                        type_out("Invalid input. Enter a number 1–6.")
                        continue
                    
                    if choice == 1:
                        hero.attack(enemy)
                        enemy.health_bar.update()
                        enemy.health_bar.draw()
                        if enemy.health <= 0:
                            return("hero_win")
                        action_taken = True
                    elif choice == 2:
                        action_taken = True
                        pass
                    elif choice == 3:
                        
                        consumables = hero.inventory.consumables
                        if not consumables:
                            type_out("You have no consumables!")
                        else:
                            while True:
                                hero.inventory.view_consumables_for_use()
                                try:
                                    choice = int(input("Choose a consumable to use: "))
                                    if 1 <= choice <= len(consumables):
                                        break
                                    else:
                                        type_out(f"Enter a number between 1 and {len(consumables)}")
                                except ValueError:
                                    type_out("Invalid input. Enter a number.")

                        selected_item = consumables[choice - 1]

                        if selected_item.quantity == 0:
                            type_out(f"You have no {selected_item}s left!")
                            continue

                        if selected_item.consumable_type.lower() == "healing":
                            selected_item.use(hero)
                        elif selected_item.consumable_type.lower() == "damaging":
                            selected_item.use(hero, enemy)
                       

                        action_taken = True



                        
                    elif choice == 4:
                        action_taken = True
                        pass
                    elif choice == 5:
                        hero.inventory.view_inventory()
                        type_out("Press any key to return to combat")
                        input("")
                        continue
                    elif choice == 6:
                        return("retreated")
                
     
            else:
                
                enemy.attack(hero)
                hero.health_bar.update()
                hero.health_bar.draw()
                if hero.health <= 0:
                    return("hero_lose")
                    
        