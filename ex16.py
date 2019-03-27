from sys import argv #Imports the functions of argv package from python

script, filename = argv #set's the variables of argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do what that, hit RETURN.")

input("?") #allows the user to enter any data for this exercise we are wanting thim to hit RETURN or CTRL-C

print("Opening the file...") #Shows the text "Opening the file..." on the users screen
target = open(filename, 'w') #w tells python that when we are opening this file that we are looking to write to the file.

print("truncating the file. Goodbye!") #Shows the text inside the brackets on screen.
target.truncate() #goes to the start of the document and completley wipes the document.

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ") #asks the user to input data for line 1
line2 = input("line 2: ") #asks the user to input data for line 2
line3 = input("line 3: ") #asks the user to input date for line 3

print("I'm going to write these to the file.") Shows the text inside the brackets on screen.

target.write(line1 +"\n" + line2 + "\n" + line3 + "\n") #written target.write to 1 line instead of 3.
#writes the 3 lines entered by the user to the file located in filename

#target.write(line1)
#target.write ("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("and finally, we close it.") #Shows the text inside the brackets on screen.
target.close() #closes the file after we have completed with it

print(">>>> argv=", repr(argv)) #using this each exercise to see what the script is saying.

target2 = open(filename, 'r') #r tells python that when opening this file we are looking to read the file and not write.
#opens the file that we are looking to read
print(target2.read()) #reads the file that we have opened in the previous step and print's the contents of that file on the screen.

target2.close() #closes the file that was opened by the user.
