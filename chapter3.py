import globalvariables
import chapter1
import chapter4
import chapter5
import gameover

def start_chapter():
    print(f"\nChapter {globalvariables.chapter}: The Cafeteria")
    print("The cafeteria is deserted, save for overturned tables and the stench of stale food.")
    print("Shadows move in the corners of your eyes.")

    print("\nWhat would you like to do?")
    print("1. Search for Supplies")
    print("2. Fight the Hostile Patients")
    print("3. Talk to a Group of Survivors")
    print("4. Attempt to Escape through the Back Door")

    choice = input("Choose an action (1-4): ")

    if choice == "1":
        search_for_supplies()
    elif choice == "2":
        fight_hostile_patients()
    elif choice == "3":
        talk_to_survivors()
    elif choice == "4":
        escape_through_back_door()
    else:
        print("Invalid choice. Try again.")
        start_chapter()

def search_for_supplies():
    print("You find food, a weapon, and medical supplies that could prove useful.")
    globalvariables.chapter = 4
    chapter4.start_chapter()

def fight_hostile_patients():
    print("You overwhelm your enemies, but you suffer severe injuries.")
    globalvariables.chapter = 1
    chapter1.start_chapter()

def talk_to_survivors():
    print("You gain allies who can help you escape, providing crucial information.")
    globalvariables.chapter = 5
    chapter5.start_chapter()

def escape_through_back_door():
    print("You are ambushed by a guard and captured.")
    gameover.trigger_game_over()
