from character import Character, Enemy, Drone
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
                    
                    if choice == 1: #attack with equipped weapon DONE
                        hero.attack(enemy)
                        enemy.health_bar.update()
                        enemy.health_bar.draw()
                        if enemy.health <= 0:
                            return("hero_win")
                        action_taken = True
                    elif choice == 2: #defend NOT DONE
                        action_taken = True
                        pass
                    elif choice == 3: #use item DONE
                    
                        def use_consumable(hero, enemy):
                            consumables = hero.inventory.consumables
                            if not consumables:
                                type_out("You have no consumables!")
                                return False  # nothing used

                            while True:
                                hero.inventory.view_consumables_for_use()
                                try:
                                    choice = int(input("Choose a consumable to use: "))
                                    if 1 <= choice <= len(consumables):
                                        selected_item = consumables[choice - 1]
                                        break
                                    else:
                                        type_out(f"Enter a number between 1 and {len(consumables)}")
                                except ValueError:
                                    type_out("Invalid input. Enter a number.")

                            # Use the item
                            if selected_item.consumable_type.lower() == "healing":
                                selected_item.use(hero)
                            elif selected_item.consumable_type.lower() == "damaging":
                                selected_item.use(hero, enemy)

                            # Decrement quantity and remove if zero
                            
                            if selected_item.quantity <= 0:
                                type_out(f"You have no {selected_item.name}s left!")
                                hero.inventory.consumables.remove(selected_item)

                            return True  # item successfully used 


                        action_taken = use_consumable(hero, enemy)
                        if not action_taken:
                            continue      
                    elif choice == 4: #swap weapon  DONE
                        hero.inventory.view_weapons_for_use()
                        if not hero.inventory.view_weapons:
                            type_out("You have no weapons!")
                            continue
                        
                        while True:
                            try:
                                weapon_choice = int(input(""))
                                if 1<= weapon_choice <= len(hero.inventory.weapons):
                                    break
                                else:
                                    type_out(f"Enter a number between 1 and {len.hero.inventory.weapons}")
                            except ValueError:
                                type_out("Invald input. Please enter a number.")

                        chosen_weapon = hero.inventory.weapons[weapon_choice - 1]
                        hero.equip(chosen_weapon)

                        action_taken = True
                        pass
                    elif choice == 5: #view inventory DONE
                        hero.inventory.view_inventory()
                        type_out("Press any key to return to combat")
                        input("")
                        continue
                    elif choice == 6: #retreat DONE
                        return("retreated")
                
     
            else:
                
                enemy.attack(hero)
                hero.health_bar.update()
                hero.health_bar.draw()
                if hero.health <= 0:
                    return("hero_lose")
                    
        