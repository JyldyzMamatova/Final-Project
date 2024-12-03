class Player:
    def __init__(self):
        self.name = ""
        self.room_explored = False
        self.door_checked = False
        self.note_found = False
        self.ally_met = False
        self.captured = False

global player
global chapter

player = Player()
chapter = 1
