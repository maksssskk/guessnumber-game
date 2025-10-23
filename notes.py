notes = []
work = True
print("\033[1mHi!\033[0m\nYou're in Notes!\nPlease, choose a command:")
while work:
    print("\n\033[1mCommands list:\033[0m\n1 - New note\n2 - Save note\n3 - Show notes\n4 - Delete note\n5 - Quit\n")
    com = int(input("Enter command: "))
    if com == 1:
        note = input("Note:")
        print("Wrire '2' for saving")
        com = int(input("Enter command: "))
        if com == 2:
            notes.append(note)
            print("Successfully saved!")
    elif com == 2:
        print("There's nothing to save! Please, enter '1' for adding some notes")
    elif com == 3:
        if not notes:
            print("There's nothing to save! Please, enter '1' for adding some notes")
        else:
            for i in notes:
                print(i)
    elif com == 4:
        for i in notes:
            print(i)
        num_note = int(input("\nEnter a note number: ")) - 1
        if 0 <= num_note < len(notes):
            d = notes.pop(num_note)
            print(f"Note '{d}' is deleted successfully!")
        else:
            print("This note doesnt exist")
    elif com == 5:
        print("Program is ended")
        work = False
    else:
        print("You entered invalid number")
        

