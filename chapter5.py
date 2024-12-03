import globalvariables
import chapter1
import chapter4
import gameover

def start_chapter():
    print(f"\nChapter {globalvariables.chapter}: The Escape")
    print("The exit looms ahead, tantalizingly close. The final barrier between you and freedom.")

    print("\nWhat would you like to do?")
    print("1. Confront the Guards")
    print("2. Use the Secret Passage")
    print("3. Distract and Flee")
    print("4. Find an Alternate Route")

    choice = input("Choose an action (1-4): ")

    if choice == "1":
        confront_guards()
    elif choice == "2":
        use_secret_passage()
    elif choice == "3":
        distract_and_flee()
    elif choice == "4":
        find_alternate_route()
    else:
        print("Invalid choice. Try again.")
        start_chapter()

import random

def confront_guards():
    print("You engage in a fierce battle with the guards.")
    if globalvariables.player.weapon_found:  # Check if the player has a weapon
        success_chance = 75  # Higher success rate with a weapon
    else:
        success_chance = 50  # Lower success rate without a weapon

    if random.randint(1, 100) <= success_chance:
        print("You defeated the guards and gained your freedom!")
        print("Ending: Freedom")
        exit()
    else:
        print("You were overpowered by the guards.")
        gameover.trigger_game_over()


def use_secret_passage():
    print("You navigate the dark, narrow passage.")
    hazards = random.choice([
        "A collapsing wall nearly crushes you, but you escape just in time.",
        "You encounter a deadly trap but manage to disable it.",
        "The passage is clear, and you reach freedom unharmed."
    ])
    print(hazards)

    if "trap" in hazards:
        print("You are injured but make it out alive.")
    print("Ending: Freedom")
    exit()


def distract_and_flee():
    print("You need to create a distraction. What will you use?")
    print("1. Set off the fire alarm")
    print("2. Throw a heavy object to create noise")
    print("3. Tamper with the power grid")

    choice = input("Choose your distraction method (1-3): ")

    if choice == "1":
        print("The fire alarm causes chaos, allowing you to slip through unnoticed.")
    elif choice == "2":
        print("The noise attracts the guards, but you manage to evade them.")
    elif choice == "3":
        print("Tampering with the power grid plunges the area into darkness, aiding your escape.")
    else:
        print("Invalid choice. The guards catch you.")
        gameover.trigger_game_over()
    
    print("Ending: Freedom")
    exit()


def find_alternate_route():
    if globalvariables.player.map_found:
        print("Using the map, you navigate a hidden path that bypasses the guards.")
        print("Ending: Freedom")
        exit()
    else:
        print("Without a map, you wander aimlessly and get caught.")
        gameover.trigger_game_over()

def display_ending(ending_type):
    if ending_type == "Hero":
        print("You fought bravely and claimed your freedom!")
    elif ending_type == "Strategist":
        print("Your cunning and resourcefulness led you to freedom.")
    elif ending_type == "Survivor":
        print("You barely escaped, battered but alive.")
    print("The end. Thank you for playing!")
    exit()

