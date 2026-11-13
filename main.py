# ==============================================================================
# WILLIAM'S TEXT ADVENTURE GAME: The Magic Tower
# Purpose: A text andveture, a branching choice-based text adventure game, with 11 endings.
# Requirements Met: Functions, Variables, Lists/Dictionaries, If/Else Logic, 
#                   Consistent Inputs, Descriptive Comments, Multiple Endings.
# ==============================================================================

# Global variable to store player state
# Utilizing a dictionary to keep track of items the player collects
well_filled = False
water_lever_activated = False
approached_well_before = False

import sys

player_status = {
    "name": "",
    "inventory": []
    
}

Unlocked_Endings = set()

def start_game():
    """Initializes the game, welcomes the player, and routes them to the first room."""
    print("Welcome to Magic Tower The Text Adventure!")
    
    # Prompting the user for their name using standard inputs, if one hasn't already been Entered before.
    if player_status["name"] == "":
        player_status["name"] = input("What is your name? ")
    
    print(f"\nWelcome, {player_status['name']}!")
    print("You wake up in a dimly lit stone courtyard. Tied to a wooden pillar, you can see Two massive doors stand before you.")
    print("Your choices will determine your fate. Type your choices carefully!")
            
    # Send the player to the first choice room
    Bound_in_the_courtyard() 
    
def get_choice(options):
    """
    A helper function to guarantee consistent, clearly explained user inputs.
    It loops until the user enters a valid choice from the provided list.
    """
    print("\nWhat will you do? Options:", options)
    while True:
        choice = input("> ").strip().lower()
        if choice in options:
            return choice
        print("Invalid choice. Please type one of the exact options listed above.")

# ==============================================================================
# PLAY AGAIN FUNCTION
# ==============================================================================

# the endigns are numbered from 0 to 10 in how many items and steps are needed to reach them, at least that is how it should work.
def play_again(ending_name):
    """Asks the player if they want to restart, resets inventory, and stops the current run."""
    Unlocked_Endings.add(ending_name)


    print("\n" + "=" * 50 + "\n")
    print(f"ENDINGS UNLOCKED: {len(Unlocked_Endings)} / 11")
    for ending in sorted(Unlocked_Endings):
        print(f" - {ending}")
    if len(Unlocked_Endings) == 11:
         print("CONGRATULATIONS! You've gotten every ending in The Magic Tower. ")
         print("I hope you have had fun playing this text adventure.")
                
    
    print("\n" + "=" * 50 + "\n")



    choice = get_choice(["play again", "quit"])
    if choice == "play again":
        player_status["inventory"].clear()  # Completely empties the inventory list
        print("\n" + "=" * 50 + "\n")
        start_game()  
    else:
        print("\nThanks for playing The Magic Tower! Goodbye.")
    sys.exit()  # Stops all previous room functions from running

# ==============================================================================
# ROOM FUNCTIONS AND BRANCHING PATHWAYS
# ==============================================================================


def Bound_in_the_courtyard():
    """the Starting Choice"""
    if "Dagger" not in player_status["inventory"]:
        print("\n--- The Sunken Courtyard ---")
        print("You awaken in a sunken courtyard, surrounded by ancient stone walls, and loosely tied to a wooden pillar.")
    else:
        print("with the dagger in hand what now?")

    # Present options based on whether they already have the dagger
    if "Dagger" not in player_status["inventory"]:
        choice = get_choice(["attempt to grab dagger", "wiggle free"])
    else:
        choice = get_choice(["cut the ropes", "wiggle free"])

    if choice == "attempt to grab dagger":
        print("\nYou reach for the dagger in your pocket.")
        print("You manage to grab the handle of the dagger.")
        # Modifying the list/dictionary inventory variable
        player_status["inventory"].append("Dagger")
        Bound_in_the_courtyard()  # Loop back into the room function so they can make their next move

    elif choice == "cut the ropes":
        print("\nYou use the dagger to cut the ropes binding you.")
        print("You are free! You can now explore the courtyard.")
        courtyard() #move to the courtyard function to continue the game

    elif choice == "wiggle free":
        # this can be achieved.
        # the 0 ending, that player are most likly to get first.
        print("\nYou attempt to wiggle free from the ropes.")
        print("But all you manage to do is slip down a bit, and end up with a rope choking you.")
        print("You are unable to breathe, the world goes dark and you parish. Your Journey Ends Before It can begin.")
        # ENDING 0: Ending At the Beginning Ending
        print("\n*** ENDING 0: Ending At the Beginning (DEFEAT)***")
        play_again("ENDING 0: Ending At the Beginning (DEFEAT)")


def courtyard():
    times_key_Thrown_in_well = 0
    """The starting area. Branches into two main paths: Left or Right."""
    print("To your left, a heavy wooden door creaks in the wind.")
    print("To your right, a iron-reinforced door glows with a faint green light.")
    print("In front of you, a deep well sits in the center of the courtyard, its depths shrouded in darkness.")
    
    # Getting a validated input from the user
    choice = get_choice(["left", "right", "approach well", "spawn item(debug)"])
    
    # If/Else logic handling the primary branching paths
    if choice == "left":
        wooden_room()

    elif choice == "right":
        iron_room()

    # the Debug helps to test all ending functions, and is staying here for repeat playthroughs to help get the other endings.
    elif choice == "spawn item(debug)":
        print("\nDebug: You have chosen to spawn an item. This is a debug feature.")
        print("You can choose to spawn a 'Dagger', 'gold key', 'rusty key', 'silver key', 'ebony key', 'Vial', 'Crank handle', or 'Ancient Grimoire'.")
        item_to_spawn = input("Which item would you like to spawn? ").strip()
        if item_to_spawn in ["Dagger", "gold key", "rusty key", "silver key", "ebony key", "Vial", "Crank handle", "Ancient Grimoire"]:
            player_status["inventory"].append(item_to_spawn)
            print(f"\nDebug: {item_to_spawn} has been added to your inventory.")
        else:
            print("\nDebug: Invalid item. No item has been spawned.")
        courtyard()  # Loop back into the courtyard function so they can make their next move

    elif choice == "approach well":
        # this is the choice to get the 1st and 9th endings, along with getting items required for the other endings
        while True:
            if "well_filled" in player_status["inventory"]:
                if "approached well" not in player_status["inventory"]:
                    print("\nYou approach the well and peer into its depths. You can see water shimmering at the bottom.")
                elif "approached well" in player_status["inventory"]:
                    print("\nYou approach the well and peer into its depths. You can see water shimmering at the bottom.")
                    print("The magical power that came from within the well before is now gone, what do you do?")

            else:  
                print("\nYou approach the well and peer into its depths. It's dark and you can't see the bottom, or if there even is any water inside.")
                print("But you can sense a magical power from within the well, what do you do?")
                player_status["inventory"].append("approached well")


            choice = get_choice(["jump in", "drop stone in", "throw item in", "go back"])

            if choice == "jump in":
                if "well_filled" in player_status["inventory"]:
                    # this can be achieved.
                    # the 9th ending, requires all the rusty key, the silver key, and the crank handle along with pulling the lever to get.
                    print("\nYou take a deep breath and jump into the well. The water is freezing cold, but you manage to swim down.")
                    print("At the bottom, you find a hidden passage leading to a secret cave filled with treasure!")
                    print("The cave is so large and vast that you can't see where the treasure ends!")
                    # ENDING 9: The Hidden Treasure Ending
                    print("\n*** ENDING 9: The Hidden Treasure (VICTORY) ***")
                    play_again("ENDING 9: The Hidden Treasure (VICTORY)")
                else: 
                    # this can be achieved.
                    # the 1st ending achieved after cutting yourself free.
                    print("you jump into the well, you fall, all of a sudden you feel strange.") 
                    print("Your body shifts in to something else and you die, you are lost forever without knowing what you became.")
                    # ENDING 1: The Unknown Transformation Ending
                    print("\n*** ENDING 1: The Unknown Transformation (DEFEAT) ***")
                    play_again("ENDING 1: The Unknown Transformation (DEFEAT)")

            elif choice == "drop stone in":
                print("\nYou drop a stone into the well. after a awhile a pile of fine sand gains flies up out of the well and land on the other side.")
                 
            elif choice == "go back":
                courtyard()
                break  # Exit the loop and return to the courtyard

            elif choice == "throw item in":
                
                while True:
                    
                    if "gold key" in player_status["inventory"]:
                        choice = get_choice(["dagger", "gold key", "go back"])
                    elif "rusty key" in player_status["inventory"]:
                        choice = get_choice(["dagger", "rusty key", "go back"])
                    elif "silver key" in player_status["inventory"]:
                        choice = get_choice(["dagger", "silver key", "go back"])
                    elif "gold key" not in player_status["inventory"] and "rusty key" not in player_status["inventory"] and "silver key" not in player_status["inventory"]:
                        choice = get_choice(["dagger", "go back"])
        
                    if choice == "dagger":
                                    if "Dagger" in player_status["inventory"]:
                                        print("\nYou throw the dagger into the well. A sword flies out, and lands on the other side, You pick it up.")
                                        player_status["inventory"].remove("Dagger")
                                        player_status["inventory"].append("Sword")
                                    else:
                                        print("\nYou don't have a dagger to throw into the well.")

                    elif times_key_Thrown_in_well >= 3 and choice in ["gold key", "rusty key", "silver key"]:
                                                        print("\nYou throw the key into the well. A different key flies out, and lands on the other side.")
                                                        print("A key You've never seen before, made of a dark ebony material, You pick it up.")
                                                        print("The key is heavy and cold to the touch, and you can feel a strange energy emanating from it.")
                                                        player_status["inventory"].remove(choice)
                                                        player_status["inventory"].append("ebony key")

                    elif choice == "gold key":
                                    print("\nYou throw the gold key into the well. A silver key flies out, and lands on the other side, You pick it up.")
                                    player_status["inventory"].remove("gold key")
                                    player_status["inventory"].append("silver key")
                                    times_key_Thrown_in_well += 1
                
                    elif choice == "silver key":
                                    print("\nYou throw the silver key into the well. A rusty key flies out, and lands on the other side, You pick it up.")
                                    player_status["inventory"].remove("silver key")
                                    player_status["inventory"].append("rusty key")
                                    times_key_Thrown_in_well += 1
                
                    elif choice == "rusty key":
                                    print("\nYou throw the rusty key into the well. A gold key flies out, and lands on the other side, You pick it up.")
                                    player_status["inventory"].remove("rusty key")
                                    player_status["inventory"].append("gold key")
                                    times_key_Thrown_in_well +=1
                
                    elif choice == "go back":
                                    break  # Exit the loop and return to the courtyard
  

def wooden_room():
    """The left pathway. Introduces items/inventory and splits into multiple endings."""
    print("\n--- The Armory ---")
    print("You enter a dusty room filled with rusted armor. On a pedestal sits A shiny gold key and A rusty key.")
    print("Ahead of you lies a dark staircase leading down.")

   
    # Present options based on whether they already have the Gold key
    if "gold key" not in player_status["inventory"] or "rusty key" not in player_status["inventory"]:
        choice = get_choice(["approach keys", "descend", "go back"])
    else:
        choice = get_choice(["descend", "go back"])
        
    if choice == "approach keys":
        if "gold key" in player_status["inventory"] or "rusty key" in player_status["inventory"] or "silver key" in player_status["inventory"] or "ebony key" in player_status["inventory"]:
            print("\nYou have already taken a key from the pedestal, and the other disappeared.")
            wooden_room()
        print("You Approach the pedastal with the keys. You see a shiny gold key, and a dull rusty key. Which do you garb?")
        choice = get_choice(["gold key", "rusty key", "go back"])

        if choice == "gold key":
            print("\nYou picked up the gold key! It feels heavy in your pocket.")
            print("As you picked up the gold key, you noticed the rusty key had disappered.")
            # Modifying the list/dictionary inventory variable
            player_status["inventory"].append("gold key")
            # Loop back into the room function so they can make their next move
            wooden_room()
        elif choice == "rusty key":
            
            print("\nYou picked up the rusty key! It feels light in your pocket.")
            print("As you picked up the rusty key, you noticed the gold key had disappered.")
            # Modifying the list/dictionary inventory variable
            player_status["inventory"].append("rusty key")
            # Loop back into the room function so they can make their next move
            wooden_room()
        elif choice == "go back":
            print("\nYou step away from the pedistal, hesitan to make a choice ")
            wooden_room()

    elif choice == "descend":
        dungeon_room()

    elif choice == "go back":
        courtyard()


def dungeon_room():
    """Deep in the left pathway. Contains the 5th Ending and 6th Ending based on inventory."""
    print("\n--- The Deep Dungeon ---")
    print("At the bottom of the stairs there is a dimly lit dungeon. The air is damp and musty.")
    print("in the corner of the room there sits a small round table with a empty vial on top.")
    print("on the wall next to the door is an old rotting wooden crank wheel, missing its handle.")
    print("on the far wall is a massive chest wrapped in heavy chains with a golden lock.")
    print("It requires a key to open.")

# Present options based on whether they already have the Vial.
    if "Vial" not in player_status["inventory"]:
        choice = get_choice(["take vial", "approach crank wheel", "open chest", "go back"])
    else:
        choice = get_choice(["approach crank wheel", "open chest", "go back"])


    if choice == "take vial":
        print("\nYou pick up the empty vial. It might be useful later.")
        player_status["inventory"].append("Vial")
        dungeon_room()


    elif choice == "approach crank wheel":
        print("\nYou approach the crank wheel. It is missing its handle, Without the handle it won't function.")
        if "Crank handle" in player_status["inventory"]:
            # Required to get the 9th ending.
            if "water_lever_activated" in player_status["inventory"]:
                print("You insert the crank handle into the wheel and turn it.")
                print("The wheel creaks and the sound of water rushing can be heard behind the wall.")
                player_status["inventory"].append("well_filled")
            else:
                print("You insert the crank handle into the wheel and turn it.")
                print("The wheel creaks, but nothing happens. Perhaps you need to activate the water flow first.")
        dungeon_room()            

    
    
    elif choice == "open chest":
        # Checking conditional requirements (earned vs unearned state)
        if "gold key" in player_status["inventory"]:
            # this can be achieved.
            # the 6th ending that can be achieved after aqquiring the gold key from the preivious room, and opening the chest.
            print("\nYou insert the gold key into the lock. It turns with a satisfying click!")
            print("The chest explodes with brilliant white light, showering you in ancient treasure and vast riches.")
            # ENDING 6: The Wealthy Explorer Ending
            print("\n*** ENDING 6: The Wealthy Explorer (VICTORY) ***")
            play_again("ENDING 6: The Wealthy Explorer (VICTORY)")

        else:
            # this can be achieved.
            # the 5th ending, you'll get this ending if you try to open the chest with out the gold key.
            print("\nYou try to force the chest open, but a magical trap triggers!")
            print("Spikes shoot out from the walls. You did not prepare adequately.")
            # ENDING 5: Trapped in the Darkness Ending
            print("\n*** ENDING 5: Trapped in the Dark (DEFEAT) ***")
            play_again("ENDING 5: Trapped in the Dark (DEFEAT)")

    elif choice == "go back":
        wooden_room()


def iron_room():
    """The right pathway. Splits into four distinct pathways and lots of endings."""
    print("\n--- The Laboratory ---")
    print("A wizard's lab! A bubbling cauldron sits in the center.")
    print("To the side, An old wooden door with a small mat out front.")
    print("To the other side, a sleeping dragon rests on a pile of ancient scrolls.")
    print("A glowing portal stands wide open at the back of the room.")
    
    choice = get_choice(["drink from the cauldron", "approach the door", "wake the dragon", "enter the portal", "go back"])
    
    if choice == "drink from the cauldron":
        if "Vial" in player_status["inventory"]:
            if "Ancient Grimoire" in player_status["inventory"]:
                if "ebony key" in player_status["inventory"]:
                    # this can be achieved.
                    # the 10th ending, and the hardest one to achieve, it requires the rusty key, silver key, Ancient Grimoire, 
                    # Vial, and the Ebony key.
                    print("\nYou scoop up a small vial worth of the bubbling green liquid and drink it.")
                    print("Your body begins to feel like it's burning from the inside, your magic capacity increases.")
                    print("you gain the magical abilities of a master wizard.")
                    print("You open the Ancient Grimoire and begin to study the ancient spells and magic within.")
                    print("You have become a master wizard who can weild ancient magic.")
                    print("You use the ebony key along with a special spell within the grimoire to unlock a hidden World only you can open the way too.")
                    print("You have become a master wizard who can weild ancient magic, known as the Master of ancient Magic from another world.")
                    # Ending 10 : The Master of Ancient Magic from another World Ending
                    print("\n*** ENDING 10: The Master of Ancient Magic from another World (VICTORY) ***")
                    play_again("ENDING 10: The Master of Ancient Magic from another World (VICTORY)")

                else:
                    # this can be achieved.
                    # the 8th ending, requires the Vial, Rusty key, Silver key, and Ancient Grimoire
                    print("\nYou scoop up a small vial worth of the bubbling green liquid and drink it.")
                    print("Your body begins to feel like it's burning from the inside, your magic capacity increases.")
                    print("you gain the magical abilities of a master wizard.")
                    print("You open the Ancient Grimoire and begin to study the ancient spells and magic within.")
                    print("You have become a master wizard who can weild ancient magic, you're known as the Master of ancient Magic.")
                    # Ending 8: Master of ancient Magic Ending
                    print("\n*** ENDING 8: The Master of Ancient Magic (VICTORY) ***")
                    play_again("ENDING 8: The Master of Ancient Magic (VICTORY)")

            else:
                # this can be achieved.
                # The 7th Ending, All thats needed is the Vial to get this one.
                print("\nYou scoop up a small vial worth of the bubbling green liquid and drink it.")
                print("Your body begins to feel like it's burning from the inside, your magic capacity increases.")
                print("you gain the magical abilities of a master wizard.")
                # ENDING 7: Master of Magic Ending
                print("\n*** ENDING 7: The New Master of Magic (VICTORY) ***")
                play_again("ENDING 7: The New Master of Magic (VICTORY)")

        else:
            # this can be achieved.
            # the 2nd ending, if you try to drink from the cauldron without the vial.
            print("\nYou attempt to drink from the cauldron without a vial. The liquid is too hot and burns your hand.")
            print("You collapse to the floor, as the overwhelming magical power corses throughout your body, unable to withstand the magical backlash.")
            # ENDING 2: Too Hot To Handle Ending
            print("\n*** ENDING 2: Too Hot To Handle (DEFEAT) ***")
            play_again("ENDING 2: Too Hot To Handle (DEFEAT)")


    elif choice == "approach the door":
        if "rusty key" in player_status["inventory"] or "unlocked bedroom" in player_status["inventory"]:
            print("\nYou use the rusty key to unlock the door. Inside, you find what appears to be a small bed room.")
            player_status["inventory"].append("unlocked bedroom")
            bedroom()
             
        else:
            print("\nYou grab the door knob, The door is locked. You need a key to open it.")
            iron_room()
                
    elif choice == "wake the dragon":
        # this can be achieved.
        # the 3rd ending, if the mess with the dragon you get burnt.
        print("\nYou approach the beast and shake its wing. It opens one massive, fiery eye.")
        print("Annoyed by your interruption, it sneezes a blast of fire, reducing you to ash.")
        # ENDING 3: The Charred and Crispy Adventurer Ending
        print("\n*** ENDING 3: Charred and Crispy Adventurer (DEFEAT) ***")
        play_again("ENDING 3: Charred and Crispy Adventurer (DEFEAT)")
        
    elif choice == "enter the portal":
        # this can be achieved.
        # the 4th ending, the easiest victory ending to achieve with out items.
        print("\nYou step through the swirling vortex. The world spins rapidly.")
        print("You open your eyes and realize you've been teleported right back outside of your own house.")
        # ENDING 4: Escape to Home Ending
        print("\n*** ENDING 4: There's No Place Like Home (ESCAPED) ***")
        play_again("ENDING 4: There's No Place Like Home (ESCAPED)")

    elif choice == "go back":
        courtyard()


def bedroom():
    print("the only things of note in the room are a dusty locked cabinet, and a lever on the wall, with the label 'Primary water flow'.")

    choice = get_choice(["approach cabinet", "pull lever", "go back"])

    if choice == "approach cabinet":
        if "silver key" in player_status["inventory"]:
            print("\nYou use the silver key to unlock the cabinet. Inside, you find a small crank handle, and a grimoire of ancient spells and magic.")
            print("You take the crank handle and ancient grimoire and add them to your inventory.")
            player_status["inventory"].append("Crank handle")
            player_status["inventory"].append("Ancient Grimoire")
            bedroom()
            
        else:
            print("\nThe cabinet is locked. You need a key to open it.")
            bedroom()
            
    elif choice == "pull lever":
            print("\nYou pull the lever, and hear the sound of water rushing behind the wall.")
            player_status["inventory"].append("water_lever_activated")
            bedroom()

    elif choice == "go back":
            iron_room()
            

# ==============================================================================
# MAIN PROGRAM EXECUTION
# ==============================================================================
# This triggers the start of the program when run in Python
if __name__ == "__main__":
    start_game()