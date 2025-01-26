# I've added  .strip() method to the input() function to remove any leading or trailing whitespaces from the user's input. This will help in making the input case-insensitive.

print("You wake up in an abandoned mansion in the middle of the desert. The air is dusty, the windows are boarded up, and you hear faint creaking noises.")
print("What do you do?")
print("Options: EXPLORE, SEARCH, SHOUT")

choice1 = input("Your choice: ").strip().upper()

if choice1 == "EXPLORE":
    print("\nYou decide to explore the mansion. It's dark and the air feels heavy.")
    print("Where do you go?")
    print("Options: CHECK KITCHEN, CHECK BASEMENT, CHECK ATTIC")
    choice2 = input("Your choice: ").strip().upper()
    
    if choice2 == "CHECK KITCHEN":
        print("\nYou enter the kitchen and find a strange note on the table. It says, 'Beware the shadows.'")
        print("What do you do?")
        print("Options: READ NOTE, IGNORE NOTE")
        choice3 = input("Your choice: ").strip().upper() 
        
        if choice3 == "READ NOTE":
            print("The note reveals a secret door in the kitchen. You find a way out and escape into the desert. You win!")
        elif choice3 == "IGNORE NOTE":
            print("Ignoring the note, you hear footsteps behind you. The shadows consume you. Game over.")
        else:
            print("Invalid choice. Please restart.")
    
    elif choice2 == "CHECK BASEMENT":
        print("\nYou find a staircase leading to the basement. It's dark and cold.")
        print("What do you do?")
        print("Options: ENTER BASEMENT, TURN BACK")
        choice3 = input("Your choice: ").strip().upper()
        
        if choice3 == "ENTER BASEMENT":
            print("You find a hidden tunnel leading out of the mansion. You escape into the desert. You win!")
        elif choice3 == "TURN BACK":
            print("You turn back, but the mansion seems to shift around you. You are lost forever. Game over.")
        else:
            print("Invalid choice. Please restart.")
    
    elif choice2 == "CHECK ATTIC":
        print("\nYou climb up to the attic and find an old chest.")
        print("What do you do?")
        print("Options: OPEN CHEST, LEAVE ATTIC")
        choice3 = input("Your choice: ").strip().upper()
        
        if choice3 == "OPEN CHEST":
            print("The chest contains a map of the desert. Using it, you find your way out. You win!")
        elif choice3 == "LEAVE ATTIC":
            print("As you leave the attic, the floor collapses beneath you. Game over.")
        else:
            print("Invalid choice. Please restart.")
    
    else:
        print("Invalid choice. Please restart.")

elif choice1 == "SEARCH":
    print("\nYou decide to search for an exit. The doors and windows are all locked.")
    print("Where do you look?")
    print("Options: LOOK AT DOOR, CHECK WINDOWS, SEARCH CLOSET")
    choice2 = input("Your choice: ").strip().upper()
    
    if choice2 == "LOOK AT DOOR":
        print("\nYou find the door locked, but you notice something strange on the doorknob.")
        print("What do you do?")
        print("Options: TOUCH DOORKNOB, LOOK AROUND THE ROOM")
        choice3 = input("Your choice: ").strip().upper()
        
        if choice3 == "TOUCH DOORKNOB":
            print("The doorknob triggers a hidden trap, and the room starts to flood with sand. Game over.")
        elif choice3 == "LOOK AROUND THE ROOM":
            print("You find a hidden key behind a painting! You unlock the door and escape into the desert. You win!")
        else:
            print("Invalid choice. Please restart.")
    
    elif choice2 == "CHECK WINDOWS":
        print("\nThe windows are boarded up tightly, but you spot a small crack.")
        print("What do you do?")
        print("Options: TRY TO BREAK WINDOW, WAIT FOR STORM TO PASS, SEARCH THE ROOM")
        choice3 = input("Your choice: ").strip().upper()
        
        if choice3 == "TRY TO BREAK WINDOW":
            print("The window shatters, and the storm outside gets worse. A sandstorm swallows you, and you can't see. Game over.")
        elif choice3 == "WAIT FOR STORM TO PASS":
            print("The storm passes after a while, and you use the opportunity to break the window and escape. You win!")
        elif choice3 == "SEARCH THE ROOM":
            print("You find a hidden passage leading out of the mansion. You escape into the desert. You win!")
        else:
            print("Invalid choice. Please restart.")
    
    elif choice2 == "SEARCH CLOSET":
        print("\nYou search the closet and find a journal filled with strange symbols.")
        print("What do you do?")
        print("Options: READ JOURNAL, LEAVE CLOSET")
        choice3 = input("Your choice: ").strip().upper()
        
        if choice3 == "READ JOURNAL":
            print("The journal contains clues about the mansion's history and reveals a hidden exit. You win!")
        elif choice3 == "LEAVE CLOSET":
            print("As you leave the closet, a trapdoor opens bellow you. You fall into darkness. Game over.")
        else:
            print("Invalid choice. Please restart.")
    
    else:
        print("Invalid choice. Please restart.")

elif choice1 == "SHOUT":
    print("\nYou shout into the darkness, and the echo seems to answer back.")
    print("What do you do?")
    print("Options: RUN, HIDE, WAIT")
    choice2 = input("Your choice: ").strip().upper()
    
    if choice2 == "RUN":
        print("\nYou run towards the door, but the mansion seems to stretch endlessly. You get lost in it. Game over.")
    
    elif choice2 == "HIDE":
        print("\nYou find a small closet and hide inside. After a while, the mansion goes silent.")
        print("What do you do?")
        print("Options: COME OUT, WAIT")
        choice3 = input("Your choice: ").strip().upper()
        
        if choice3 == "COME OUT":
            print("You come out and find a way to escape the mansion. You win!")
        elif choice3 == "WAIT":
            print("You wait too long and the mansion collapses around you. Game over.")
        else:
            print("Invalid choice. Please restart.")
    
    elif choice2 == "WAIT":
        print("\nYou wait quietly, hoping for help. Hours pass, but no one comes.")
        print("What do you do?")
        print("Options: WAIT LONGER, MOVE AROUND")
        choice3 = input("Your choice: ").strip().upper()
        
        if choice3 == "MOVE AROUND":
            print("As you move around, you find clues and you manage to escape into the desert. You win!")
        elif choice3 == "WAIT LONGER":
            print("As you wait longer, the mansion seems to close in on you. You are trapped forever. Game over.")
        else:
            print("Invalid choice. Please restart.")
    
    else:
        print("Invalid choice. Please restart.")

else:
    print("Invalid choice. Please restart.")
