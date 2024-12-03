import globalvariables
import chapter3
import chapter5
import gameover

def start_chapter():
    print(f"\nChapter {globalvariables.chapter}: The Laboratory")
    print("The sterile, cold atmosphere of the laboratory contrasts sharply with the chaos outside.")
    print("The air is thick with chemical fumes.")

    print("\nWhat would you like to do?")
    print("1. Search for Documents")
    print("2. Disable Security Systems")
    print("3. Confront the Professor")
    print("4. Unlock the Main Door")

    choice = input("Choose an action (1-4): ")

    if choice == "1":
        search_for_documents()
    elif choice == "2":
        disable_security_systems()
    elif choice == "3":
        confront_professor()
    elif choice == "4":
        unlock_main_door()
    else:
        print("Invalid choice. Try again.")
        start_chapter()

import random

def search_for_documents():
    outcomes = [
        "You uncover evidence of illegal experiments, finding a clue to escape.",
        "You find a journal detailing gruesome test subjects but no clear way out.",
        "You stumble upon encrypted data, requiring a code you don’t yet have."
    ]
    print(random.choice(outcomes))
    globalvariables.chapter = 5
    chapter5.start_chapter()


def disable_security_systems():
    if globalvariables.player.ally_met:
        print("Your ally helps you disable the systems quickly and quietly.")
        globalvariables.chapter = 5
        chapter5.start_chapter()
    else:
        print("You struggle alone, accidentally triggering an alarm.")
        gameover.trigger_game_over()


def confront_professor():
    print("You confront the professor, who seems unfazed by your presence.")
    print("1. Demand answers about the experiments.")
    print("2. Threaten the professor with a weapon.")
    print("3. Search the room while keeping an eye on the professor.")

    choice = input("Choose an action (1-3): ")

    if choice == "1":
        print("The professor admits to the experiments but stalls for time. Guards arrive, and you are captured.")
        gameover.trigger_game_over()
    elif choice == "2":
        print("The professor reveals crucial information in fear, but you still hear guards approaching.")
        globalvariables.chapter = 5
        chapter5.start_chapter()
    elif choice == "3":
        print("You find a hidden keycard before the professor escapes, allowing you to proceed.")
        globalvariables.chapter = 5
        chapter5.start_chapter()
    else:
        print("Invalid choice.")
        confront_professor()


def unlock_main_door():
    attempts = 3
    while attempts > 0:
        print(f"You have {attempts} attempts left to unlock the door.")
        code = input("Enter the 4-digit code: ")
        if code == "4321":  # Example code
            print("You successfully unlock the door without triggering alarms.")
            globalvariables.chapter = 5
            chapter5.start_chapter()
            return
        else:
            print("Incorrect code.")
            attempts -= 1

    print("You’ve failed to unlock the door, and the alarm sounds.")
    gameover.trigger_game_over()
