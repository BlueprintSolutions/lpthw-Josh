from sys import exit
from random import randint # imports the random function of python (https://www.geeksforgeeks.org/python-randint-function)
from textwrap import dedent # makes it easier to print lines, without indents


class Scene(object):

    def enter(self):
        print("This scence is not yet configured. Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # DEBUG: print(">>>> PLAY: current_scene = ", current_scene, "last_scene = ", last_scene, "scene_map = ", scene_map)
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        # DEBUG: print("^^^ BEFORE while: current_scene = ", current_scene, "last_scene = ", last_scene, "scene_map = ", scene_map)

        while current_scene != last_scene:
            # DEBUG: print("^^^ TOP of while: current_scene = ", current_scene, "last_scene = ", last_scene, "scene_map = ", scene_map)
            print("\n --------------------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            # DEBUG: print("^^^ END of while: current_scene = ", current_scene, "last_scene = ", last_scene, "scene_map = ", scene_map, "next_scene_name = ", next_scene_name)"

        # be sure to print out the last scene
        # DEBUG: print("^^^ END of PLAY: current_scene = ", current_scene, "last_scene = ", last_scene, "scene_map = ", scene_map, "next_scene_name = ", next_scene_name)"
        current_scene.enter()

class Death(Scene):
# This is when the player dies and should be something funny
    death_quotes = [
    "You died. You kinda suck at this.",
    "Your mum would be proud... if she were smarter",
    "Such a luser",
    "I have a small puppy that's better at this."
    ]

    def enter(self):
        print(Death.death_quotes[randint(0,len(self.death_quotes)-1)]) # randomly selects one of the death Scenes above
        exit(1) #the user is exited out of the game.

#added a finished scence so closes off the loop nicely
class Finished(Scene):
# This is when the player successfully finishes the a_game
    finish_notes = [
    "Congratulations you slayed this game.",
    "I don't know if you could of played this game better or not.",
    "Well that was over too quick, wasn't it."
    ]


    def enter(self):
        print(Finished.finish_notes[randint(0,len(self.finish_notes)-1)]) # randomly selects one of the Dinish notes.
        print("Do you wish to play again?")
        choice = input("Y/N > ")

        if choice == "Y":
            return 'central_corridor' # not sure why this one not working.

        elif choice == "N":
            exit(1)

        else:
            exit(1)


class CentralCorridor(Scene):
# This is the starting point and has Gothon already standing there which the player has to defeat with a joke before continuing.

    def enter(self):
        # this is how to use dedent instead of writing print for every line
        print(dedent("""
            The Gothons of planet Percal #25 have invaded your ship and destroyed
            Your entire crew. You are the last surviving member, an your last
            Mission is to get the neutron destruct bomb from the Weapons Armory,
            put it in the bridge and blow the ship up after getting into an
            escape pod

            You're running down the central corridor to the Weapons Armory when
            a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
            costume flowing around his hate filled body, He's blocking the door
            to the Armory and about to pull a weapon to blast you.

            Do you?
            A: Shoot the Gothon? (shoot!)
            B: Jump out of the way and Dodge the Gothon? (dodge!), or
            C: Tell the Gothon a joke? (tell a joke)
            """))

        action = input(">  ")

        if action == "shoot!":
            print("Quick on the draw you yank out your blaster and fire it at the Gothon")
            print("His clown costume is flowing and moving around his body, which throws")
            print("off your aim. Your laser hits his costume but misses him entirely. This")
            print("completley ruins his brand new costume his mother bought him, which")
            print("make him fly into a rage and blast you repeatedly in the face until")
            print("you are dead. Then he eats you")
            return 'death'

        elif action == "dodge!":
            print("Like a world class boxer you dodge, weave, slip and slide right")
            print("as the Gothon's blaster crankes a laser past your head")
            print("In the midde of your artful dodge your goot slips and you")
            print("bang your head on the metal wall and pass out.")
            print("You wake up shortly after only to die as the Gothon stomps on")
            print("your head and eats you")
            return 'death'

        elif action == "tell a joke":
            print("Lucky for you they made you learn Gothon insults in the academy")
            print("You tell the one Gothon joke you know:")
            print("Lbhe zbgure vf fb sng, jura fur, fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr")
            print("The Gothon stops, tries not to laugh, then bursts out laughing and he can't move")
            print("While he's laughing you run up and shoot him square in the head.")
            print("Putting him down, then jump through the Weapon Armory door.")
            return 'laser_weapon_armory'

        else:
            print("Does not Compute!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
# This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod.
# It has a keypad he has to guess the number for. (Use Randint function for this).

    def enter(self):
        print("You dive roll into the Weapon Armory, crouch and scan the room")
        print("for more Gothons that might be hiding. It's dead quite.")
        print("You stand up and run to the far side of the room and find the")
        print("neutron bomb in it's container. There's a keyboard lock on the box")
        print("and you need the code to get the bomb out. If you get the code")
        print("wrong 10 times the lock closes forever and you can't")
        print("get the bomb. The code is 3 digits from 1-9")

        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9)) # not sure if this is right to generate the numbers in python 3.
        guess = int(input("[keypad] >  "))
        guesses = 0

        while guess != code and guesses < 10 and guess != 999: # added and guess != 999 for the cheat code.
            print(f"BZZZZEDD! that was guess number: {guesses}")
            guesses += 1
            guess = input("[keypad] >  ")

        if guess == code:
            print("The container clicks open and the seal breaks, letting gas out")
            print("You grab the neuron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot")
            return 'the_bridge'

        elif guess == 999: #cheat code
            print("That was a cheat code!")
            print("The container clicks open and the seal breaks, letting gas out")
            print("You grab the neuron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot")
            return 'the_bridge'

        else:
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sound as the mechanism is fused together")
            print("you decide to sit there, and finally the Gothons blow up the")
            print("ship from their ship and you die")
            return 'death'

class TheBridge(Scene):
# Another battle scene with a Gothon where the hero places the bomb.

    def enter(self):
        print("You burst onto the Bridge with the nutron destruct bomb")
        print("Under your arm and surprise 5 Gothons who are trying to")
        print("take control of the ship. Each of them has an even uglier")
        print("clown costume than the last. They haven't pulled their")
        print("weapons out yet, as they see the active bomb under your")
        print("arm and don't want to set it off.\n")
        print("what will you do?")
        print("A: Throw the bomb (throw the bomb)")
        print("B: slowly place the bomb (slowly place the bomb)")

        action = input("> ")

        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of Gothons")
            print("and make a leap for the door. Right as you drop it a")
            print("Gothon shoots you right in the back killing you.")
            print("As you die you see another Gothon frantically try to disarm")
            print("the bomb. you die knowing they will probably blow up when")
            print("it goes off.")
            return 'death'

        elif action == 'slowly place the bomb':
            print("You point your blaster at the bomb under your arm")
            print("and the Gothons put thier hands up and start to sweat.")
            print("you inch backward to the door, open it, and then carefully")
            print("place the bomb on the floor, pointing your blaster at it.")
            print("You then jump ack through the door, punch the close button")
            print("and blast the lock so the Gothons can't get out.")
            print("Now that the bomb is placed you run to the escape pod to")
            print("Get off this tin can")
            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'

class EscapePod(Scene):
# Where the hero escapes but only after guessing the right escape pod.

    def enter(self):
        print("You rush through the ship desperately trying to make it to")
        print("the escape pod before the whole ship explodes. It seems like")
        print("hardly any Gothons are on the ship, so your run is clear of")
        print("interference. You get to the chamber with the escape pods, and")
        print("now need to pick on to take. Some of them could be damaged")
        print("but you don't have time to look. There's 5 pods, which one")
        print("do you take?")

        good_pod = randint(1,5)
        guess = input("[Pod #] > ")

        if int(guess) != good_pod and int(guess) != 4:
            print(f"You jump into pod {guess} and hit the eject button.")
            print("The pod escapes out inot the void of space, then")
            print("implodes as the hull ruptures, crushing your body")
            print("Into jam jelly.")
            return 'death'

        elif int(guess) == 4:
                print("you are such a cheater!")
                print(f"You jump into pod {guess} and hit the eject button.")
                print("The pod easily slides out into space heading to")
                print("the planet below. As it flies to the planet, your look")
                print("back and see your ship implode then explode like a")
                print("bright star, taking out the Gothon ship at the same time.")
                print("YOU WON!")
                return 'finished'

        else:
            print(f"You jump into pod {guess} and hit the eject button.")
            print("The pod easily slides out into space heading to")
            print("the planet below. As it flies to the planet, your look")
            print("back and see your ship implode then explode like a")
            print("bright star, taking out the Gothon ship at the same time.")
            print("YOU WON!")
            return 'finished'

class Map(object):
# storing each scene by name in a dictionary, then refer back to dict with map.scences
    scenes = { #dict
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
