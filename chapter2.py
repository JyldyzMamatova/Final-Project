import globalvariables
import chapter1
import chapter3
import chapter4
import gameover


def start_chapter():
    print(f"\nChapter {globalvariables.chapter}: The Hallway")
    print("The hallway stretches endlessly, filled with unsettling whispers and flickering lights.")
    print("You feel the cold gaze of cameras on you.")

    print("\nWhat would you like to do?")
    print("1. Open Random Doors")
    print("2. Search for Clues")
    print("3. Hide from Guards")
    print("4. Proceed to the Cafeteria")

    choice = input("Choose an action (1-4): ")

    if choice == "1":
        open_random_doors()
    elif choice == "2":
        search_for_clues()
    elif choice == "3":
        hide_from_guards()
    elif choice == "4":
        proceed_to_cafeteria()
    else:
        print("Invalid choice. Try again.")
        start_chapter()


def open_random_doors():
    print("You stumble into a dangerous room filled with hostile patients.")
    gameover.trigger_game_over()

def search_for_clues():
    print("You find a map showing a hidden exit in the basement.")
    globalvariables.chapter = 4
    chapter4.start_chapter()

def hide_from_guards():
    print("You successfully evade the guards but end up back where you started.")
    globalvariables.chapter = 1
    chapter1.start_chapter()

def proceed_to_cafeteria():
    print("You make your way to the cafeteria, seeking supplies and allies.")
    globalvariables.chapter = 3
    chapter3.start_chapter()
