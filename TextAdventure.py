#I'm going to attempt to make a room, roaming kind of thing.
#Ex. Person can choose to turn left, right, go through the attic, etc etc
#Plus I'll add actions you can do along with people you can interact with.
import time
choice = ""
failsafe = 0
class Room:
    def __init__(self, name, description, hasChest, hasNPC):
        self.name = name
        self. description = description
        self.hasChest = hasChest
        self.hasNPC = hasNPC
        self.npc = None
        self.connections = {}

    def connect(self, direction, room):
        self.connections[direction] = room

    def getNPC(self):
        if self.hasNPC == False:
            print("You are alone.")

        elif self.hasNPC and self.npc is not None:
            return("You see " + self.npc.description + ". " + self.npc.name + ".")

    def getConnections(self):

        if not self.connections:
            return("There is no exit here.")

        directions = ', '.join(self.connections.keys()) #This is cool, but I still have no idea how the keys() part works.
        return "Options are : " + directions

    def describe(self):
        return("You walk into " + self.description + ".")

#-----------------------------------------------------------------------------

class NPC:
    def __init__(self, name, description):
        self.name = name
        self.description = description

#-----------------------------------------------------------------------------

class Game:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.current_room = self.rooms["Bedroom"] #You start in the bedroom.


    def create_rooms(self):
        Bedroom = Room("Bedroom", "a small wooden room with a dirty mattress against the back wall. There are two windows, but they're too dusty to see out of", True, False)
        Bathroom = Room("Bathroom", "a dirty bathroom with cracked tiles on the floors and walls. There is a bathtub on your right. There is a sink that has a broken mirror above it", True, False)
        Closet = Room("Closet", "a lone closet sitting in the house. It's pretty dark inside, though you can smell the weird odor more prominently in here", True, True)
        Hallway = Room("Hallway", "a long, hallway. The wallpaper is clearly damp and decaying. There is an odd odor along with it", False, True)

        ghost = NPC("Ghost", "a small, white phantom. Transparent. They seem more friendly than aggressive")

        Closet.npc = ghost
        #-----------------------------------------------------------------------------

        Bedroom.connect("Exit",Hallway) #You can only exit the Bedroom
    
        Bathroom.connect("Exit", Hallway) #You can only exit the Bathroom

        Closet.connect("Exit",Hallway) #You can only exit the closet

        Hallway.connect("Bathroom", Bathroom) #Hallway can take you to Bathroom
        Hallway.connect("Bedroom", Bedroom) #Hallway can take you to Bedroom
        Hallway.connect("Closet", Closet) #Hallway can take you to closet

        return {
                    "Bedroom": Bedroom,
                    "Bathroom": Bathroom,
                    "Closet": Closet,
                    "Hallway": Hallway
               }
        #-----------------------------------------------------------------------------

    def move(self, direction):
        # Check if the current room has a connection in the given direction
        if direction in self.current_room.connections:
            # Move to the new room
            self.current_room = self.current_room.connections[direction]
            print(self.current_room.describe())
            if self.current_room.getNPC() != None:
                print("---------------------------" + "\n" + self.current_room.getNPC())  # Show the NPC in the room if present
        elif direction == "End":
            print("Process aborted.")
        else:
            print("You can't go that way!")

game = Game()
print(game.current_room.describe())

while choice != "End" and failsafe != 10:
    print("What would you like to do?")
    print(str(game.current_room.getConnections()))
    choice = input("Enter choice : ")

    game.move(choice)

    failsafe = failsafe + 1


