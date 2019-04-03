from sys import argv #Imports the functions of argv package from python

script, input_file = argv #sets up the variables of argv

def print_all(f): #defines the file as f
    print(">>> print_all: f=", f) # Start of debug script to show how the code is being interpretted by the computer.
    print(f.read()) #opens the current_file as f in read only mode
    print("<<< print_all: f=", f) #end of debug script

def rewind(f): #rewind is from old tape days so need to call Rewind to then seek a spot in that file.
    f.seek(0) #is a way to seek a spot inside a file. In this case we want to be at the start of the document which is postion 0

def print_a_line(line_count, f): #Shows what is inside the document in the terminal for the user.
    print(line_count, f.readline()) #

current_file = open(input_file) #opens the file as referenced in argv

print(f"First Let's print the whole file:\n") #Shows the text inside the brackets on screen.

print_all(current_file) #Shows the text inside the input_file on the screen

print("Now let's rewind, kind of like a tape") #Shows the text inside the brackets on screen.

rewind(current_file) #moves the current position of in the file to the start. As previously the positon in the file was at the very end of the file due to the read function

print("Let's print threee lines:") #Shows the text inside the brackets on screen.

current_line = 1 #current_line = 1 #defines the variable for current_line as 1
print(">>> print: current_line",current_line) #start of debug script to show what the current line is
print_a_line(current_line, current_file) #prints the information for the current line , but interestingly not the current_file so must be using current_file to reference where it is printing the current_line from.
print("<<< print: current_line", current_line) #end of debug script

current_line = current_line + 1 #current_line = 2 #Takes the variable current line and adds 1 to it.
print(">>> print: current_line",current_line) #start of debug script to show what the current line is
print_a_line(current_line, current_file) #prints the information for the current line , but interestingly not the current_file so must be using current_file to reference where it is printing the current_line from.
print("<<< print: current_line", current_line) #end of debug script

current_line = current_line + 1 #current_line = 3 #Takes the variable current line and adds 1 to it.
print(">>> print: current_line",current_line) #start of debug script to show what the current line is
print_a_line(current_line, current_file) #prints the information for the current line , but interestingly not the current_file so must be using current_file to reference where it is printing the current_line from.
print("<<< print: current_line", current_line) #end of debug script

print("Let's print threee lines using += for LPTHW:") #Shows the text inside the brackets on screen.

current_line = 1 #current_line = 1 #defines the variable for current_line as 1
print(">>> print: current_line",current_line) #start of debug script to show what the current line is
print_a_line(current_line, current_file) #prints the information for the current line , but interestingly not the current_file so must be using current_file to reference where it is printing the current_line from.
print("<<< print: current_line", current_line) #end of debug script

current_line += 1 #current_line = 2 #Takes the variable current line and adds 1 to it.
print(">>> print: current_line",current_line) #start of debug script to show what the current line is
print_a_line(current_line, current_file) #prints the information for the current line , but interestingly not the current_file so must be using current_file to reference where it is printing the current_line from.
print("<<< print: current_line", current_line) #end of debug script

current_line += 1 #current_line = 3 #Takes the variable current line and adds 1 to it.
print(">>> print: current_line",current_line) #start of debug script to show what the current line is
print_a_line(current_line, current_file) #prints the information for the current line , but interestingly not the current_file so must be using current_file to reference where it is printing the current_line from.
print("<<< print: current_line", current_line) #end of debug script
