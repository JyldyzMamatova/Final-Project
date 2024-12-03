import time
import globalvariables
import chapter1
import gameover

def main():
    globalvariables.player.name = input("You wake up in a dimly lit hospital room. What is your name? ")
    chapter1.start_chapter()

if __name__ == "__main__":
    main()
