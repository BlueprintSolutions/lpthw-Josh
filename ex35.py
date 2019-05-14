from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    next = input("> ")
    if int(next) in range(0, 100):
    #"0" in next or "1" in next: # this was the original code.
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("""There is a bear here
    The bear has a bunch of honey
    The fat bear is in front of another door
    How are you going to move the bear?""") # moved this print line to just be 1 print.
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("""Here you see that great evil cthulhu
    He, it, whater stares at you and you go insane
    Do you flee for your life or eat your head?""") # moved this print line to just be 1 print.
    cthulhu_alive = False

    while True:
        next = input("> ")

        if next == "flee":
            start()
        elif next == "stab the cthulhu" and not cthulhu_alive:
            print("You stabbed the cthulhu, How are you going to kill it?")
            cthulhu_alive = True
        elif next == "slice throat" and cthulhu_alive:
            print("You have successfully slain the Cthulhu, you can now open the door")
        elif next == "open door" and cthulhu_alive:
            print("You open the door")
            gold_room()
        elif next == "head" in next:
            dead("well that was tasty")
        else:
            print("I guess you got eaten by the cthulhu, try again")
            cthulhu_room()

        # This was the original code
        # if "flee" in next:
            # start()
        # elif "head" in next:
            # dead("well that was tasty!")
        # else:
            # cthulhu_room()


def dead(why):
    print(why,"Good job!")
    exit(0)

    print("""
    Q: Draw a map of the game and how you flow through it.
    A:

    Q: Fix all your mistakes, including spelling mistakes.
    A: Done.

    Q: Write comments for the function you do not understand. Remember doc comments?
    A: Done see code.

    Q: Add more to the game. What can you do to both simplify and expand it?
    A: See comments in the code.

    Q: The gold_room has a weird way of getting you to type a number. What are all the bugs in this way of doing it? Can you make it better than just checking if "1" or "0" are in the number? Look at how int() works for clues.
    A:see comments in the code.
    """)

def start():
    print("""Your in a dark room
    There is a door to your right and left.
    which one do you take?""")# moved this print line to just be 1 print.

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stubmle around the room until you starve.")


start()
