print("You enter a dark room with two doors. Do you through door #1 or door #2?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake?")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The beat eats your legs off. Good Job!")
    else:
        print(f"well doing {bear} is probably better. Bear runs away")

elif door == "2":
    print("you stare into the endless abyss at cthulhu's retina.")
    print("1. Blueberries")
    print("2. Yellow Jackt clothespins")
    print("3. Understanding revolvers yelling melodies")
    print("4. Why am I looking into the abyss?")
    print("6. pick a number between 5 and 400 the voice says.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    elif insanity == "4":
        print("because I think you are crazy.")
    elif insanity >= "5": #new section that I added
        print("well you just had to go and break the system didn't you?")
        print("Now a demon has appeared what are your going to do?")
        print("1. Run away")
        print("2. pick-up the rusty sword and slice your throat?")
        print("3. Charge the demon?")
        demon_action = input("Choose wisely my leige > ")

        if demon_action == "1":
            print("The demon hunts you down and sucks out your soul. Congratulations you are dead.")

        elif demon_action == "2":
            print("Well not the way you where anticipating to go, but what the hell.")

        elif demon_action == "3":
            print("really? The demon falls over laughing at your stupidity")

        else:
            print("That wasn't an option, START AGAIN!")

    else:
        print("The intensity rots your eyes into a pool of muck. Good Job!")


else:
    print("You stumble around and fall on a knife and die. Good job!")
