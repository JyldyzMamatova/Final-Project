import globalvariables
import chapter2
import chapter3
import gameover

def start_chapter():
    while True:
        print("\nWhat would you like to do?")
        print("1. Explore the Room")
        print("2. Check the Door")
        print("3. Talk to a Fellow Patient")
        print("4. Exit the Room Recklessly")

        choice = input("Choose an action (1-4): ")

        if choice == "1":
            explore_room()
            break
        elif choice == "2":
            check_door()
            break
        elif choice == "3":
            talk_to_patient()
            break
        elif choice == "4":
            reckless_exit()
            break
        else:
            print("Invalid choice. Try again.")


def explore_room():
    globalvariables.player.room_explored = True
    globalvariables.player.note_found = True
    print("You find a hidden note with a hint about a secret passage.")
    globalvariables.chapter = 3
    chapter3.start_chapter()

def check_door():
    globalvariables.player.door_checked = True
    print("The door is unlocked, and you cautiously step into the hallway.")
    globalvariables.chapter = 2
    chapter2.start_chapter()

def talk_to_patient():
    globalvariables.player.ally_met = True
    print("You gain valuable information about the hospital's layout and learn about a potential ally in another wing.")
    globalvariables.chapter = 3
    chapter3.start_chapter()

def reckless_exit():
    globalvariables.player.captured = True
    print("You alert the guards and are captured.")
    gameover.trigger_game_over()
