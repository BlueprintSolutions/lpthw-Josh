from sys import argv

script, user_name, script_name = argv #added an extra variable for script_name
prompt = 'answer here: ' #changes the data for what the prompt will show

print(f"hi {user_name}, I'm the {script} script.")
print(f"but I like to be known as {script_name}.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print(f"what kind of computer do you have {user_name}?")
computer = input(prompt)

print(f"what kind of dog do you have living with you at {lives}?") #added another arguement to use in script
dog = input(prompt)

print(">>>> argv=", repr(argv)) #using this each exercise to see what the script is saying.

print(f"""
Alright {user_name}, so you said {likes} about liking me ({script_name}).""", end=' ')
if likes == ("No"): #had a play here based on the Zorg game of trying to get a variable outcome for if I said something.
    print ("well that makes me upset", end=' ')
elif likes == ("Yes"):
    print ("Ow you make me so happy", end=' ')
print(f"""
You live in {lives}. Not sure where that is.
You have a {dog}, man that's an ugly {dog}
And you have a {computer} computer. Nice.
""")

#if likes == ("No"): #me working out how to make the if this than that function work
    #print ("well that makes me upset")
#elif likes == ("Yes"):
    #print ("ow you make me so happy")



#text book example which is incorrect for pythong 3.7 and above.

#print "Hi %s, I'm the %s script." % (user_name, script)
#print "I'd like to ask you a few questions."
#print "Do you like me %s?" % user_name
#likes = input(prompt)

#print "where do you live %s?" % user_name
#lives = input(prompt)

#print "What kind of computer do you have?"
#computer = input(prompt)

#print """
#Alright so you said %r about liking me.
#You live in %r. Not sure where that is.
#And you have a %r computer. Nice.
#"""
#% (likes, lives, computer)
#print(">>>> argv=", repr(argv))
