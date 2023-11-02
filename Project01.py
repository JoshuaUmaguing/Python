#I added a loop statement where it asks the user if he wishes to restart again
while True:
    
    print("Please enter the following: ")
    adjective = input("\nadjective: ")
    animal = input("animal: ")
    verb = input("verb: ")
    exclamation = input("exclamation: ")
    verb2 = input("verb: ")
    verb3 = input("verb: ")
    print("\nYour story is: ")
    print("The other day, I was really in trouble. It all started when I saw a very")
    print(f"{adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all")
    print(f"I could think to do was to {verb2} over and over. Miraculously,")
    print(f"that caused it to stop, but not before it tried to {verb3}")
    print("right in front of my family.")
    answer = input("\nWould you like to try again? Yes/No: ")
    if answer.capitalize() != "Yes":
        break
