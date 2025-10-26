import os
import sys
import time 
from type_out import type_out
from combat import combat
from character import Hero, Enemy, Drone
from inventory import Inventory
from weapon import blaster, nova_sword, plasma_grenade, stim_pack

while True:
    os.system("cls")

    #type_out("The year is 2749, and humanity has moved into the stars.")
    #type_out("We've settled our differences and no longer wage wars against one another,")
    #type_out("but, we didn't do it for the right reasons.")
    #type_out("After the first intergalactic war, we faced a new threat:")
    #type_out("Hyperintelligent aliens and supersentient AI.")
    #type_out("To prepare humanity for this new threat, our governments designed a learning lab to fight these unknown enemies:")
    #type_out("\n\nNEON HUB.\n\n")
    #type_out("In the hub, cadets are placed in a simulated battle environment,\nallowing them to train to handle ever-evolving threat vectors,")
    #type_out("while facing no threats themselves.")
    #type_out("Welcome to \n\n\n\n\n\n          NEON\n          FRONTIER\n\n\n\n\n")

    type_out("What is your name?")
    player_name = input("")
    print("\n\n")

    hero = Hero(name = player_name, health = 100, speed = 50) 
    
    player_status = "in_hub"
    while player_status == "in_hub":
        type_out(f"""Hello {player_name}, welcome to the Neon Hub battle simulator.\n\n[1]: Enter combat simulation\n[2]: View stats and inventory\n[3]: Enter shop\n[4]: Upgrade stats\n[5]: Challenge boss\n\n\n""")
    
        choice = input("")
        print("")
        while choice not in ["1", "2", "3", "4", "5"]:
            type_out("Invalid input. Please enter a valid input.")
            choice = ("")
            
        if choice == "1":

           
            

            enemy = Drone()

            player_status = "in_combat"
            combat_result = combat(hero, enemy)

            if combat_result == "hero_win":
                type_out("You win!\nYou were awarded x credits.\n\n\n\n")
                player_status = "in_hub"
            elif combat_result == "hero_lose":
                type_out("You lose!\nYou lost x credits.\n\n\n\n")
                player_status = "in_hub"
            elif combat_result == "retreated":
                type_out("You retreated from the battle!\nYou lost x credits.\nYou lost x experience.\n\n\n\n")
                player_status = "in_hub"
                pass
            
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass

    

   
    input()
