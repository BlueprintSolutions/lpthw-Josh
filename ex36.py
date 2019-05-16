from sys import exit

def bedroom(): #Option A
    print("now that you are awake, where shall we go next ")
    print("The Bathroom? (bathroom)")
    print("The Toilet? (toilet)")
    print("The coffee machine (coffee machine)?")

    next = input ("Where to next > ")

    if next == "bathroom":
        bathroom()

    elif next == "toilet":
        toilet()

    elif next == "coffee machine":
        coffeemachine()

    else:
        print("You did not pick a viable option try again")
        bedroom()

def bathroom():
    print("What are your going to do in the bathroom?")
    print("Brush your teeth? (toothbrush)")
    print("Have a shower? (shower)")
    print("Have Tablets? (tablets)")
    have_shower = False

    while True:
        next = input ("What action will you take > ")

        if next == "shower":
            print("Great let's get undressed and have a shower")
            have_shower = True
            print("what shall we do next?")
            print("Brush your teeth?")
            print("Have tablets?")

        elif next == "toothbrush" and have_shower:
            print("let's brush our teeth")
            print("what should we do next?")
            bathroom()

        elif next == "toothbrush" and not have_shower:
            print("You need to have a shower first")
            bathroom()

        elif next == "tablets" and have_shower:
            print("It's time to take your tablets")
            print("Where shall we go now?")
            office()

        elif next == "tablets" and not have_shower:
            print("You need to have a shower first")
            # bathroom() # wondering if I need this line in here to start them again?

        else:
            print("you did no select a viable option, try again")
            bathroom()

def toilet():
    print("Feel better, you have done your toilet break?")
    print("Where too next?")
    print("The bathroom? (bathroom)")
    print("The coffee machine? (coffee machine)")

    next = input("Where to next > ")

    if next == "Bathroom":
        bathroom()

    elif next == "coffee machine":
        coffeemachine()

    else:
        print("Where do you think you are going?")
        print("You fall down a hole and die")
        dead("Really should learn how to type correct mate you are dead.")

def coffeemachine():
    print("Ahh the best way to start the day")
    print("what sort of coffee will you have?")
    print("Latte")
    print("Long black")
    print("flat white")

    next = input("Select your coffee >  ")

    if next == "latte":
        print("A good choice")
        print("Now that you have made your coffee shall we head to the office?")
        go_to_office()

    if next == "Long Black":
        print("I think you could of picked a better coffee")
        dead("You should really of picked a better type of coffee!")

    if next == "flat white":
        print("Now this is a good coffee")
        print("lets head to the office")
        office()

def go_to_office():
    print("Yes/No?")

    next = input ("> ")

    if next == "yes":
        office()

    elif next == "no":
        bedroom()

def office():
    print("Congratulations you made it through your morning routine")
    print("Now you can sit down and begin your work.")
    print("Do you wish to start again? Yes / No")

    next = input ("> ")

    if next == "Yes":
        start()

    elif next == "No":
        dead("welcome to the end of the game")

    else:
        print("That wasn't an option so we will end this roleplay")
        dead("welcome to the end of the game")


def audiobook(): #Option C
    print ("What genre do you want to listen too?")
    print ("Fantasy")
    print ("War")
    print ("non-fiction")

    next = input("> ")

    if next == "Fantasy":
        print("That's a great choice lets put that on now")
        print("It has been over 30 minutes you should get out of bed")
        bedroom()

    elif next == "War":
        print("You are not going to get too scared are you?")
        print("It has been over 30 minutes you should get out of bed")
        bedroom()

    elif next == "non-fiction":
        print("well that's an interesting choice.")
        print("A dragon flies out of the book and burns you alive")
        dead("Well that was an interesting way to go")

    else:
        print("I don't think you have that kind of book yet")
        audiobook()


def dead(why):
    print(why, "Good Job!")
    exit(o)

def start():
    print("Your alarm starts to go off in the morning what do you do?")
    print("A: Get out of bed before the misses kicks your out?")
    print("B: Roll over and go back to sleep?")
    print("C: Listen to an audio book?")
    print("Remember you can only choose a,b or c (case sensitive)")

    next = input("> ")

    if next == "a":
        print("Well seems we are in agreement")
        bedroom()

    elif next == "b":
        print("Really? lets try that again")
        start()

    elif next == "c":
        audiobook()

    else:
        dead("")

start()
